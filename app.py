import redis
from flask import Flask

app = Flask(__name__)
db = redis.Redis(host='server', port=6379, db=0)

@app.route('/')
def hello_world():
    name = db.get('Name').decode('utf-8')
    return 'Hello my dear %s' % name

@app.route('/setname/<name>')
def setname(name):
    db.set('Name', name.encode('utf-8'))
    return 'Name updated'

if __name__ == '__main__':
  app.run()
