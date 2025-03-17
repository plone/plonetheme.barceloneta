from pathlib import Path
from setuptools import find_packages
from setuptools import setup


version = "3.2.3"

long_description = f"{Path('README.md').read_text()}\n{Path('CHANGES.md').read_text()}"

setup(
    name="plonetheme.barceloneta",
    version=version,
    description="The Classic-UI theme for Plone 6.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: Core",
        "Framework :: Plone :: Theme",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="web zope plone theme",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/plone/plonetheme.barceloneta",
    license="GPL version 2",
    packages=find_packages(),
    namespace_packages=["plonetheme"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "plone.app.theming",
        "plone.resource",
        "plone.theme",
        "Products.GenericSetup",
    ],
    extras_require={"test": []},
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
