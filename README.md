# Fil rouge de conteneurisation

Projet individuel de formation réalisé par Geoffrey Deverchere. L’objectif était de faire fonctionner une API FastAPI et deux bases de données dans des services Docker Compose, avec initialisation des données et contrôles de démarrage.

## Architecture

| Service | Rôle |
|---|---|
| `db_mongo` | Base MongoDB initialisée avec les publications d’exemple. |
| `db_mysql` | Base MySQL initialisée avec les utilisateurs d’exemple. |
| `admin_mongo` | Interface Mongo Express pour consulter MongoDB. |
| `admin_mysql` | Interface Adminer pour consulter MySQL. |
| `api` | API FastAPI qui expose `GET /posts` et `GET /users`. |

Le [fichier Compose](docker-compose.yml) orchestre ces services. Le code de l’API est dans `api/` et les scripts d’initialisation dans `mongo/` et `mysql/`.

## Démarrage en environnement de test

Ce montage est prévu pour une machine de test isolée. Le Compose publie plusieurs ports et Mongo Express n’a pas d’authentification HTTP. Éviter de le démarrer tel quel sur une machine accessible depuis le réseau.

Installer Docker avec Compose, puis copier [`.env.example`](.env.example) vers `.env` à la racine. Les valeurs d’exemple sont réservées à la démonstration locale. Depuis la racine du projet, lancer :

```sh
docker compose up -d --build
docker compose ps
```

## Vérifications du rendu

Avec les ports du fichier d’exemple, ouvrir les routes sur `localhost:8000` et vérifier l’état des cinq services. Les captures conservées dans le dépôt documentent le rendu de formation.

- [`GET /posts`](assets/screenshots/verification-api-posts.png) pour la lecture de MongoDB.
- [`GET /users`](assets/screenshots/verification-api-users.png) pour la lecture de MySQL.
- [État des services Compose](assets/screenshots/verification-stack-healthy.png).
