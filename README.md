```bash
docker compose up --build

docker build -t dsuprunov/dummy-portal:latest . --no-cache

docker push dsuprunov/dummy-portal:latest

helm template dummy-portal ./helm/ --namespace dummy-portal

helm upgrade --install dummy-portal ./helm/ --namespace dummy-portal --create-namespace

kubectl -n dummy-portal get pods -o wide

kubectl -n dummy-portal get services
```

