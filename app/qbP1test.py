import qbproductofferings
import json
from client.restTenantStage import rest, config
import qbpayloads

productOffering = qbproductofferings.offerings["productOfferingP1"]
accountManagerNumber = config["agent"]

resp = rest.post("/worksessions",
                 data=qbpayloads.wfpayload())
try:
    sessionId = resp.json()['self']
except (ValueError, NameError, KeyError) as var_err:
        print(f'Problem creating workflow: {var_err}')
        sessionId = '123155'
finally:
# querystring = {"sessionId":sessionId}
    pass

resp = rest.post('/persons',
                 params={"sessionId": sessionId},
                 data=qbpayloads.partypayload(accountManagerNumber),)
partyId = resp.json()['self']

resp = rest.post('/persons/'+personId+'/partyroles',
                 params={"sessionId": sessionId},
                 data=qbpayloads.phpayload(partyId))

resp = rest.post('/properties',
                 params={"sessionId": sessionId},
                 data=qbpayloads.propertyPayload)
propertyId = resp.json()['self']

resp = rest.post('/insuredproperties',
                 params={"sessionId": sessionId},
                 data=qbpayloads.insuredpropertypayload(propertyId))

resp = rest.post('/contractuals',
                 params={"sessionId": sessionId},
                 data=qbpayloads.contractpayload(productOffering))
contractualsId = resp.json()['self']

resp = rest.post('/contractuals/'+contractualsId+'/processtransition',
                 params={'sessionId': sessionId, 'contractIssuingType': '1'},
                 data=qbpayloads.processpayload(contractualsId))

resp = rest.post('/contracts/'+contractualsId+'/processtransition',
                 params={'sessionId': sessionId, 'contractIssuingType': '1'},
                 data=qbpayloads.processpayload(contractualsId))

resp = rest.delete("/workflows/"+sessionId)
try:
   print(resp.json())
except json.decoder.JSONDecodeError:
   print("N'est pas JSON")