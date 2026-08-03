import json
import urllib.parse
import urllib.request
from PIL import Image
import cv2
import io
import base64


# CEASER CIPHER DECRYPTION
def decrypt_ceaser(shift, encrypted_text):
	plain_text = ""
	for c in encrypted_text:
	    if c.isupper():
	        c_unicode = ord(c)
	        c_index = ord(c) - ord("A")
	        new_index = (c_index - shift) % 26
	        new_unicode = new_index + ord("A")
	        new_character = chr(new_unicode)
	        plain_text = plain_text + new_character
	    else:
	        plain_text += c
	return plain_text


# SUBSTITUTION CIPHER DECRYPTION
def decrypt_substitution(key, ciphertext):
	key = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', key))
	flipped = {v: k for k, v in key.items()}
	return ''.join(flipped[l] for l in ciphertext)



# GET THE CIPHER TYPE
url = "https://9tz2kcnyme.execute-api.eu-west-1.amazonaws.com/Prod/cipher_type"
API_KEY = 'kDNsRFhwGv9Fqwh57DqdD54DHYsMiciH5BzZLU9g'
headers = {'x-api-key' : API_KEY}

while True:
	try:
		req = urllib.request.Request(url, headers=headers)
		response = urllib.request.urlopen(req).read()
		response = json.loads(response)
		break
	except:
		pass


# GET THE METRIX AND KEY
url = "https://9tz2kcnyme.execute-api.eu-west-1.amazonaws.com/Prod/get_encrypted_text?cipher=" + response['cipher']
while True:
	try:
		req = urllib.request.Request(url, headers=headers)
		response = urllib.request.urlopen(req).read()
		response = json.loads(response)
		break
	except:
		pass

# DECODE
if response['cipher'] == "CAESAR":
	for position, x in enumerate(response['encrypted_matrix']):
		response['encrypted_matrix'][position] = decrypt_ceaser(response['key'], x)

	for position, x in enumerate(response['encrypted_matrix']):
		response['encrypted_matrix'][position] = x[:position] + decrypt_ceaser(response['key'], x[position]) + x[position+1:]

	decrypted_text = ''
	for position, x in enumerate(response['encrypted_matrix']):
		decrypted_text += x[position]

elif response['cipher'] == "SUBSTITUTION":
	for position, x in enumerate(response['encrypted_matrix']):
		response['encrypted_matrix'][position] = decrypt_substitution(response['key'], x)

	for position, x in enumerate(response['encrypted_matrix']):
		response['encrypted_matrix'][position] = x[:position] + decrypt_substitution(response['key'], x[position]) + x[position+1:]

	decrypted_text = ''
	for position, x in enumerate(response['encrypted_matrix']):
		decrypted_text += x[position]



# VERIFY DECODED METRIX
url = "https://9tz2kcnyme.execute-api.eu-west-1.amazonaws.com/Prod/verify_diagonal/"
while True:
	try:
		post_param = json.dumps({
		                    'diagonal' : decrypted_text
		          }).encode()
		req = urllib.request.Request(url, post_param, headers)
		response = urllib.request.urlopen(req)
		response = json.loads(response.read())
		break
	except:
		pass

# CONVERT RESPOSE STRING TO IMAGE AND SHOW
imgdata = base64.b64decode(str(response['response_image']))
image = Image.open(io.BytesIO(imgdata))
image.show()