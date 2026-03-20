'''
       the setup.py is an essential part of packaging and distribution 
       python project . it is used by setuptools (or disutills in older
       python version ) to define the configuration of your project , 
       such as it's metadata, dependencies and more 
'''
from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    '''this function will return the list of requiremnets '''
    requirement_lst:list[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file 
            lines = file.readlines() 
            # Process each line 
            for line in lines:
                requirement=line.strip()
                # ignore empty lines an -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return  requirement_lst

setup(
    name="Network Security",
    version='0.0.1',
    author='Aakash Talyan',
    author_email='aakashtalyan14@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)