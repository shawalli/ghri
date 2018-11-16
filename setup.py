from pathlib import Path
from setuptools import setup, find_packages

about_file = Path(Path(__file__).parent, "ghri", "__about__.py")

about = {}
with open(about_file) as f:
    exec(f.read(), about)

long_description = ''
with open('README.rst') as f:
    long_description = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__summary__"],
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url=about["__uri__"],
    author=about["__author__"],
    author_email=about["__email__"],
    license=about["__license__"],
    packages=find_packages(),
    zip_safe=False,
    platforms="any",
    include_package_data=True,
    install_requires=[
        "attrdict",
        "Click",
        "click-didyoumean",
        "click-log",
        "marshmallow",
        "PyGithub",
        "requests"
    ],
    entry_points="""
        [console_scripts]
        ghri=ghri.scripts.ghri:cli
    """,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    keywords="github git vcs command-line cli releases python",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Click",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Utilities",
    ]
)
