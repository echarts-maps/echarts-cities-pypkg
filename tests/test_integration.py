# coding=utf8
from __future__ import unicode_literals
from nose.tools import assert_dict_equal, eq_

from pyecharts.datasets.coordinates import (
    get_coordinate,
    search_coordinates_by_country_and_keyword,
    search_coordinates_by_filter,
)


def test_get_coordinate():
    coordinate = get_coordinate("Oxford", "GB")
    eq_([-1.25596, 51.75222], coordinate)


def test_get_coordinate_without_data():
    coordinate = get_coordinate("Alien City", "Glaxy")
    assert coordinate is None


def test_search_coordinates_by_country():
    # search the city name containing '北京'
    result = search_coordinates_by_country_and_keyword("GB", "London")
    expected = {
        "Londonderry County Borough": [-7.30917, 54.99721],
        "City of London": [-0.09184, 51.51279],
        "London": [-0.12574, 51.50853],
    }
    eq_(result, expected)


def test_advance_search_coordinates():
    result = search_coordinates_by_filter(
        func=lambda name: "Central" in name or "Hong Kong" in name,
        country="HK",
    )
    expected = {
        "Hong Kong": [114.15769, 22.28552],
        "Central": [114.15846, 22.28299],
    }
    eq_(result, expected)
    result2 = search_coordinates_by_country_and_keyword(
        "HK", "Central", "Hong Kong"
    )
    assert_dict_equal(result, result2)
