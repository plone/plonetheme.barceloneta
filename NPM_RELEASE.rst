========================
NPM Release Instructions
========================

------------
Pre-Releases
------------

Based on https://survivejs.com/maintenance/packaging/publishing/#publishing-a-pre-release-version

    - Change version in package.json to correspondig version in setup.py
    - `npm publish --tag alpha` - Publish the package under alpha tag.

To consume the test version, users have to use ``npm install @plone/plonetheme-barceloneta-base@alpha`.