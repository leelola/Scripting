import sys
import boto3

try:
    def main():
        create_s3bucket(jane)

except Exception as e:
    print(e)

def create_s3bucket(jane):
    s3_bucket=boto3.client(
        's3',
    )

    bucket = s3_bucket.create_bucket(
        Bucket=jane,
        ACL='private',
        CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
    )

    print(bucket)

jane = sys.argv[1]

if __name__ == '__main__':
    main()
    