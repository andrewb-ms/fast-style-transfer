az acr login --name mulesoftpm.azurecr.io/fast-style-transfer
docker build --no-cache . -t mulesoftpm.azurecr.io/fast-style-transfer
docker push mulesoftpm.azurecr.io/fast-style-transfer
