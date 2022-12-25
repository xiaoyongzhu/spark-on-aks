#!/bin/bash
CONTAINER_REGISTRY="xiaoyzhuacrdytmchfs.azurecr.io"
az acr build -t $CONTAINER_REGISTRY/spark:3.3.1 -r $CONTAINER_REGISTRY .