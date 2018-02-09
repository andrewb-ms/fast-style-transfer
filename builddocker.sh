git pull
az acr login --name mulesoftpm
docker build --no-cache . -t mulesoftpm.azurecr.io/fast-style-transfer:latest
docker push mulesoftpm.azurecr.io/fast-style-transfer
