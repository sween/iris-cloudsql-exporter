docker build -t iris-cloudsql-exporter .
docker image tag iris-cloudsql-exporter sween/iris-cloudsql-exporter:latest
docker push sween/iris-cloudsql-exporter:latest