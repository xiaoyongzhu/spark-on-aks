# From here: http://livy.incubator.apache.org/examples/

import time
import json
import pprint
import requests
import textwrap

host = 'http://20.252.45.68:8998'

data = {
    "className": "Spark_BLOB_Basic",
    "conf": {
        "spark.executor.instances": 2,
        "spark.eventLog.enabled": "false",
        # "spark.eventLog.dir" :"abfss://spark-event-logs@azurefeathrstorage.dfs.core.windows.net/logs",
        "spark.kubernetes.driver.volumes.hostPath.aksvm.mount.path": "/mnt",
        "spark.kubernetes.driver.volumes.hostPath.aksvm.options.path": "/tmp",
        "spark.kubernetes.namespace": "spark",
        "spark.kubernetes.authenticate.driver.serviceAccountName": "spark-sa",
        "spark.kubernetes.executor.podTemplateFile": "/opt/livy/work-dir/executor-pod-template.yaml",
        "spark.kubernetes.container.image": "xiaoyzhuacrdytmchfs.azurecr.io/spark:3.3.1",
        "spark.kubernetes.container.image.pullPolicy": "Always",
        "spark.kubernetes.file.upload.path": "file:///tmp",
        # "spark.jars.packages":"com.linkedin.feathr:feathr_2.12:0.9.0",
        "spark.hadoop.fs.azure.account.key.azurefeathrstorage.dfs.core.windows.net" : "<input key here>",
    },
    "file": "abfss://public@azurefeathrstorage.dfs.core.windows.net/test_data/spark-s3-sbt-basic.jar",
    "args": ["abfss://nytaxidata@<storageaccount>.dfs.core.windows.net/input", "abfss://nytaxidata@<storageaccount>.dfs.core.windows.net/output"]
}
headers = {'Content-Type': 'application/json'}

print("post sessions")
r = requests.post(host + '/batches', data=json.dumps(data), headers=headers)
print(r.json())

job_id = r.json()['id']
time.sleep(10)

r = requests.get(host + '/batches/' + str(job_id), headers=headers)
print(r.json())
