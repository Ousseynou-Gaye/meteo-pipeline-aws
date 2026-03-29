import boto3
import csv
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

TABLE_NAME = "meteo-table"
BUCKET_NAME = "meteo-pipeline-ouz-badara"

def lambda_handler(event, context):

    table = dynamodb.Table(TABLE_NAME)

    response = table.scan()
    items = response['Items']

    file_name = f"/tmp/rapport_meteo_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

    headers = ["ville", "temperature", "humidite", "pression", "vent_vitesse", "timestamp"]

    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for item in items:
            writer.writerow({
                "ville": item.get("ville"),
                "temperature": item.get("temperature"),
                "humidite": item.get("humidite"),
                "pression": item.get("pression"),
                "vent_vitesse": item.get("vent_vitesse"),
                "timestamp": item.get("timestamp")
            })

    s3.upload_file(file_name, BUCKET_NAME, "reports/rapport_meteo.csv")

    return {
        "status": "OK",
        "message": "Rapport généré avec succès"
    }
