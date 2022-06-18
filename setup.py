from setuptools import setup

PROJECT_NAME = "Housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Pradeep Tripathi"
DISCRIPTION="This is a first machine learning project"
PACKAGES=['housing']
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list():
    """
    Description: This function is going to return list of requirement 
    mention in requirements.txt file
    
    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DISCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)