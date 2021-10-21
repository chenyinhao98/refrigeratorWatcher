#! /usr/bin/python

# Imports
import requests

def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandboxe1fc3be9bd514e718ee8b9b690652642.mailgun.org/messages",
        auth=("api", "f5f7cf5393723e903f625de2cbf9743b-443ec20e-d6011f87"),
        data={"from": 'refrigeratorwatcher@example.com',
              "to":'yche0445@student.monash.edu',
            "subject": "Visitor Alert",
            "html": "<html> Your Raspberry Pi recognizes someone. </html>"})
                      
request = send_simple_message()
print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))
