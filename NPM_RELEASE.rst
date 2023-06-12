========================
NPM Release Instructions
========================

.. note::
    You need the correct access rights to publish to npm or pypi.


- First create a pypi release using zest.releaser. This tool also creates the correct tag based on the setup.py version.
- After the pypi release edit the release version in package.json.
- Run: `npm publish`


------------
Pre-Releases
------------

Based on https://survivejs.com/maintenance/packaging/publishing/#publishing-a-pre-release-version

    - Change version in package.json to corresponding version in setup.py
    - You can also use `npm version 3.0.0-beta1` - This will change the version in package.json and create a git tag.
    - `npm publish --tag beta` - Publish the package under beta tag.
    - Mark beta release as latest with `npm dist-tag add @plone/plonetheme-barceloneta-base@3.0.0-beta1 latest``

To consume the test version, users have to use `npm install @plone/plonetheme-barceloneta-base@beta`.
