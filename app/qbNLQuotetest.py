import qbNLProductofferings
import json
from client.restTenantStage import rest, config
import qbpayloads
import datetime
from datetime import date

today = str(date.today())

offerings = qbNLProductofferings.offerings

offering = offerings[0]

P = 1

for offering in offerings:

    productOfferingsID = offering["self"]
    productOfferingsName = offering["name"]

    print("ProductOffering NL P",P,"= ",productOfferingsName)

    Starttime = datetime.datetime.now()

    resp = rest.post("/worksessions",
                     data=qbpayloads.wfpayload())
    sessionId = resp.json()['self']
    # querystring = {"sessionId":sessionId}

    resp = rest.post('/contractuals',
                     params={"sessionId": sessionId},
                     data=qbpayloads.contractnestedpayloadNL(productOfferingsID, today,"N03","12345","80331","1985-06-04","2006-05-04","2015-07-04",today,"True") )
    contractualsId = resp.json()['self']

    print("contractualsId P",P," = ",  contractualsId)

    resp = rest.get('/contractuals/' + contractualsId + '/premium',
                     params={'sessionId': sessionId})
    Premium = resp.json()['grossPremium']

    if Premium == '0.00':
        print("Premium is equal to 0")
        exit(1)
    else:
        print("Premium P",P," = ",  Premium)

    resp = rest.delete("/worksessions/" + sessionId)
    try:
        print(resp.json())
    except json.decoder.JSONDecodeError:
        print("N'est pas JSON")

    Endtime = datetime.datetime.now()

    TestDuration = Endtime - Starttime

    print("Total Duration P",P," = ", round(TestDuration.total_seconds(),2), "s")

    P=P+1