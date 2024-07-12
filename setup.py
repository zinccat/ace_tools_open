from setuptools import setup, find_packages

setup(
    name='ace_tools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'itables',
        'IPython',
    ],
    extras_require={
        'dev': ['pytest']
    },
    description='Open implementation of ace_tools referenced in GPT4o.',
    author='ZincCat',
    author_email='zincchloride@outlook.com',
    url='https://github.com/zinccat/ace_tools',
)
