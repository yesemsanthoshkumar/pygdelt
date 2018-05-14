from setuptools import setup, find_packages
from codecs import open
from os import path

with open(
    path.join(
        path.dirname(path.abspath(__file__)),
        'README.md'
        )) as readme:
    DESC = readme.read()

setup(
    name='pygdelt',
    version='0.0.1a1',
    description='An easy interface to GDELT datasets',
    long_description=DESC,
    long_description_content_type='text/markdown',
    url='https://github.com/yesemsanthoshkumar/pygdelt',
    author='yesemsanthoshkumar',
    author_email='yesemsanthoshkumar@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='gdelt',
    packages=["pygdelt"],
    install_requires=[
        'requests>=2.18.4',
        'tqdm>=4.23.2'
    ],
    package_data={
        '': ['LICENSE'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/yesemsanthoshkumar/pygdelt/issues',
        'Source': 'https://github.com/yesemsanthoshkumar/pygdelt',
    }
)
