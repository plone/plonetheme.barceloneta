In order to develop plonetheme.barceloneta you need to execute on the root of
the package::

     sudo npm install
     sudo npm install -g grunt-cli

After executing these commands you can run grunt to watch for any less changes::

     grunt watch

This will make sure that the many .less files are compiled to .css on the fly and then served up from the theme.

See rules.xml for the relevant Diazo rules.

If you prefer to do a one time compile of the less files you can run::

    grunt less

Note
----

- Make sure that Development Mode is enabled by going to the `Site Setup` > `Resource Registries`
  and check the `Development Mode` checkbox, this ensures that your changes show up and aren't cached.

Note
----

All css is compiled from LESS files. Do NOT edit the file barceloneta.css.original-reference, it is not read and is just there for reference purposes.


Fonts
-----

Read `plonetheme.barceloneta/plonetheme/barceloneta/theme/less/roboto/README.rst if you need to update the shipped fonts.