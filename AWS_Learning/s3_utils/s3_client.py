import boto3
from botocore.exceptions import BotoCoreError, ClientError
from decouple import config

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'ap-south-1'
s3_file_path='project/files/'

class S3Client:
    def __init__(self,):
        self.bucket_name = AWS_STORAGE_BUCKET_NAME
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME
        )

    def upload_file(self, file_path, s3_key):
        try:
            self.s3.upload_file(Filename=file_path, Bucket=self.bucket_name, Key=s3_key)
            return f"Uploaded: {s3_key}"
        except (BotoCoreError, ClientError) as e:
            return f"Upload failed: {str(e)}"

    def upload_fileobj(self, file_obj, s3_key):
        try:
            self.s3.upload_fileobj(Fileobj=file_obj, Bucket=self.bucket_name, 
                                   Key=s3_key,ExtraArgs={'ACL': 'public-read'})
            return f"Uploaded from fileobj: {s3_key}"
        except (BotoCoreError, ClientError) as e:
            return f"Upload failed: {str(e)}"
        
    def list_files(self, prefix=""):
        try:
            response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
            return [item['Key'] for item in response.get('Contents', [])]
        except (BotoCoreError, ClientError) as e:
            return f"List failed: {str(e)}"

    def delete_file(self, s3_key):
        try:
            self.s3.delete_object(Bucket=self.bucket_name, Key=s3_key)
            return f"Deleted: {s3_key}"
        except (BotoCoreError, ClientError) as e:
            return f"Delete failed: {str(e)}"

    def list_image_urls(self, prefix="images/"):
        try:
            response = self.s3.list_objects_v2(Bucket=AWS_STORAGE_BUCKET_NAME, Prefix=prefix)
            urls = []

            for obj in response.get("Contents", []):
                key = obj["Key"]
                if key.endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
                    url = self.s3.generate_presigned_url(
                        'get_object',
                        Params={'Bucket': AWS_STORAGE_BUCKET_NAME, 'Key': key},
                        ExpiresIn=3600  # 1 hour
                    )
                    urls.append(url)
            return urls
        except Exception as e:
            return []
