```bash
docker login

docker compose up --build

docker build -t dsuprunov/demo-website:1.0.1 . --no-cache

docker push dsuprunov/demo-website:1.0.1
```

```bash
helm lint ./charts/demo-website-chart

helm template demo-website ./charts/demo-website-chart --namespace demo-website

mkdir -p dist

helm package ./charts/demo-website-chart --version 0.1.1 --app-version 1.0.1 --destination dist

helm registry login registry-1.docker.io -u dsuprunov

helm push dist/demo-website-chart-0.1.1.tgz oci://registry-1.docker.io/dsuprunov
```

```bash
helm upgrade --install demo-website oci://registry-1.docker.io/dsuprunov/demo-website-chart --version 0.1.1 --namespace demo-website --create-namespace

kubectl -n demo-website get pods -o wide

kubectl -n demo-website get services
```
