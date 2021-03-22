import sys
import boto3
try:
    def main():
        create_s3bucket('lee')
except Exception as eT:
    print(eT)

def create_s3bucket(lee):
    s3_bucket=boto3.resource(
        's3',
    )
    #CREATE output BUCKET TO CRAETE A NEW S3
    s3_bucket.create_bucket(
        Bucket='lee')
    s3_bucket.create_bucket(
        Bucket='lee',     
        CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
    )
    
    #print(s3_bucket)
    lee = sys.argv[1]

if __name__ =='__main__' :
    main()
        