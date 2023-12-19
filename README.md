# Projet NoSQL

## Description

L'objectif de ce projet est d'apprendre à utiliser Docker et son système de containers.  
Ici, on crée 2 containers dédiés à la base de données de notre projet. Un utilise la technologie PostgreSQL, l'autre utilise MongoDB.  
L'application web est en Django.  
  
Le but de l'application web est de faire une recherche d'image de chiens via l'API implémenté appelé "DogAPI", selon une race spécifique de chien.  
L'utilisateur pourra ensuite enregistrer l'image dans les bases de données.

## Accéder aux containers BDD

### PostgreSQL :

```bash
- docker exec -it postgres bash
- psql -U myuser -d mydb
```

### MongoDB :

```bash
- docker exec -it mongodb bash
- mongo -u admin -p mypassword
- use mydb
```

## Auteurs

Ce projet est réalisé par :
- Laurent NGETH
- Steeven NOVO