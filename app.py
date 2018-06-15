from flask import Flask
from rediscluster import StrictRedisCluster

app = Flask(__name__)
startup_nodes = [{"host": "cluster.clustercfg.use1.cache.amazonaws.com", "port": "6379"}]
db = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)

@app.route('/')
def hello_world():
    name = db.get("Name")
    if (name != None):
        return 'Hello my dear %s' %name
    else:
        return 'Key not ready'

@app.route('/setname/<name>')
def setname(name):
    db.set('Name', name.encode('utf-8'))
    return 'Name updated'

if __name__ == '__main__':
  app.run()
