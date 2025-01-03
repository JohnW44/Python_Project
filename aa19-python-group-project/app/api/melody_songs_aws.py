import boto3
import os
from dotenv import load_dotenv
import uuid

ALLOWED_EXTENSIONS = {"mp3", "wav", "ogg"}

def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"

def upload_file_to_s3(file, acl="public-read"):
    load_dotenv()
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("S3_KEY"),
        aws_secret_access_key=os.environ.get("S3_SECRET")
    )
    
    bucket_name = os.environ.get("S3_BUCKET")
    
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
        
        return {"url": f"https://{bucket_name}.s3.amazonaws.com/{file.filename}"}
    except Exception as e:
        return {"errors": str(e)}

def test_aws_connection():
    # Load environment variables
    load_dotenv()
    
    # Print environment variables (without the secret)
    print("Testing with:")
    print(f"Bucket: {os.environ.get('S3_BUCKET')}")
    print(f"Key: {os.environ.get('S3_KEY')}")
    print("Secret: [hidden]")
    
    try:
        # Create S3 client
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.environ.get("S3_KEY"),
            aws_secret_access_key=os.environ.get("S3_SECRET")
        )
        
        # Try to list objects in your specific bucket
        bucket_name = os.environ.get("S3_BUCKET")
        print(f"\nTrying to list objects in {bucket_name}:")
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents'][:5]:  # Show first 5 objects
                print(f"- {obj['Key']}")
        else:
            print("Bucket is empty")
            
    except Exception as e:
        print("\nError occurred:")
        print(str(e))

if __name__ == "__main__":
    test_aws_connection()