from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'Auxiliary module for calculating invariant representations of effective models of E_8xE_8'


# Setup

setup(
    name="MKD",
    version=VERSION,
    description=DESCRIPTION,
    author="Enrique Escalante-Notario, Ignacio Portillo-Castillo, Saúl Noé Ramos-Sánchez",
    author_email="enriquescalante@gmail.com"
    url="http://github.com/enriqueescalante",
    install_requires=['itertools','numpy','shlex', 'subprocess','os','re']
    scripts=[]
)
