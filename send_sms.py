# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

def sms(num):
    phone='+918838197753'
    account_sid = 'AC1939650b5c19da5c9f0df88e113a74c4'
    auth_token = '3ae1fbfde7f45923452f5917b50b2116'
    client = Client(account_sid, auth_token)
    if num=='101':
        phone='+919994735455'
    message = client.messages \
          .create(
              body='Someone tried to open your car!',
              from_='+15082327026',
              to=phone
              )
    print('Message sent')
