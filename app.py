from flask import Flask
from rediscluster import StrictRedisCluster

app = Flask(__name__)
startup_nodes = [{"host": "cache-cluster.j130cz.clustercfg.use1.cache.amazonaws.com", "port": "6379"}]
db = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)

@app.route('/')
def hello_world():
    name = db.get("Name")
    if (name != None):
        return 'Hello my dear %s' %name
    else:
        return 'Key not ready'

@app.route('/listnames')
def list():
    nameslen = db.llen("names")
    message = ''
    if (nameslen > 0):
        #for i in range(0, nameslen):
        for i in reversed(range(0, nameslen)):
            name = db.lindex('names', i)
            message = message + "%s \n" %name
        return message
    else:
        return 'No names in the system'

@app.route('/addname/<name>')
def setname(name):
    db.lpush("names", name.encode('utf-8'))
    return 'Name added'

@app.route('/delname')
def delname():
    db.delete('Name')
    return 'Name deleted'

if __name__ == '__main__':
  app.run()
