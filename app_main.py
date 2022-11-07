import pathlib
from flask import Flask, render_template, request
from reportMonaco import report


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    return app


path_to_folder = pathlib.PosixPath(__file__).parent / 'tests' / 'test_reportMonaco' / 'data'
app = create_app()


@app.route('/report/')
@app.route('/')
def parent_route():
    reverse_mode = True if request.values.get('order') else False
    data = report.print_report(str(path_to_folder), html=True, reverse=reverse_mode)
    return render_template('index.html', content=data)


@app.route('/report/drivers/')
def drivers():
    data = report.get_drivers(str(path_to_folder))
    abbr = request.values.get('driver')
    reverse_mode = True if request.values.get('order') else False
    list_of_drivers = report.get_drivers(path_to_folder)

    if reverse_mode:
        data.reverse()

    if abbr:
        for _, driver, abbr_of_driver in list_of_drivers:
            if abbr == abbr_of_driver:
                name, car, result = report.find_driver(driver, path_to_folder)[0]
                content = f'{name}   {car}   {result}'
                return render_template('drivers.html', content=content)
    else:
        content = '<br><br>'.join(
            [f'{values[0]} {values[1]} <a href="/report/drivers/?driver={values[2]}">{values[2]}</a>'for values in data]
        )
        return render_template('drivers.html', content=content)


if __name__ == '__main__':  # pragma: no cover
    app.run(debug=True)
