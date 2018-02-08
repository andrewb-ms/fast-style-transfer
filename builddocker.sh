az acr login --name mulesoftpm.azurecr.io
docker build --no-cache . -t mulesoftpm.azurecr.io/fast-style-transfer
docker push mulesoftpm.azurecr.io/fast-style-transfer
