import os
import json
import requests
import boto3
from dotenv import load_dotenv
from datetime import datetime

# Load .env variables
load_dotenv()

aws_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret = os.getenv("AWS_SECRET_ACCESS_KEY")
s3_bucket = os.getenv("S3_BUCKET")
youtube_api = os.getenv("YOUTUBE_API_KEY")

# YouTube API endpoint
channel_id = "UCNU_lfiiWBdtULKOw6X0Dig"  
url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={youtube_api}"

# Call API
response = requests.get(url)
data = response.json()

# Save response to JSON file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"youtube_stats_{timestamp}.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=4)

print(f"Saved API response locally: {filename}")

# Upload to S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_key,
    aws_secret_access_key=aws_secret
)

s3.upload_file(filename, s3_bucket, filename)
print(f"Uploaded {filename} to S3 bucket {s3_bucket}")
