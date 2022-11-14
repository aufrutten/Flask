from flask import Blueprint, render_template, request
from reportMonaco import report
import pathlib

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates',
                        )

path_to_folder = str(pathlib.PosixPath(__file__).parent / 'tests' / 'test_reportMonaco' / 'data')


@simple_page.route('/report/')
@simple_page.route('/')
def parent_route():
    reverse_mode = True if request.values.get('order') else False
    data = report.print_report(path_to_folder, html=True, reverse=reverse_mode)
    return render_template('index.html', content=enumerate(data))


@simple_page.route('/report/drivers/')
def drivers():
    list_with_results = report.get_drivers(path_to_folder)
    data = report.build_report(path_to_folder)[0]

    abbr = request.values.get('driver')
    reverse_mode = True if request.values.get('order') else False

    if reverse_mode:
        list_with_results.reverse()

    if abbr:
        content = report.find_driver(data[abbr]['name'], path_to_folder)[0]
        return render_template('drivers.html', driver=content)
    else:
        return render_template('drivers.html', drivers=list_with_results)

