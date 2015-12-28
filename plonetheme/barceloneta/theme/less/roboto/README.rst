Fonts
-----

This readme has some information about the shipped font files and where these
font files are from.

Download
--------

The Roboto fonts in this directory are downloaded from:

    `http://www.fontsquirrel.com/fonts/roboto`

Download settings:

    Choose a subset:     No Subsetting
    Choose font formats: TTF, EOT, WOFF, SVG. All checked.


Subsetting
----------

Subsetting reduces the number of glyphs in the font to make a smaller file.
The shipped with Barceloneta contain all designed glyphs (no subset).


Formats
-------

Roboto fonts shipped with Barceloneta are available in the following file types:

TTF - Works in most browsers except IE and iPhone.
EOT - IE only.
WOFF - Compressed, emerging standard.
SVG - iPhone/iPad.


Changes
-------

  - All downloaded fonts are moved into one `roboto` directory
  - The downloaded file names where renamed. Dropped `-webfont`.
  - `Apache License.txt` is also moved into the `roboto` directory


SVG IDs
-------

SVG fonts need the correct ID in the font-face declaration. These are the
id's as supplied in the font-face declarations by Font Squirrel:

  - robotoblack_italic
  - robotobold
  - roboto_condensedbold
  - robotoblack
  - roboto_condensedbold_italic
  - robotobold_italic
  - roboto_condensedregular
  - roboto_condenseditalic
  - robotoitalic
  - robotolight
  - roboto_condensedlight
  - roboto_condensedlight_italic
  - robotolight_italic
  - robotomedium
  - robotomedium_italic
  - robotoregular
  - robotothin
  - robotothin_italic


Local
-----

Roboto is Androids default font. Therefore it is likely to be available on many
devices. We use `local` in the font-face declaration to let the browser
try to load the system installed Roboto first.

Noto
----

Google has been developing a font family called Noto, which aims to support
all languages with a harmonious look and feel. So checkout
`http://www.google.com/get/noto` if you need to support a language that
has other writing system than supported by Roboto.
