az acr login --name mulesoftpm
docker run -i -p 5000:5000 mulesoftpm.azurecr.io/fast-style-transfer
