from setuptools import find_packages, setup

with open("VERSION") as f:
    version = f.read().strip()

with open("README.md") as fh:
    readme = fh.read()

setup(
    name='file_uploader_lib',
    version=version,
    author='Saidur Rahman Sajol',
    description="Python library for uploading data to specific table",
    license='Proprietary',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/scorchSupernova/file_uploader_lib",
    install_requires=[
        'minio',
        'psycopg2-binary',
        'pandas',
        'openpyxl'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: Other/Proprietary License",
    ],

)
