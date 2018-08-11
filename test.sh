pip freeze
nosetests --with-coverage --cover-package echarts_cities_pypkg --cover-package tests tests echarts_cities_pypkg && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
