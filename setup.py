from setuptools import find_packages,setup
from typing import List


HYPER_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function return the list of requirements
    """
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n'," ") for req in requirements]
        

        if HYPER_E_DOT in requirements:
            requirements = requirements.remove(HYPER_E_DOT)

    
    return requirements





setup(
    name="Student_performance",
    version="0.0.1",
    author="Professor Nitish",
    email="professorernitish@gmail.com",
    packages=find_packages(),
    install_requires =get_requirements('requirements.txt')
)