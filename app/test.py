#import slack, url, headers
from errorslackapi import slack

text = "hello world"

req = slack(text)

print(req.url)
