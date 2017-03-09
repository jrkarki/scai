import setuptools
import os
import codecs

KEYWORDS = ['Testing', 'Devops']
CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.6',
    'Topic :: Scientific/Engineering :: Bio-Informatics'
]

HERE = os.path.abspath(os.path.dirname(__file__))


def get_long_description():
    """Get the long_description from the README.rst file. Assume UTF-8 encoding."""
    with codecs.open(os.path.join(HERE, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

if __name__ == '__main__':
   setuptools.setup(
       name='scai',
       version='v 0.1',
       author='Reagon Karki',
       author_email='reagon.karki@scai-extern.fraunhofer.de',
       description='',
       license='',
       url='https://github.com/jrkarki',

       # Look for python code inside /src/
       packages=setuptools.find_packages(where='src'),

       # Assign the package-level folder ('') to be the one it finds in 'src'
       package_dir={'': 'src'},

       install_requires=[
           'click',
       ],


        long_description=get_long_description(),
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS,
    )