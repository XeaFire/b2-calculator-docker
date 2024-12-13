# Build avec le Dockerfile :

**Run la commande suivante en vous situant dans le dossier où se situe le Dockerfile**


```bash
docker build . -t calc
```

## Pour le run pensez à partagez vos ports avec la commande suivante

```bash
docker run -p (port):(port) calc
```

## Pour choisir vos propres ports utilisez cette commande 

```bash
docker run -e CALC_PORT=10000 -p 10000:10000 calc
```


# Compose le Docker

**Run la commande suivante en vous situant dans le dossier où se situe le docker-compose**

```bash
docker compose up
```
