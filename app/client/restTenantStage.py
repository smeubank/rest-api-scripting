# https://gist.github.com/stefansundin/96b655f1512d1ce9d570e008dbe122d3
# http://docs.python-requests.org/en/master/api/
import requests
from client.errorhandling import getstatus
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config = {
    "headers": {'user': "{[]}}", 'Content-Type': "application/json", 'Accept-Language': "de-DE"},
    "host": "{{host}}",
    "path": "{{path}}",
    "agent": "{{agent}}"
}

headers = config["headers"]
host = config["host"]
path = config["path"]


class RequestsApi:
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url()
        self.session = requests.Session()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    def request(self, method, url, **kwargs):
        return self.session.request(method, self.base_url+url, **kwargs)

    def options(self, url, **kwargs):
        return getstatus(lambda: (self.session.options(self.base_url+url, **kwargs, headers=headers, verify=False)))

    def get(self, url, **kwargs):
        return getstatus(lambda: (self.session.get(self.base_url+url, **kwargs, headers=headers, verify=False)))

    def post(self, url, **kwargs):
        return getstatus(lambda: (self.session.post(self.base_url+url, **kwargs, headers=headers, verify=False)))

    def put(self, url, **kwargs):
        return getstatus(lambda: (self.session.put(self.base_url+url, **kwargs, headers=headers, verify=False)))

    def patch(self, url, **kwargs):
        return getstatus(lambda: (self.session.patch(self.base_url+url, **kwargs, headers=headers, verify=False)))

    def delete(self, url, **kwargs):
        return getstatus(lambda: (self.session.delete(self.base_url+url, **kwargs, headers=headers, verify=False)))

    @staticmethod
    def __deep_merge(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestsApi.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination


def _url():
    return config["host"] + config["path"]


rest = RequestsApi(_url)