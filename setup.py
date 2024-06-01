from setuptools import setup, find_packages

setup(
    name='our_stopwords',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
       'pandas',
       'scikit-learn'
    ],
    package_data={
        'our_stopwords': ['data/*.jsonl'],
    },
    author='Ndamulelo Nemakhavhani',
    author_email='endeesa@yahoo.com',
    description='A package for accessing multilingual stop words for South African Bantu Languages.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ndamulelonemakh/our-stopwords',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'our_stopwords = our_stopwords.__main__:cli'
        ]
    },
)
