from flask import Flask
from views import simple_page


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        instance_relative_config=True
    )
    return app


app = create_app()
app.register_blueprint(simple_page)


if __name__ == '__main__':  # pragma: no cover
    app.run(debug=True)
