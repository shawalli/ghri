from setuptools import setup, find_packages

setup(
    name="ghri",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "attrdict",
        "Click",
        "click-didyoumean",
        "click-log",
        "PyGithub",
        "marshmallow",
        "requests"
    ],
    entry_points="""
        [console_scripts]
        ghri=ghri.scripts.ghri:cli
    """,
)
