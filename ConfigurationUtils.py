import glob
import json
import ConfigurationDTO


def GetModuleCodes():

    if glob.glob('./configurations.json'):
        GetConfigurations()

    else:
        structure = {
            "core": "CORE",
            "calculators": "CALCULATORS",
            "flowcredit": "FLOWCREDIT",
            "collections": "COLLECTIONS",
            "risk": "RISK",
            "scoring": "SCORING",
            "externalServices": "EXTERNALSERVICES"
        }

        SetConfigurations(structure)

    pass


def SetConfigurations(structure):
    json.dumps(structure)
    pass


def GetConfigurations():
    json.loads("../configurations.json")
    pass


GetModuleCodes()
