# InterSystems IRIS CloudSQL Exporter
Export your CloudSQL Deployments to Google Cloud Operations

<img src="https://github.com/sween/iris-cloudsql-exporter/raw/main/assets/rivian-nats.png" alt="CloudSQL Exporter">


## Setup
Create a namespace

```
kubectl create ns iris
```

Create a configmap of the otel configuration

```
kubectl -n iris create configmap otel-config --from-file collector_config.yaml
```



## References
https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-otel#explicit-credentials



## Author
Ron Sweeney [sween](https://www.github.com/sween)

