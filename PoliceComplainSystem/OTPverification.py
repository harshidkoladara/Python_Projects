import nexmo
from pprint import pprint
import random
otp = "your        OTP           is ...."+ str(random.randint(0,9) )+"   " +  str(random.randint(0,9)) +"   " + str(random.randint(0,9)) +"   " + str(random.randint(0,9) )
otp2 = "    .........    I     repeat " + otp
client = nexmo.Client(
  application_id='619ca1fa-7104-4e90-a72b-ba831956ceb5',
  private_key='private.key',
)
ncco = [ {
    'action': 'talk',
    'voiceName': 'Joey',
    'text': otp + otp2
  }]

response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': '919726753852'
  }],
  'from': {
    'type': 'phone',
    'number': '919726753852'
  },
  'ncco': ncco
})

