import pytest
from app_main import app


def test_main_glory_hole():
    response = app.test_client().get('/report/')
    assert response.status_code == 200


class TestRouteDrivers:

    def test_route_drivers(self):
        response = app.test_client().get('/report/drivers/')
        assert response.status_code == 200

    def test_with_reverse_mode(self):
        response = app.test_client().get('/report/drivers/?order=desc')
        assert response.status_code == 200

    def test_with_abbr(self):
        response = app.test_client().get('/report/drivers/?driver=NHR')
        assert response.status_code == 200

