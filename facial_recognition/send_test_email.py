#! /usr/bin/python

# Imports
import requests

def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandbfdgsgdfhdfhsfdasd0652642.mailgun.org/messages",
        auth=("api", "sfsdf3723esdgsgsg-443ecsdgsdg"),
        data={"from": 'refrigeratorwatcher@example.com',
              "to":'@gmail.com',
            "subject": "Visitor Alert",
            "html": "<html> Your Raspberry Pi recognizes someone. </html>"})
                      
request = send_simple_message()
print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))
