import time
import os
import requests
import json

from warrant import Cognito
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
from prometheus_client.parser import text_string_to_metric_families

class IRISCloudSQLExporter(object):
    def __init__(self):

        self.access_token = self.get_access_token()
        self.portal_api = os.environ['IRIS_CLOUDSQL_API']
        self.portal_deploymentid = os.environ['IRIS_CLOUDSQL_DEPLOYMENTID']

    def collect(self):

        # Requests fodder
        url = self.portal_api
        deploymentid = self.portal_deploymentid

        headers = {
            'Authorization': self.access_token, # needs to be refresh_token, eventually
            'Content-Type': 'application/json'
        }

        metrics_response = requests.request("GET", url + '/metrics/' + deploymentid, headers=headers)
        metrics = metrics_response.content.decode("utf-8")

        for iris_metrics in text_string_to_metric_families(metrics):
            for sample in iris_metrics.samples:

                labels_string = "{1}".format(*sample).replace('\'',"\"")
                labels_dict = json.loads(labels_string)
                labels = []

                for d in labels_dict:
                    labels.extend(labels_dict)
                if len(labels) > 0:
                    g = GaugeMetricFamily("{0}".format(*sample), 'Help text', labels=labels)
                    g.add_metric(list(labels_dict.values()), "{2}".format(*sample))
                else:
                    g = GaugeMetricFamily("{0}".format(*sample), 'Help text', labels=labels)
                    g.add_metric([""], "{2}".format(*sample))
                yield g

    def get_access_token(self):
        
        try:
            user_pool_id = os.environ['IRIS_CLOUDSQL_USERPOOLID'] # isc iss 
            username = os.environ['IRIS_CLOUDSQL_USER']
            password = os.environ['IRIS_CLOUDSQL_PASS']
            clientid = os.environ['IRIS_CLOUDSQL_CLIENTID'] # isc aud 
            
            try:
                u = Cognito(
                    user_pool_id=user_pool_id,
                    client_id=clientid,
                    user_pool_region="us-east-2", # needed by warrant, should be derived from poolid doh
                    username=username
                )
                u.authenticate(password=password)
            except Exception as p:
                print(p)
        except Exception as e:
            print(e)

        return u.id_token
    
if __name__ == '__main__':

    start_http_server(8000)
    REGISTRY.register(IRISCloudSQLExporter())
    while True:
        REGISTRY.collect()
        print("Polling IRIS CloudSQL API for metrics data....")
        #looped e loop
        time.sleep(30)