import qbDEProductofferings
from client.restTenantStage import rest, config
import json
import qbpayloads
import datetime
from datetime import date

today = str(date.today())

offerings = qbDEProductofferings.offerings

## check that rest GET premium call returns a 403 HTTP code - sysnonym for Camunda returned a Stop action (here because birthdate = 1900-01-01 --> driver too old

offering = offerings[0]
productOfferingsID = offering["self"]
productOfferingsName = offering["name"]
P = 1

print("ProductOffering DE P", P, "= ", productOfferingsName)

Starttime = datetime.datetime.now()

resp = rest.post("/worksessions",
                 data=qbpayloads.wfpayload())
sessionId = resp.json()['self']
# querystring = {"sessionId":sessionId}

resp = rest.post('/contractuals',
                 params={"sessionId": sessionId},
                 data=qbpayloads.contractnestedpayloadDE(productOfferingsID, today, "D03", "D03", "0005", "CBR",
                                                         "80331", "1900-01-01", "2006-05-04", "2015-07-04", today,
                                                         "True"))
contractualsId = resp.json()['self']

print("ContractualsId P", P, " = ", contractualsId)

try:
        resp = rest.get('/contractuals/' + contractualsId + '/premium',
                        params={'sessionId': sessionId})
        resp.raise_for_status()
except:
        if resp.status_code == 403:
            print("HTTP Error Code = ",resp.status_code," --> OK (Stop action from Camunda leads to a 403)")
        else:
            print ("GET /Premium did not return a 403 HTTP Code --> Stop action from Camunda was not triggered")
            exit(1) ## wrong exit in case no HTTP Code 403 was raised
else:
    print ("GET /Premium did not return a 403 HTTP Code --> Stop action from Camunda was not triggered")
    exit(1) ## wrong exit in case no HTTP Code 403 was raised

resp = rest.delete("/worksessions/" + sessionId)

Endtime = datetime.datetime.now()

TestDuration = Endtime - Starttime

print("Total Duration P", P, " = ", round(TestDuration.total_seconds(), 2), "s")
