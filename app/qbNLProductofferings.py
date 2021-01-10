import json
from client.restTenantStage import rest, config
import qbpayloads

resp = rest.get("/offerings", params=qbpayloads.offeringParams)
prodOffs = resp.text
offerings = json.loads(prodOffs)

