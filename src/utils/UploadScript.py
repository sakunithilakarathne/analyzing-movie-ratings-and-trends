
import boto3

from pathlib import Path
from botocore.exceptions import NoCredentialsError




access_key = "AKIAXHND3CRPCBHL2V4A"
secret_key = "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"
region = 'ap-southeast-1'


bucket_name='datascienceproject02'
s3_path='datasets/preprocessed_movie_data.csv'

data_file_path='/home/ec2-user/datasets'
data_file_name="preprocessed_movie_data.csv"

data_file_path = Path(data_file_path)
data_file_full_path = data_file_path / data_file_name

s3 = boto3.client('s3',aws_access_key_id=access_key,
                  aws_secret_access_key = secret_key,
                  region_name =region
)  


#s3 upload
try:
    s3.upload_file(data_file_full_path,bucket_name,s3_path)
    print(f'file {data_file_full_path} is uploaded to s3 {s3_path}')

except NoCredentialsError:  
    print('AWS credentials not found') 

except FileNotFoundError:   
     print('File not found {data_file_path}') 

                            