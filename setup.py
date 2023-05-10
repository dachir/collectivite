from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in collectivite/__init__.py
from collectivite import __version__ as version

setup(
	name="collectivite",
	version=version,
	description="La gestion des collectivités",
	author="Kossivi",
	author_email="dodziamouzou@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
