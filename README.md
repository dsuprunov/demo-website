```bash
docker login dhi.io

docker compose up --build

docker build -t dsuprunov/demo-portal:latest . --no-cache

docker push dsuprunov/demo-portal:latest
```

```bash
helm template demo-portal ./helm/ --namespace demo-portal

helm upgrade --install demo-portal ./helm/ --namespace demo-portal --create-namespace

kubectl -n demo-portal get pods -o wide

kubectl -n demo-portal get services
```

