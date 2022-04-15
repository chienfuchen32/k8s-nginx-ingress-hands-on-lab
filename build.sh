# !/bin/bash
set -e
IMAGE=foo.com/k8s-nginx-ingress-lab:latest
docker build -t $IMAGE .
docker push $IMAGE
