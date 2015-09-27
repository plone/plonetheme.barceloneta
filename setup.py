import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.6.14'

long_description = (
    read('README.rst') + '\n' +
    read('CHANGES.rst') + '\n'
    )

setup(name='plonetheme.barceloneta',
      version=version,
      description="The default theme for Plone 5.",
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 5.0",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          ],
      keywords='web zope plone theme',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plonetheme.barceloneta',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
      ],
      extras_require={
          'test': [
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
