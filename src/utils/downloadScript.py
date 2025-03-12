import boto3

# AWS Credentials and Region (Use environment variables or AWS CLI for security)
aws_access_key_id = "AKIAXHND3CRPCBHL2V4A"
aws_secret_access_key = "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"
region_name = "ap-southeast-1"

# Initialize S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# File details
bucket_name = "datascienceproject02"
s3_key = "datasets/preprocessed_movie_data.csv"  # Path of the file in S3
local_file_path = "/home/ec2-user/datasets/preprocessed_movie_data.csv"  # Path to save the file locally

# Download file from S3
try:
    s3.download_file(bucket_name, s3_key, local_file_path)
    print(f"File '{s3_key}' downloaded from S3 and saved as '{local_file_path}'")
except Exception as e:
    print(f"Error downloading file: {e}")
