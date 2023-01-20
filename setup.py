from setuptools import find_packages,setup
from typing import List

REQUIREMENTS_FILE_NAME="requirements.txt"
REMOVE_PACKAGE="-e ."
def get_requirements_file()-> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as REQUIREMENTS_FILE:
        requirement_list = REQUIREMENTS_FILE.readline()
    requirement_list  = [requirement_name.replace("\n"," ") for requirement_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list
setup(name='Insurance',
      version='1.0',
      description='Insurance Premium Prediction',
      author='Rais Jalia',
      author_email='raisjaliarj@outlook.com',
      packages=find_packages(),
      install_reqires = get_requirements_file()
     )