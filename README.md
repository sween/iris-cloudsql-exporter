# InterSystems IRIS CloudSQL Exporter
Export your Saas CloudSQL Deployments to Google Cloud Operations

<img src="https://github.com/sween/iris-cloudsql-exporter/raw/main/assets/iris-cloudsql.png" alt="InterSystems CloudSQL Exporter">

## Container Build

```
docker build -t iris-cloudsql-exporter .
docker image tag iris-cloudsql-exporter sween/iris-cloudsql-exporter:latest
docker push sween/iris-cloudsql-exporter:latest

```

## Kubernetes Setup
Create a namespace

```
kubectl create ns iris
```

Create a configmap of the otel configuration

```
kubectl -n iris create configmap otel-config --from-file collector_config.yaml
```

Secrets - InterSystems Cloud Portal Stuff

```
kubectl create secret generic iris-cloudsql -n iris \
    --from-literal=user='sween' \
    --from-literal=password='12345' \ # same as your luggage
    --from-literal=clientid='' \ # from jwt
    --from-literal=userpoolid=''
```

Secrets - Google Cloud Stuff

```
kubectl -n iris create secret generic gmp-test-sa \
  --from-file=key.json=gmp-test-sa-key.json
```


## References
https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-otel#explicit-credentials


## Author
Ron Sweeney [sween](https://www.github.com/sween)

