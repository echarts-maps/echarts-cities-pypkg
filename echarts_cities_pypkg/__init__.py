# flake8: noqa
import os
import json
import codecs

from echarts_cities_pypkg._version import __version__
from echarts_cities_pypkg._version import __author__
from lml.plugin import PluginInfo


@PluginInfo('pyecharts_geo_data_bank', tags=['custom'])
class Pypkg():
    def __init__(self):
        __package_path__ = os.path.dirname(__file__)
        self.js_extension_path = os.path.join(
            __package_path__, "resources")

    def get_cities_in_country(self, country):
        _file = country.upper()
        _country_json = os.path.join(self.js_extension_path,
                                     "echarts-cities-js",
                                     _file + ".json")
        if os.path.exists(_country_json):
            with codecs.open(_country_json, encoding="utf-8") as file_handle:
                return json.load(file_handle)
        else:
            return None
