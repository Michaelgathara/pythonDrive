from setuptools import setup
setup (
    name = 'pythonDrive',
    version = '0.1',
    description = 'A Python wrapper for Google Drive API',
    author = 'Michael Gathara',
    author_email = 'michael@michaelgathara.com',
    maintainer = 'Michael Gathara',
    maintainer_email = 'michael@michaelgathara.com',
    url = 'https://michaelgathara.com/pythondrive',
    license='MIT',
    packages = ['pythondrive'],
    install_requires = [
        "cachetools >= 5.2.0",
        "certifi >= 2022.5.18.1",
        "charset-normalizer >= 2.0.12",
        "google-api-core >= 2.8.1",
        "google-api-python-client >= 2.50.0",
        "google-auth >= 2.7.0",
        "google-auth-httplib2 >= 0.1.0",
        "googleapis-common-protos >= 1.56.2",
        "httplib2 >= 0.20.4",
        "idna >= 3.3",
        "protobuf >= 3.20.1",
        "pyasn1 >= 0.4.8",
        "pyasn1-modules >= 0.2.8",
        "pyparsing >= 3.0.9",
        "requests >= 2.28.0",
        "rsa >= 4.8",
        "six >= 1.16.0",
        "uritemplate >= 4.1.1",
        "urllib3 >= 1.26.9"

    ],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)