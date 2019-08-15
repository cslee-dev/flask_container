import importlib

from flask import Flask
from flask_restful import Api
from settings import configs, database

app = Flask(__name__)
app.config.from_object(configs.config)

api = Api(app)

urls = importlib.import_module(configs.ROOT_URL)


for res, url in urls.urlpatterns:
    if urls.prefix_url is not None:
        url = urls.prefix_url + url
    api.add_resource(res, url)

if __name__ == "__main__":
    app.run('localhost', 1472)
