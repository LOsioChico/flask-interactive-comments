from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    # Default config
    app.debug = True

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
