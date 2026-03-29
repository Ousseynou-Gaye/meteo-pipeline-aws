# Pipeline météo automatisé pour l’agriculture (AgriTech)

## Description
Ce projet implémente un pipeline de données cloud automatisé sur AWS permettant de collecter, traiter et analyser des données météorologiques afin d’aider à la prise de décision dans le domaine agricole.

## Objectifs
- Optimiser l’irrigation des cultures
- Anticiper les conditions climatiques
- Améliorer la productivité agricole grâce aux données

## Architecture du système

Le pipeline fonctionne selon l’architecture suivante :

1. Collecte des données météo via l’API OpenWeatherMap
2. Stockage des données brutes dans Amazon S3
3. Traitement des données avec AWS Lambda
4. Enregistrement structuré dans Amazon DynamoDB
5. Automatisation des exécutions via Amazon EventBridge Scheduler
6. Surveillance et logs via Amazon CloudWatch

## Technologies utilisées

- AWS Lambda (traitement serverless)
- Amazon S3 (stockage des données)
- Amazon DynamoDB (base de données NoSQL)
- Amazon EventBridge Scheduler (automatisation)
- Amazon CloudWatch (monitoring)
- API OpenWeatherMap (source de données météo)
- Python (logique de traitement)

## Structure du projet

- `lambda-meteo-fonction` → collecte des données météo
- `lambda-meteo-traitement` → traitement des données
- `lambda-meteo-export` → export des données en CSV

## Sécurité

Les clés API sensibles sont stockées dans les variables d’environnement AWS Lambda afin de garantir la sécurité et éviter leur exposition dans le code source.


## Résultat

- Pipeline entièrement automatisé
- Traitement cloud sans serveur (serverless)
- Données exploitables pour l’agriculture
- Système scalable et modulaire


##  Auteur
Ousseynou Gaye - Alioune Badara Ba
