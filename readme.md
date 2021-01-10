Purpose:

Wiki Guides:

wiki

Tricks:

Dealing with SSL-
def get_contractinfos(customerNumber):
    return requests.get(_url('/search/contractinfos'),
                        headers=config.config["headers"],
                        params={'webUserId': customerNumber},
                        verify=False) #avoids issue with HTTPS calls to the adapter, should resolve in the long run

Dealing with HTML responses-

When testing a new orchestration often there will be many mistakes. To avoid spam from non JSON response, you can add
the following. this also is always good with calls like DEL workflow since it never has a JSON response.

resp = restcalls.del_workflow(workflowId)
try:
   print(resp.json())
except json.decoder.JSONDecodeError:
   print("N'est pas JSON")


Dealing with JSON in Python-

There are some slight modifications to be made when working with JSON files in Python, below examples

    For boolean values like trues, false in Python must be as True, False
    "readOnlyMode" : False,
    
Dealing with an array of objects - 

what in Python is called a list of dictionaries. Like the response of getOfferings

https://stackoverflow.com/questions/7271482/getting-a-list-of-values-from-a-list-of-dicts/7271523#7271523

Inspirations and learning guides:

https://www.pythonforbeginners.com/requests/using-requests-in-python#targetText=Requests%20will%20allow%20you%20to,Python%20in%20the%20same%20way.
https://2.python-requests.org/en/master/user/quickstart/
https://2.python-requests.org/en/master/user/advanced/#advanced
https://realpython.com/api-integration-in-python/
https://realpython.com/python-requests/
https://www.geeksforgeeks.org/get-post-requests-using-python/ google example
https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html
https://stackoverflow.com/questions/2349991/how-to-import-other-python-files
