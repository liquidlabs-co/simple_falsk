from flask import Flask, render_template
import redis
app = Flask(__name__)

@app.route("/")
def main():
   redis_client = redis.StrictRedis.from_url('redis://redis:6379')
   new_image = redis_client.get('new_image')
   return render_template('index.html', new_image = new_image.decode('utf-8'))

if __name__== "__main__":
    app.run('0.0.0.0')
