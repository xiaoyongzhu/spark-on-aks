# From here: http://livy.incubator.apache.org/examples/


import json, pprint, requests, textwrap

host = 'http://20.252.45.68:8998'

data= {
        # "name": "k8stestsession",
        "kind": "pyspark",
        # "numExecutors": 2,
        # "driverMemory": "4g",
        # "executorMemory": "20g",
        # "executorCores": 6,
        "conf": {
                "spark.executor.instances" : 2, 
                "spark.eventLog.enabled" : "true", 
                # "spark.eventLog.dir" :"abfss://spark-event-logs@<storageaccount>.dfs.core.windows.net/logs",  
                "spark.kubernetes.driver.volumes.hostPath.aksvm.mount.path" : "/mnt", 
                "spark.kubernetes.driver.volumes.hostPath.aksvm.options.path" : "/tmp",  
                "spark.kubernetes.namespace" : "spark",  
                "spark.kubernetes.authenticate.driver.serviceAccountName" : "spark-sa", 
                "spark.kubernetes.executor.podTemplateFile" : "/opt/livy/work-dir/executor-pod-template.yaml",
                "spark.kubernetes.container.image" : "xiaoyzhuacrdytmchfs.azurecr.io/spark:3.3.1",
                "spark.kubernetes.container.image.pullPolicy" :"Always",
                # "spark.hadoop.fs.azure.account.key.<storageaccount>.dfs.core.windows.net" : "<storage access key>"
        },
        # "file": "abfss://jars@<storageaccount>.dfs.core.windows.net/drop/nyctaxidata-1.0.jar",
        # "args": ["abfss://nytaxidata@<storageaccount>.dfs.core.windows.net/input", "abfss://nytaxidata@<storageaccount>.dfs.core.windows.net/output"]
        }
# data = {'kind': 'spark'}
headers = {'Content-Type': 'application/json'}

r = requests.get(host + '/sessions')
print(r.json())
# exit(0)

print("post sessions")

r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
print(r.json())

# {u'state': u'starting', u'id': 0, u'kind': u'spark'}

session_url = host + r.headers['location']
statements_url = session_url + '/statements'
r = requests.get(session_url, headers=headers)
print(r.json())






data = {
  'code': textwrap.dedent("""
    import random
    NUM_SAMPLES = 100000
    def sample(p):
      x, y = random.random(), random.random()
      return 1 if x*x + y*y < 1 else 0

    count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)
    print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)
    """)
}

# session_url = 'http://20.252.45.68:8998/sessions/0'

r = requests.post(statements_url, data=json.dumps(data), headers=headers)
pprint.pprint(r.json())