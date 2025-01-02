from setuptools import find_packages,setup
from typing import List
def get_requirements(path:str)->List[str]:
    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if '-e .' in requirements:
                requirements.remove('-e .')
    return requirements
    

setup(
    name='mlproject',
    version='0.0.1',
    author='Abu',
    author_email='mdabucse@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
)
