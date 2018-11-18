from flask import Flask
from config import Config
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

js = Bundle('jquery.js', 'base.js', 'widgets.js',
            filters='jsmin', output='gen/packed.js')
assets.register('js_all', js)
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
