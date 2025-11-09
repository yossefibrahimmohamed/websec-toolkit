import requests  # Correct import

# Open the file and read each domain
with open("domains.txt", "r") as file:
    for line in file:
        domain = line.strip()
        if not domain:
            continue  # Skip empty lines

        # Define paths to check
        paths = ["/admin", "/backup", "/adminpanel", "/robots.txt"]  # ...etc

        for path in paths:
            url = domain.rstrip("/") + path  # Ensure proper URL format

            try:
                response = requests.get(url, timeout=5)
                if response.status_code in [200, 301, 403]:
                    print(f"[+] Found path {path} on {domain} (Status: {response.status_code})")
                else:
                    print(f"[-] {path} not found on {domain} (Status: {response.status_code})")
            except requests.RequestException as e:
                print(f"[!] Error checking {url} -> {e}")
