import random
import re
import hashlib
import string


while True:

    # The salt
    salt = 'a0'

    # Generate random six character string using letters
    input = salt + ''.join(random.choices(string.ascii_letters, k=6)) 
    
    # Find the MD5 digest of the salted input
    digest = hashlib.md5(input.encode()).hexdigest()
    

    # Check if "'='" is in the hexadecimal representation of the digest
    match = re.search(r"273d27", digest)
    
    # If a match is found, check that it starts on an even index, since every two hex characters corrospond to one ASCII character.
    if match and match.start() % 2 == 0:

        # Print the password if it is a match yay
        print("Password:\t", input[2:])
        



