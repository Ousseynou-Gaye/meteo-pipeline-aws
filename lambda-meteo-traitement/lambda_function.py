import json
import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('meteo-table')

def lambda_handler(event, context):

    print("===== EVENT RECU =====")
    print(json.dumps(event))

    try:
        print("START TRAITEMENT")

        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        print(f"Fichier reçu : {key}")

        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        data = json.loads(content)

        print("Données lues :", data)

        table.put_item(
            Item={
                'ville': data['ville'],
                'temperature': str(data['temperature'])
            }
        )

        print("INSERTION OK DYNAMODB")

    except Exception as e:
        print("ERREUR :", str(e))

    return {
        'statusCode': 200
    }
