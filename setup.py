from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    # requirements = []
    hypen_e_dot = '-e.'
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()  ## will return ['numpy\n','pandas\n']
        requirements = [req.replace("\n","").strip() for req in requirements]
    if hypen_e_dot in requirements:
        requirements.remove(hypen_e_dot)
    return requirements
    


setup(
    name="MarketResearchAndUseCaseGenerator",   ## project name 
    version = "1.0.0",        ## project version
    author='Rohit Kumar',     ## project author name
    install_requirements = get_requirements('requirements.txt'),   ## path of requirements.txt
    packages = find_packages()
 ) 