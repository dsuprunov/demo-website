```bash
docker login dhi.io

docker compose up --build

docker build -t dsuprunov/demo-website:latest . --no-cache

docker push dsuprunov/demo-website:latest
```

```bash
helm template demo-website ./helm/ --namespace demo-website

helm upgrade --install demo-website ./helm/ --namespace demo-website --create-namespace

kubectl -n demo-website get pods -o wide

kubectl -n demo-website get services
```

