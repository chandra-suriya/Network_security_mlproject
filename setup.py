'''
the setup.py is an essential of packaging and distributing python projects 
it is used to define the configurations of your project such as it metadata, dependencies,and  more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements

    """
    requirement_list:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            #read the lines from the files
            lines = file.readlines() 
            #process the each line
            for line in lines:
                requirement = line.strip()
                ## ignore the empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    
    except Exception as e:
        print(f"some issues while installing requirments .txt : {e}")
    
    return requirement_list

#installing the file
                     
setup(
    name = "Network_security_mlproject",
    version = "0.0.1",
    author = "Chandra suriya",
    author_email="chandrasuriya305@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)

