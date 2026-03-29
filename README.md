#  Pipeline météo automatisé (AgriTech)

##  Description
Ce projet est un pipeline de données AWS serverless qui collecte, traite et stocke des données météo pour l’aide à la décision agricole.

##  Objectif
Fournir des données météo fiables pour :
- Optimiser l’irrigation
- Anticiper les conditions climatiques
- Améliorer la productivité agricole

## Technologies utilisées
- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon EventBridge
- Amazon CloudWatch
- API OpenWeatherMap

##  Architecture du système

1. Collecte des données météo via API
2. Stockage des données brutes dans S3
3. Traitement des données via Lambda
4. Sauvegarde structurée dans DynamoDB
5. Automatisation avec EventBridge
6. Monitoring avec CloudWatch

## Structure du projet

- lambda-meteo-fonction → collecte des données météo
- lambda-meteo-traitement → traitement des données
- lambda-meteo-export → export des données

## Auteur
Ousseynou Gaye - Alioune Badara Ba
