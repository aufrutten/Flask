import pathlib
from flask import Flask, render_template, request
from reportMonaco import report


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        instance_relative_config=True
    )
    app.config['path_to_folder'] = str(pathlib.PosixPath(__file__).parent / 'tests' / 'test_reportMonaco' / 'data')
    return app


app = create_app()


@app.route('/report/')
@app.route('/')
def parent_route():
    reverse_mode = True if request.values.get('order') else False
    data = report.print_report(app.config.get('path_to_folder'), html=True, reverse=reverse_mode)
    return render_template('index.html', content=enumerate(data))


@app.route('/report/drivers/')
def drivers():
    list_with_results = report.get_drivers(app.config.get('path_to_folder'))
    data = report.build_report(app.config.get('path_to_folder'))[0]

    abbr = request.values.get('driver')
    reverse_mode = True if request.values.get('order') else False

    if reverse_mode:
        list_with_results.reverse()

    if abbr:
        content = report.find_driver(data[abbr]['name'], app.config.get('path_to_folder'))[0]
        return render_template('drivers.html', driver=content)
    else:
        return render_template('drivers.html', drivers=list_with_results)


if __name__ == '__main__':  # pragma: no cover
    app.run(debug=True)
