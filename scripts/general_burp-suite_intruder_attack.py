#!/usr/bin/python3
import requests
import json
import time
from datetime import datetime

# ============================================
# CONFIGURATION (EDIT AS NEEDED)
# ============================================

CONFIG = {
    # Base API URL; can insert placeholders dynamically
    "base_url": "https://example.com/api/resource/{uuid}",

    # Optional: Add query parameters dynamically
    "query_params": {
        "include": "details",
        # example: "id": "{uuid}"  # dynamic insertion
    },

    # Optional: Add headers (token or custom fields)
    "headers": {
        "Authorization": "Bearer YOUR_TOKEN_HERE",
        "User-Agent": "UUID-Scanner/1.0"
    },

    # File containing UUIDs or IDs (one per line)
    "input_file": "uuids.txt",

    # Output JSON log
    "output_file": "results.json",

    # Delay between requests (seconds)
    "delay": 0.01,

    # How many characters of body to print
    "preview_length": 120
}

# ============================================
# CORE SCRIPT
# ============================================

def load_input_list(path):
    """Load UUIDs or values from a text file, stripping whitespace."""
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def save_json_log(path, data):
    """Save results to JSON file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def make_request(uuid_value, config):
    """Build and send a GET request."""
    # Build dynamic URL
    url = config["base_url"].format(uuid=uuid_value)

    # Build dynamic query parameters
    params = {}
    for key, val in config["query_params"].items():
        # Insert {uuid} inside query params if needed
        params[key] = val.format(uuid=uuid_value)

    # Build headers
    headers = config["headers"]

    # Send GET request
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        return response
    except requests.RequestException as e:
        return e


def main():
    input_values = load_input_list(CONFIG["input_file"])
    results = []

    print(f"[+] Loaded {len(input_values)} UUID values from {CONFIG['input_file']}")
    print("[+] Starting requests...\n")

    for index, uuid_value in enumerate(input_values, start=1):
        response = make_request(uuid_value, CONFIG)
        timestamp = datetime.utcnow().isoformat()

        # Handle request exception
        if isinstance(response, Exception):
            print(f"[{index}] ERROR for {uuid_value}: {response}")
            results.append({
                "uuid": uuid_value,
                "timestamp": timestamp,
                "error": str(response)
            })
            continue

        # Create log entry
        preview = response.text[:CONFIG["preview_length"]].replace("\n", "")
        log_entry = {
            "uuid": uuid_value,
            "timestamp": timestamp,
            "status": response.status_code,
            "url": response.url,
            "preview": preview,
            "full_body": response.text
        }
        results.append(log_entry)

        # Print terminal feedback
        print(f"[{index}] {uuid_value} → {response.status_code} | {preview}")

        # Delay
        time.sleep(CONFIG["delay"])

    # Save JSON log
    save_json_log(CONFIG["output_file"], results)
    print(f"\n[+] Completed. Output saved to {CONFIG['output_file']}")


if __name__ == "__main__":
    main()
