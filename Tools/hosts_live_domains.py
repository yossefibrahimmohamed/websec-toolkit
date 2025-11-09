import requests

with open("domains.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if not line:  
            continue

        try:
            response = requests.get(line, timeout=5)
            if response.status_code == 200:
                print(f"{line} is 200 OK")
            else:
                print(f"{line} is NOT 200 OK (Status: {response.status_code})")
        except requests.RequestException as e:
            print(f"{line} -> Error: {e}")
