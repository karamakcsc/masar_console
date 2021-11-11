from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in masar_console/__init__.py
from masar_console import __version__ as version

setup(
	name="masar_console",
	version=version,
	description="Database Console",
	author="KCSC",
	author_email="info@kcsc.com.jo",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
