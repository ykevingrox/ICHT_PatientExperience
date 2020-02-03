import codecs
import os
import sys
try:
	from setuptools import setup, find_packages
except:
	from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'ICHT_PatientExperience',
      description = 'A pre-trained text classification model',
      long_description = read("README.txt"),
      version = '1.0',
      author = 'Jingxian You',
      author_email = 'jingxian.you@nhs.net',
      packages = find_packages('models'),
      package_data={
              'ICHT_PatientExperience.models': ['*'],
              },
      include_package_data=True,
      url = "https://github.com/ykevingrox/ICHT_PatientExperience"
      )