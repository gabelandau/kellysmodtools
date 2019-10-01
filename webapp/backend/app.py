from flask import Flask, jsonify, render_template
from flask_cors import CORS

DEBUG = True

app = Flask(__name__, static_folder = "../dist/static", template_folder = "../dist/templates")

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index():
  return render_template("index.html")

if __name__ == '__main__':
  app.run()