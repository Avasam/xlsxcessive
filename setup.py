from setuptools import setup

setup(
    name="XlsXcessive",
    version="0.1.3",
    description="A Python library for writing .xlsx files.",
    packages=['xlsxcessive'],
    author="Christian Wyglendowski",
    author_email="christian@dowski.com",
    url="http://xlsx.dowski.com/",
    license="MIT",
    install_requires = [
        'openpack',
    ],
)
