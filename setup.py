
try:
    from setuptools import find_packages, setup
except:
    from distutils.core import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="MediumBot",
    version="0.0.1",
    author="Deyaa Muhammad",
    author_email="deyaa@hackermotto.com",
    description="Medium Bot.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hackermotto/mediumbot",
    scripts=[
        # "scripts/mediumbot",
        # "scripts/mediumbot.service",
        ],
    data_files=[
        ("mediumbot", ["config/logging.yaml"]),
        ("mediumbot", ["config/default.yaml"]),
    ],
    entry_points={'console_scripts': ['mediumbot=mediumbot.__main__:main']},
    packages=find_packages(
        where="src",
        # exclude = ['additional',]
    ),
    package_dir={"":"src"},
    python_requires=">=3",
    platforms=["win32", "linux", "linux2", "darwin"],
    install_requires=[
        "beautifulsoup4==4.9.3",
        "bs4==0.0.1",
        "PyYAML==5.4.1",
        "schedule==1.1.0",
        "selenium==3.141.0",
        "soupsieve==2.2.1",
        "urllib3==1.26.4"
    ],
    include_package_data=True,
    zip_safe=False,
    license=[
        "Apache 2",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules"
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 5 - Production/Stable",
    ],
    project_urls={
        "Funding": "https://www.paypal.me/DeyaaMuhammad",
        "Documentation": "http://mediumbot.readthedocs.io/en/latest/",
        "Bug Tracker": "https://github.com/hackermotto/mediumbot/issues",
        "Source": "https://github.com/hackermotto/mediumbot"
    },
)
