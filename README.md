## install dependency
```bash
$ pip3 install -U -r requirements.txt
```
## run program
```bash
$ source .env
$ python3 app.py
```
## build and push docker image
```bash
$ bash build.sh
```
## deploy
```bash
$ kubectl apply -f k8s/deloyment.yaml
$ kubectl apply -f k8s/service.yaml
$ kubectl apply -f k8s/ingress.yaml
```
