from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='emencia.django.french_zones',
      version=version,
      description='French regions and departments utilities for your Django projects',
      long_description=open('README.rst').read() + '\n' +
                       open(os.path.join('docs', 'HISTORY.txt')).read(),
      keywords='django, french, departments, regions',
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: BSD License',
          'Framework :: Django',
          ],

      author='Fantomas42',
      author_email='fantomas42@gmail.com',
      url='http://emencia.fr',
      
      license='BSD License',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['emencia', 'emencia.django'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
