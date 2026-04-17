# Fil Rouge Docker Mongo MySQL FastAPI

Ce projet met en place une stack hybride orchestree avec Docker Compose.

L'objectif est de faire fonctionner ensemble :
- une base MongoDB personnalisee
- une base MySQL
- une interface Mongo Express
- une interface Adminer
- une API FastAPI qui lit MongoDB et MySQL

## Architecture

Les 5 services demarres par `docker-compose.yml` sont :
- `db_mongo`
- `db_mysql`
- `admin_mongo`
- `admin_mysql`
- `api`

L'API expose deux routes de verification :
- `GET /posts` : lit les donnees MongoDB
- `GET /users` : lit les donnees MySQL

## Lancer le projet

Depuis la racine du depot :

```bash
docker compose up -d --build
```

Puis verifier l'etat des services :

```bash
docker compose ps
```

## Verifications attendues

Le rendu demande doit prouver :
- que les 5 services sont bien demarres et en statut `healthy`
- que `GET /posts` fonctionne
- que `GET /users` fonctionne

## Captures d'ecran

Les captures de verification sont rangees dans [assets/screenshots].

Noms retenus :
- `verification-api-posts.png` : preuve du succes de `http://localhost:8000/posts`
- `verification-api-users.png` : preuve du succes de `http://localhost:8000/users`
- `verification-stack-healthy.png` : capture attendue de `docker compose ps` avec les 5 services en `healthy`

## Arborescence utile

```text
.
|-- api/
|-- mongo/
|-- mysql/
|-- assets/
|   `-- screenshots/
|-- docker-compose.yml
|-- .env.example
|-- .gitignore
`-- rendu.txt
```

## Contenu technique

- `api/` contient l'application FastAPI et son Dockerfile
- `mongo/` contient l'image Mongo personnalisee et son script d'initialisation
- `mysql/` contient le script SQL d'initialisation
- `docker-compose.yml` orchestre l'ensemble

## Auteur

Projet realise par Geoffrey DEVERCHERE dans le cadre d'un exercice de conteneurisation autour de Docker Compose, MongoDB, MySQL et FastAPI.

Ce depot presente mon travail personnel, de la conception de la stack a la mise en place des services, des scripts d'initialisation, des healthchecks et des verifications de fonctionnement.
