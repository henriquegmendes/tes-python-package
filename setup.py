from setuptools import setup, find_packages

setup(
    name='hentestpackage',
    version="0.0.2",
    packages=find_packages(),
    description='Test',
    include_package_data=True,
    url='https://github.com/henriquegmendes/tes-python-package/',
    author='Henrique Mendes',
    author_email='henrique.gmendes@hotmail.com',
    classifiers=[
        'Environment :: Backend Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/TCP',
    ],
)
