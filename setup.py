from setuptools import setup,find_packages;
from typing import List;

def get_requirements(file_path:str)->List[str]:
    requirements=[]

    e_hyp='-e .'

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if e_hyp in requirements:
            requirements.remove(e_hyp)
    
    return requirements



setup(
    name="ML Project",
    version="0.0.1",
    author="Daksh Patel",
    author_email="daksh6928@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)