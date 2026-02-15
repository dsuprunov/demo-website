```bash
docker compose up --build

docker build -t dsuprunov/dummy-portal:latest . --no-cache

docker push dsuprunov/dummy-portal:latest

helm template dummy-portal services/dummy-portal/helm/ --namespace dummy-portal

helm upgrade --install dummy-portal services/dummy-portal/helm/ --namespace dummy-portal --create-namespace

kubectl get nodes -o wide

kubectl get services -n dummy-portal
```
