import json
from client.restTenantStage import rest
import qbpayloads

resp = rest.get("/offerings", params=qbpayloads.offeringParams)
prodOffs = resp.text
offerings = json.loads(prodOffs)
##create an array of the productiOfferingId selfs
productOfferings = [d['self'] for d in offerings]
##then set the variables by each instance in the array
productOfferingP1 = productOfferings[0]
productOfferingP2 = productOfferings[1]
productOfferingP3 = productOfferings[2]

offerings = {
    "productOfferingP1": ""+productOfferingP1+"",
    "productOfferingP2": ""+productOfferingP2+"",
    "productOfferingP3": ""+productOfferingP3+""
}