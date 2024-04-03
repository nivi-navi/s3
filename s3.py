import boto3
client=boto3.client('s3')
def listbucket():
    response=client.list_buckets()
    print(response['Buckets'])
    return response
def createbucket():
    response=client.create_bucket(Bucket='devops-starbucks',CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})
    print(response)
    return response
def uploadfile():
    filename="C:/Users/USER/Desktop/linux-command-import.pdf"
    response=client.upload_file(filename,'devops-starbucks',"index.pdf")
    print(response)
def listobject():
    response = client.list_objects(Bucket='devops-starbucks')
    # print(response)
    contents = response.get('Contents')

    if contents:
        for content  in contents:
            print(content['Key'])
    else:
        print("File not found in the bucket.")
listobject()
# uploadfile()
# createbucket()