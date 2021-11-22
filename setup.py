from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name='filters_package',
    version='0.5.7',
    author='Saul Rocha',
    author_email='saul.rocha2001@gmail.com',
    description= "Pacote que modifica imagens rgb para canais de imagens LUV, aplica os filtros gray, gaussiano, clahe, equalização de histograma e bordas de objetos nas imagens em uma determianda pasta com N imagens",
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/saul-rocha/FilterFS.git',
    project_urls ={
        "Bug Tracker": "https://github.com/saul-rocha/FilterFS.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"":"src"},
    packages= setuptools.find_packages(where = 'src'),
    python_requires = ">=3.8",
)