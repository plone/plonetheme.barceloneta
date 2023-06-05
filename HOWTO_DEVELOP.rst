In order to develop plonetheme.barceloneta you need to execute on the root of
the package::

     npm install

After executing this you can run the following command to watch for any scss changes
in the path `plonetheme.barceloneta/scss`::

     npm run watch

This will make sure that the many .scss files are compiled to .css on the fly
and then copied over to the theme.

If you simply want to compile all resources before a release run::

     npm run build


Theme
-----

See `plonetheme.barceloneta/plonetheme/barceloneta/theme/rules.xml` for the relevant Diazo theme rules.


Fonts
-----

Read `plonetheme.barceloneta/plonetheme/barceloneta/theme/roboto/README.rst` if you need to update the shipped fonts.
