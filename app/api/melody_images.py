import boto3
import os
from dotenv import load_dotenv
import uuid

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"

def upload_file_to_s3(file, acl="public-read"):
    load_dotenv()

    print("\n=== S3 Image Upload Debug ===")
    print(f"1. File info:")
    print(f"   - Filename: {file.filename}")
    print(f"   - Content Type: {file.content_type}")
    
    print("\n2. AWS Configuration:")
    print(f"   - Images Bucket: {os.environ.get('S3_IMAGES_BUCKET')}")
    
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("S3_KEY"),
        aws_secret_access_key=os.environ.get("S3_SECRET")
    )
    
    bucket_name = os.environ.get("S3_IMAGES_BUCKET")  # Use the images bucket
    
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
        
        url = f"https://{bucket_name}.s3.amazonaws.com/{file.filename}"
        print(f"\n4. Upload successful!")
        print(f"   URL: {url}")
        return {"url": url}
    except Exception as e:
        print(f"\nError during upload:")
        print(f"Exception: {str(e)}")
        return {"errors": str(e)}

def remove_file_from_s3(image_url):
    load_dotenv()
    
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("S3_KEY"),
        aws_secret_access_key=os.environ.get("S3_SECRET")
    )
    
    try:
        # Extract key from URL
        key = image_url.split('.amazonaws.com/')[1]
        
        s3.delete_object(
            Bucket=os.environ.get("S3_IMAGES_BUCKET"),  # Use the images bucket
            Key=key
        )
        return True
    except Exception as e:
        print(f"Error removing file: {str(e)}")
        return {"errors": str(e)}

def test_images_connection():
    """Test the connection to the images bucket"""
    load_dotenv()
    
    print("Testing Images Bucket Connection:")
    print(f"Bucket: {os.environ.get('S3_IMAGES_BUCKET')}")
    print(f"Key exists: {bool(os.environ.get('S3_KEY'))}")
    
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.environ.get("S3_KEY"),
            aws_secret_access_key=os.environ.get("S3_SECRET")
        )
        
        bucket_name = os.environ.get("S3_IMAGES_BUCKET")
        objects = s3.list_objects_v2(Bucket=bucket_name)
        
        print("\nConnection successful!")
        if 'Contents' in objects:
            print("First 5 images in bucket:")
            for obj in objects['Contents'][:5]:
                print(f"- {obj['Key']}")
        else:
            print("Bucket is empty")
            
    except Exception as e:
        print(f"\nError occurred: {str(e)}")

if __name__ == "__main__":
    test_images_connection()