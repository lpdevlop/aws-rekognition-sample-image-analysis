import boto3

#app = Flask(__name__)
rekognition_client = boto3.client('rekognition',
                                  aws_secret_access_key='kkkkkkkkkkkkkkkkkkkkkkkkkkkkk',
                                  aws_access_key_id='bbbbbbbbbbbbbbbbbbbbbbbbbbb',
                                  region_name='us-east-1')

image_path = "man.jpg"

with open(image_path, "rb") as image_file:
    image_bytes = image_file.read()

response = rekognition_client.detect_labels(
    Image={'Bytes': image_bytes},
    MaxLabels=10,
    MinConfidence=80
)

print("Detected labels:")
for label in response['Labels']:
    print(f"- {label['Name']} (Confidence: {label['Confidence']:.2f}%)")