#from mainclass import cisl#from errorslackapi import slack, url, headers
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from client.errorslackapi import slack


def getstatus(x):
    try:
        resp = x()
        resp.raise_for_status()
    except (HTTPError, ConnectionError, Timeout, RequestException) as http_err:
        text = f'{http_err}, {resp.text}'
        print(f'test get status: {http_err}, {resp.text}')  ##{http_err}, {resp.headers}, {resp.text}')
        try:
            slack(lambda: text)
        finally:
            print(f'tried to post to slack ')  ##{http_err}, {resp.headers}, {resp.text}')
    finally:
        return resp



# def get_variable(x):
#     try:
#         something
#     except (ValueError, NameError, KeyError) as var_err:
#         print(f'Probelem getting or setting variable: {var_err}')