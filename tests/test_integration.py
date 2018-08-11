# coding=utf8
from __future__ import unicode_literals
from nose.tools import assert_dict_equal, eq_, raises

from pyecharts.exceptions import RegionNotFound

from pyecharts.datasets.coordinates import (
    get_coordinate,
    search_coordinates_by_region_and_keyword,
    search_coordinates_by_filter,
)


def test_get_coordinate():
    do_get_coordinate("GB")


def test_get_coordinate_in_chinese():
    do_get_coordinate("英国")


@raises(RegionNotFound)
def test_get_coordinate_from_unknown_region():
    get_coordinate("Alien City", "Glaxy")


def test_search_coordinates_by_region():
    do_search_coordinates_by_region("GB")


def test_search_coordinates_by_region_in_chinese():
    # search the city name containing '北京'
    do_search_coordinates_by_region("英国")


def test_advance_search_coordinates():
    do_advance_search_coordinates("HK")


def test_advance_search_coordinates_in_chinese():
    do_advance_search_coordinates("中国香港")


def do_get_coordinate(region):
    coordinate = get_coordinate("Oxford", region)
    eq_([-1.25596, 51.75222], coordinate)


def do_search_coordinates_by_region(region):
    result = search_coordinates_by_region_and_keyword(region, "London")
    expected = {
        "Londonderry County Borough": [-7.30917, 54.99721],
        "City of London": [-0.09184, 51.51279],
        "London": [-0.12574, 51.50853],
    }
    eq_(result, expected)


def do_advance_search_coordinates(region):
    result = search_coordinates_by_filter(
        func=lambda name: "Central" in name or "Hong Kong" in name,
        region=region,
    )
    expected = {
        "Hong Kong": [114.15769, 22.28552],
        "Central": [114.15846, 22.28299],
    }
    eq_(result, expected)
    result2 = search_coordinates_by_region_and_keyword(
        region, "Central", "Hong Kong"
    )
    assert_dict_equal(result, result2)
