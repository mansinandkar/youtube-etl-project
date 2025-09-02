from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access secrets
aws_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret = os.getenv("AWS_SECRET_ACCESS_KEY")
bucket = os.getenv("S3_BUCKET")
snowflake_user = os.getenv("SNOWFLAKE_USER")
youtube_api = os.getenv("YOUTUBE_API_KEY")

print("Bucket:", bucket)  # test
