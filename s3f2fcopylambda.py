#####This code will copy from a desired folder in S3 to desired folder in another S3 through Lambda
##send an sample event, you can run it as a cron
##bhanu.rhce@gmail.com

import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('your sourcebucket')
dest_bucket = s3.Bucket('your destination bucket')


def lambda_handler(event, context):
    print(bucket)
    print(dest_bucket)

    for obj in bucket.objects.filter(Prefix='field/'):
        #print(obj)
        dest_key = 'sftpsync/'+obj.key
        print(dest_key)
        s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {'Bucket': obj.bucket_name, 'Key': obj.key})
         ### add something if you want to print more logs something like:  #print(Files copied to 'dest_bucket')

