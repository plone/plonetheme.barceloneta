In order to develop plonetheme.barceloneta you need to execute on the root of
the package::

     sudo npm install
     sudo npm install -g grunt-cli

If you change the images/fonts files you can copy to the package at::

     grunt copy

After executing this commands you can run grunt to watch the changes::

     grunt watch

This will make sure that the many .less files are compiled to .css on the fly
and then served up from the theme. See rules.xml for the relevant Diazo rules.

Notes
-----

- Make sure that Development Mode is enabled by going to the `Site Setup` > `Resource Registries` and check the `Development Mode` box, this ensures that your changes show up and aren't cached.

- If you want to modify plonetheme.barceloneta LESS you can either run `grunt less` to do a one-off compile or `grunt watch` to compile on change, this should be done from the plonetheme.barceloneta src folder
