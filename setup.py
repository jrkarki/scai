import setuptools

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
  )
