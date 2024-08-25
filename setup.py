from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.read().splitlines()

setup(
    name='cheshire-orca-interfaces',
    version='1.0.0',
    packages=find_packages(where='src'),
    install_requires=read_requirements(),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        '': ['py.typed']
    },
    author='Cheshire Labs',
    author_email='michaeltsalmi@cheshirelabs.io',
    description='External interfaces for Orca laboratory automation software',
    url='https://github.com/Cheshire-Labs/orca-interfaces',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10'
)