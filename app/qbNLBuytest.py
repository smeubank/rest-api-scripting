import qbNLProductofferings
from client.restTenantStage import rest, config
import json
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

    print("ContractualsId P",P," = ",  contractualsId)

    resp = rest.post('/contractuals/' + contractualsId + '/processtransition',
                     params={'sessionId': sessionId},
                     data=qbpayloads.processpayload(contractualsId))

    resp = rest.post('/contractuals/' + contractualsId + '/processtransition',
                     params={'sessionId': sessionId, 'contractIssuingType': '1'},
                     data=qbpayloads.processpayload(contractualsId))
    policy = resp.json()['contractNumbers'][0]

    print("Policy P",P," = ", policy)

    resp = rest.delete("/worksessions/" + sessionId)

    Endtime = datetime.datetime.now()

    TestDuration = Endtime - Starttime

    print("Total Duration P",P," = ", round(TestDuration.total_seconds(),2), "s")

    P=P+1
