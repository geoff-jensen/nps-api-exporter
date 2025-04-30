from dotenv import load_dotenv
import os
import requests
import json
import csv
import argparse


load_dotenv()  # Loads variables from .env into environment

api_key = os.getenv("NPS_API_KEY")

if not api_key:
    raise ValueError("NPS_API_KEY not found in environment variables!")

#print(f"Using API key: {api_key}")

# Define endpoint and params
url = "https://developer.nps.gov/api/v1/parks"
params = {
    "api_key": api_key,
    "limit": 100,
}

parser = argparse.ArgumentParser(description="Export NPS park data to CSV")
parser.add_argument(
    "--state",
    type=str,
    help="Optional State code to filter parks by (e.g., OR, CA, UT). Defaults to all states."
)
args = parser.parse_args()
if args.state:
    params["stateCode"] = args.state

# Make request
response = requests.get(url, params=params)

data = response.json()

#print(json.dumps(data, indent=2))
#park_keys = data["data"][0].keys()
#print(park_keys)

def flatten_park(park):
    # Flatten activities to a comma-separated string of names
    activities = ", ".join([a["name"] for a in park.get("activities", [])])

    # Flatten operating hours (usually just one item in the list)
    hours_list = park.get("operatingHours", [])
    if hours_list:
        description = hours_list[0].get("description", "")
        standard_hours = hours_list[0].get("standardHours", {})
        # Optional: build a readable schedule from standardHours
        hours = "; ".join([f"{day}: {hours}" for day, hours in standard_hours.items()])
    else:
        description = ""
        hours = ""

    return [
        park.get("id", ""),
        park.get("fullName", ""),
        park.get("description", ""),
        activities,
        f"{description} | {hours}"
    ]




with open("parks_sample_output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Description", "Activities", "Operating Hours"])  # header

    for park in data["data"]:
        writer.writerow(flatten_park(park))

print(f"Exported {len(data['data'])} parks to parks.csv")

# Check for success
# if response.status_code == 200:
#     data = response.json()
#     for park in data["data"]:
#         print(f"{park['fullName']} – {park['states']}")
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)
