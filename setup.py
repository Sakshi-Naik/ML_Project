from setuptools import setup, find_packages

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path)-> list[str]:
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name= 'mlproject',
    version= '0.0.1',
    author= 'Sakshi Naik',
    author_email= 'sakshi2001.sn@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')
)