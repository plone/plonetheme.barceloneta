============
 Barceloneta
============
------------------------------
 The default theme for Plone 5
------------------------------

`Latest version on PyPI <https://pypi.python.org/pypi/plonetheme.barceloneta>`_

Documentation
=============

`Plonetheme.barceloneta documentation <http://docs.plone.org/adapt-and-extend/theming/barceloneta.html>`_ is part of the official Plone documentation.

Source Code and Contribution
============================

Contributors
    please read the document `Process for Plone core's development <http://docs.plone.org/develop/coredev/docs/index.html>`_.
    Also consult the section about contribution in the `plone.api contributors documentation <http://docs.plone.org/develop/plone.api/docs/contribute/index.html>`_.

Source-Code
    at the `Plone code repository hosted at Github <https://github.com/plone/plonetheme.barceloneta>`_.

Issues
    Please use the `Issue-Tracker <https://github.com/plone/plonetheme.barceloneta/issues>`_

If you made changes to the less files, to rebuild the files ``barceloneta-compiled.css`` and ``barceloneta-compiled.css.map`` you can execute this::

    cd plonetheme.barceloneta/plonetheme/barceloneta/theme/less
    npx lessc --source-map=barceloneta-compiled.css.map barceloneta.plone.local.less barceloneta-compiled.css
