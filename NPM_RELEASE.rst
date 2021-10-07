========================
NPM Release Instructions
========================

------------
Pre-Releases
------------

Based on https://survivejs.com/maintenance/packaging/publishing/#publishing-a-pre-release-version

    - Change version in package.json to correspondig version in setup.py
    - You can also use `npm version 3.0.0-alpha5` - This will change the version in package.json and create a git tag.
    - `npm publish --tag alpha` - Publish the package under alpha tag.

To consume the test version, users have to use `npm install @plone/plonetheme-barceloneta-base@alpha`.