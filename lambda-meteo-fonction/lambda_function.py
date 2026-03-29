import json
import os
import urllib.request
import boto3
import time
from datetime import datetime

# ===== AWS CLIENTS =====
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('meteo-table')


# ===== UTILS =====
def safe_get(value, default=0):
    return value if value is not None else default


# ===== LAMBDA =====
def lambda_handler(event, context):

    api_key = os.environ["OPENWEATHER_API_KEY"]
    bucket_name = "meteo-pipeline-ouz-badara"

    cities = ["Dakar", "Thies", "Saint-Louis", "Bamako", "Abidjan", "Ouagadougou"]

    results = []

    # ===== DATE STRUCTURE =====
    now = datetime.utcnow()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    date = now.strftime("%Y-%m-%d")

    for city in cities:
        try:
            print(f"START traitement {city}")

            # ===== API URL =====
            city_encoded = city.replace(" ", "%20")
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={api_key}&units=metric"

            # ===== CALL API =====
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())

            # ===== SAFE EXTRACTION =====
            temperature = round(safe_get(data["main"]["temp"]), 1)
            ressenti = round(safe_get(data["main"]["feels_like"]), 1)
            humidite = safe_get(data["main"]["humidity"])
            pression = safe_get(data["main"]["pressure"])

            # ===== STRUCTURE PROPRE =====
            result = {
                # ANTI-DOUBLON
                "cle": f"{city}_{date}",

                "ville": data["name"],
                "temperature": temperature,
                "ressenti": ressenti,
                "humidite": humidite,
                "pression": pression,

                #  METRICS SUPPLEMENTAIRES
                "vent_vitesse": safe_get(data["wind"]["speed"]),
                "latitude": safe_get(data["coord"]["lat"]),
                "longitude": safe_get(data["coord"]["lon"]),

                "description": data["weather"][0]["description"],
                "timestamp": datetime.utcnow().isoformat()
            }

            results.append(result)

            # ===== S3 SAVE =====
            file_name = f"raw/{year}/{month}/{day}/{city}/data.json"

            s3.put_object(
                Bucket=bucket_name,
                Key=file_name,
                Body=json.dumps(result)
            )

            # ===== DYNAMODB SAVE =====
            table.put_item(Item=result)

            print(f"OK {city}")

            # ===== ANTI RATE LIMIT =====
            time.sleep(1)

        except urllib.error.HTTPError as e:
            print(f"HTTP Error {city}: {e}")
            continue

        except Exception as e:
            print(f"Erreur {city}: {e}")
            continue

    print("END TRAITEMENT GLOBAL")

    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }
