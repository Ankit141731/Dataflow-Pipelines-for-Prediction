from setuptools import setup , find_packages
from typing import List

PROJECT_NAME = "learning_project"
VERSION = "0.0.0"
AUTHOR_NAME = "Ankit"
DESCRIPTION = "This project is meant for self learning of project requirements"
AUTHOR_EMAIL = "ac7265036@gmail.com"
REQUIREMENTS = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements():
    with open(REQUIREMENTS) as f:
        list_of_requirements = f.readlines()
        list_of_requirements = [requirements.replace("\n" , "") for requirements in list_of_requirements]
        
        if HYPHEN_E_DOT in list_of_requirements:
            list_of_requirements.remove(HYPHEN_E_DOT)

        return list_of_requirements
setup(

    name = PROJECT_NAME ,
    description = DESCRIPTION ,
    version = VERSION ,
    author = AUTHOR_NAME ,
    author_email = AUTHOR_EMAIL ,
    packages = find_packages() ,
    install_requires = get_requirements(),
    
)