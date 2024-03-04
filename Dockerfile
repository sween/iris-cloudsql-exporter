FROM python:3.8

ADD src /src

RUN pip install prometheus_client
RUN pip install requests

WORKDIR /src


ENV PYTHONPATH '/src/'
ENV PYTHONUNBUFFERED=1

ENV IRIS_CLOUDSQL_USERPOOLID 'userpoolid'
ENV IRIS_CLOUDSQL_CLIENTID 'clientid'
ENV IRIS_CLOUDSQL_USER 'user'
ENV IRIS_CLOUDSQL_PASS 'pass'
ENV IRIS_CLOUDSQL_API 'api'
ENV IRIS_CLOUDSQL_DEPLOYMENTID 'deploymentid'

RUN pip install -r requirements.txt


CMD ["python" , "/src/iris_cloudsql_exporter.py"]