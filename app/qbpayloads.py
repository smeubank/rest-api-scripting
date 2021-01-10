import json
#import config

offeringParams = "lineOfBusiness=KB&salesChannel=KU"


def wfpayload():
    return json.dumps({
        "classId": "com.insurancecompany.rest.core.workflow.Workflow",
        "workflowType": "CONTRACT_MANAGEMENT",
        "extEntity": {
            "classId": "com.insurancecompany.rest.ext.extworkflowmanagement.ExtWorkflow",
            "logicalSection": "V_KB",
            "readOnlyMode": False
        }
    })


def partypayload(accountmanagernumber):
    return json.dumps({
        "classId": "com.insurancecompany.rest.core.person.Person",
        "firstName": "Pyint",
        "name": "Test",
        "birthDate": "1981-01-04",
        "genderIdentity": "W",
        "accountManagerNumber": "" + accountmanagernumber + "",
        "dataConsentAgreements": {
            "classId": "com.insurancecompany.rest.core.party.DataConsentAgreement",
            "accepted": True,
            "dataConsent": {
                "classId": "com.insurancecompany.rest.core.party.DataConsent",
                "dataConsentType": "DP"
            }
        },
        "addresses": {
            "classId": "com.insurancecompany.rest.core.contact.Address",
            "countryCode": "NL",
            "city": "Amsterdam",
            "zipCode": "1071 XX",
            "type": "HW"
        }
    })


def phpayload(personId):
    return json.dumps({
        "classId": "com.insurancecompany.rest.core.contract.ContractHolder",
        "party": "" + personId + "",
        "contractHolderType": "J"
    })


propertyPayload = json.dumps({
    "classId": "com.insurancecompany.rest.core.property.Vehicle",
    "propertyType": "KFZP10",
    "propertyCode": "K",
    "usage": "KFZ01",
    "yearOfManufacture": "2016",
    "licensePlateNumber": "97-JF-XC",
    "vehicleIdentificationNumber": "123",
    "isEurotax": False,
    "characteristics": {
        "classId": "com.insurancecompany.rest.core.vehicle.VehicleCharacteristics",
        "vehicleBrand": "BMW",
        "vehicleModel": "X3",
        "vehicleBrandCode": "0005",
        "vehicleModelCode": "AKP",
        "power": "110.0",
        "maximumDesignSpeed": "150",
        "registrationInfo": {
            "classId": "com.insurancecompany.rest.core.property.vehicle.VehicleRegistrationInfo",
            "firstRegistrationDate": "2019-01-01"
        }
    }
})


def insuredpropertypayload(propertyId):
    return json.dumps({
        "classId": "com.insurancecompany.rest.core.property.InsuredProperty",
        "property": "" + propertyId + ""
    })


def contractpayload(productOffering):
    return json.dumps({
        "classId": "com.insurancecompany.rest.core.contract.Contract",
        "self": "" + productOffering + "",
        "inceptionDate": "2019-09-01",
        "contractProcessState": "QUOTATION"
    })


def contractnestedpayloadDE(productOffering, inceptiondate,bmmtpl,bmmod,hsn,tsn,zipcode,birthdate,drivelicense,firstregistration,ownregistration,dataconsent):
    return json.dumps({
        "classId": "com.insurancecompany.rest.core.contract.Contract",
        "self": "" + productOffering + "",
        "inceptionDate": "" + inceptiondate + "",
        "contractProcessState": "QUOTATION",
        "coverages": [{
            "classId": "com.restapi.insurancecompany.core.contract.Coverage",
            "bonusMalusInfoLink": {
                "classId": "com.restapi.insurancecompany.core.property.BonusMalusInformation",
                "bonusMalusLevel": ""+bmmod+""
            },
            "classProductSign": "KK"
        }, {
            "classId": "com.restapi.insurancecompany.core.contract.Coverage",
            "bonusMalusInfoLink": {
                "classId": "com.restapi.insurancecompany.core.property.BonusMalusInformation",
                "bonusMalusLevel": ""+bmmtpl+""
            },
            "classProductSign": "KH"
        }],
        "insuredProperties": [
            {
                "property": {
                    "classId": "com.restapi.insurancecompany.core.property.Vehicle",
                    "vehicleIdentificationNumber": "12387788",
                    "characteristics": {
                        "classId": "com.restapi.insurancecompany.core.vehicle.VehicleCharacteristics",
                        "buildYear": 2013,
                        "cubicCapacity": "1364",
                        "fuelType": "L",
                        "maximumDesignSpeed": 197,
                        "numberOfSeats": 5,
                        "originalPrice": "EUR 22726.89",
                        "power": "50.0",
                        "tare": 1842,
                        "vehicleBrand": "OPEL",
                        "vehicleBrandCode": "" + hsn + "",
                        "vehicleModel": "Mokka",
                        "vehicleModelCode": "" + tsn + "",
                    },
                    "isEurotax": False,
                    "licensePlateNumber": "",
                    "mileageRecords": [{
                        "classId": "com.restapi.insurancecompany.core.vehicle.MileageRecord",
                        "mileage": 14999,
                        "recordDate": "2019-08-29",
                        "recordingReason": "EM"
                    }],
                    "propertyCode": "K",
                    "propertyType": "KFZP10",
                    "registrationInfo": {
                        "classId": "com.restapi.insurancecompany.core.vehicle.VehicleRegistrationInfo",
                        "documentLodgeRegistrationDate": "" + ownregistration + "",
                        "firstRegistrationDate": "" + firstregistration + ""
                    }
                },
                "classId": "com.insurancecompany.rest.core.property.InsuredProperty",
                "premiumRelevance": "H"
            }
        ],
        "parties": [
            {
                "roles": [
                    {
                        "classId": "com.insurancecompany.rest.core.contract.ContractHolder",
                        "contractHolderType": "J",
                        "extEntity": {
                            "classId": "com.insurancecompany.rest.ext.extcontract.ExtContractHolder",
                            "insuredByPartner": True
                        }
                    }
                ],
                "classId": "com.restapi.insurancecompany.core.person.Person",
                "preferredContactChannels": [{
                    "classId": "com.insurancecompany.rest.core.contact.PhoneChannel",
                    "phoneNumber": "5552563654",
                    "mobile": True,
                    "preferred": "True"
                }, {
                    "classId": "com.insurancecompany.rest.core.contact.EmailChannel",
                    "email": "test@test.com"
                }],
                "dataConsentAgreements": {
                    "classId": "com.insurancecompany.rest.core.party.DataConsentAgreement",
                    "accepted": "" + dataconsent + "",
                    "dataConsent": {
                        "classId": "com.insurancecompany.rest.core.party.DataConsent",
                        "dataConsentType": "DP"
                    }
                },
                "accountManagerNumber": "1000001",
                "addresses": [{
                    "classId": "com.restapi.insurancecompany.core.contact.Address",
                    "countryCode": "DE",
                    "type": "HW",
                    "zipCode": "" + zipcode + "",
                }],
                "birthDate": "" + birthdate + "",
                "extEntity": {
                    "classId": "com.restapi.insurancecompany.ext.extperson.ExtPerson"
                },
                "firstName": "DEFAULT",
                "genderIdentity": "M",
                "identificationDocuments": [{
                    "classId": "com.restapi.insurancecompany.core.document.IdentityDocument",
                    "issuingDate": "" + drivelicense + "",
                    "type": "1"
                }],
                "name": "DEFAULT",
                "preferredContactChannels": []
            }
        ]
    })

def contractnestedpayloadNL(productOffering, inceptiondate,cfy,AutotelexId,zipcode,birthdate,drivelicense,firstregistration,ownregistration,dataconsent):
    return json.dumps({
        "classId": "com.insurancecompany.rest.core.contract.Contract",
        "self": "" + productOffering + "",
        "inceptionDate": "" + inceptiondate + "",
        "contractProcessState": "QUOTATION",
        "coverages": [{
            "classId": "com.restapi.insurancecompany.core.contract.Coverage",
            "bonusMalusInfoLink": {
                "classId": "com.restapi.insurancecompany.core.property.BonusMalusInformation",
                "bonusMalusLevel": ""+cfy+""
            },
            "classProductSign": "KH"
        }],
        "insuredProperties": [
            {
                "property": {
                    "classId": "com.restapi.insurancecompany.core.property.Vehicle",
                    "vehicleIdentificationNumber": "12387788",
                    "characteristics": {
                        "classId": "com.restapi.insurancecompany.core.vehicle.VehicleCharacteristics",
                        "buildYear": 2013,
                        "cubicCapacity": "1364",
                        "fuelType": "L",
                        "maximumDesignSpeed": 197,
                        "numberOfSeats": 5,
                        "originalPrice": "EUR 22726.89",
                        "power": "50.0",
                        "tare": 1842,
                        "vehicleBrand": "OPEL",
                        "mainCode": "" + AutotelexId + "",
                        "vehicleModel": "Mokka"
                    },
                    "isEurotax": False,
                    "licensePlateNumber": "",
                    "mileageRecords": [{
                        "classId": "com.restapi.insurancecompany.core.vehicle.MileageRecord",
                        "mileage": 14999,
                        "recordDate": "2019-08-29",
                        "recordingReason": "EM"
                    }],
                    "propertyCode": "K",
                    "propertyType": "KFZP10",
                    "registrationInfo": {
                        "classId": "com.restapi.insurancecompany.core.vehicle.VehicleRegistrationInfo",
                        "documentLodgeRegistrationDate": "" + ownregistration + "",
                        "firstRegistrationDate": "" + firstregistration + ""
                    }
                },
                "classId": "com.insurancecompany.rest.core.property.InsuredProperty",
                "premiumRelevance": "H"
            }
        ],
        "parties": [
            {
                "roles": [
                    {
                        "classId": "com.insurancecompany.rest.core.contract.ContractHolder",
                        "contractHolderType": "J",
                        "extEntity": {
                            "classId": "com.insurancecompany.rest.ext.extcontract.ExtContractHolder",
                            "insuredByPartner": True
                        }
                    }
                ],
                "classId": "com.restapi.insurancecompany.core.person.Person",
                "preferredContactChannels": [{
                    "classId": "com.insurancecompany.rest.core.contact.PhoneChannel",
                    "phoneNumber": "2190717365",
                    "mobile": True,
                    "preferred": "True"
                }, {
                    "classId": "com.insurancecompany.rest.core.contact.EmailChannel",
                    "email": "aerisblue21@mailinator.com"
                }],
                "dataConsentAgreements": {
                    "classId": "com.insurancecompany.rest.core.party.DataConsentAgreement",
                    "accepted": "" + dataconsent + "",
                    "dataConsent": {
                        "classId": "com.insurancecompany.rest.core.party.DataConsent",
                        "dataConsentType": "DP"
                    }
                },
                "accountManagerNumber": "1000008",
                "addresses": [{
                    "classId": "com.restapi.insurancecompany.core.contact.Address",
                    "countryCode": "DE",
                    "type": "HW",
                    "zipCode": "" + zipcode + "",
                }],
                "birthDate": "" + birthdate + "",
                "extEntity": {
                    "classId": "com.restapi.insurancecompany.ext.extperson.ExtPerson"
                },
                "firstName": "DEFAULT",
                "genderIdentity": "M",
                "identificationDocuments": [{
                    "classId": "com.restapi.insurancecompany.core.document.IdentityDocument",
                    "issuingDate": "" + drivelicense + "",
                    "type": "1"
                }],
                "name": "DEFAULT",
                "preferredContactChannels": []
            }
        ]
    })

def processpayload(contractualsId):
    return json.dumps({
        "classId": "com.insurancecompany.rest.core.contract.ContractProcessTransition",
        "contracts": ["" + contractualsId + ""],
        "contractIssuingType": "ONLINE"
    })
