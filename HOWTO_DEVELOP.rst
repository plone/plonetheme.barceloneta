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
