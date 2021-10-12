import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cptec',
    version='0.0.1',
    author='Gustavo da Silva Serra',
    author_email='gustavo.silva.serra@gmail.com',
    description='Cliente de previsão do tempo do CPTEC/INPE',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/gustavo-silva-serra/pycptec',
    project_urls = {},
    license='MIT',
    packages=['cptec'],
    install_requires=[],
    license_files = ('LICENSE.txt',),
)