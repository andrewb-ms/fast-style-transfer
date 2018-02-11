git pull
cp /msshared . -r
docker rmi mulesoftpm.azurecr.io/fast-style-transfer
az acr login --name mulesoftpm
docker build --no-cache . -t mulesoftpm.azurecr.io/fast-style-transfer
docker push mulesoftpm.azurecr.io/fast-style-transfer
