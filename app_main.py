from flask import Flask
from views import simple_page
import pathlib


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        instance_relative_config=True
    )
    app.config['path_to_folder'] = str(pathlib.PosixPath(__file__).parent / 'tests' / 'test_reportMonaco' / 'data')
    return app


app = create_app()
app.register_blueprint(simple_page)


if __name__ == '__main__':  # pragma: no cover
    app.run(debug=True)
