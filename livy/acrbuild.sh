#!/bin/bash
CONTAINER_REGISTRY=xiaoyzhuacrdytmchfs
az acr build -t $CONTAINER_REGISTRY/livy:2.0 -r $CONTAINER_REGISTRY .