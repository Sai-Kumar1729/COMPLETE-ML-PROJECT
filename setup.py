from setuptools import setup, find_packages

HYPEN_E_DOT = "-e ."
def get_requirements(file_path):
    requirements = []  
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(

    name = "ML Project",
    version = "0.0.1",
    author = "Sai Kumar",
    author_email = "saikumarkummari1729@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")

)