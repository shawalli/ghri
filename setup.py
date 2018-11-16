from pathlib import Path
from setuptools import setup, find_packages

about_file = Path(Path(__file__).parent, "ghri", "__about__.py")

about = {}
with open(about_file) as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__summary__"],
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
        "PyGithub",
        "marshmallow",
        "requests"
    ],
    entry_points="""
        [console_scripts]
        ghri=ghri.scripts.ghri:cli
    """,
    python_requires=">=3.7",
    keywords="github git vcs command-line cli releases python",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Click",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Utilities",
    ]
)
