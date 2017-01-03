Changelog
=========


1.6.23 (2017-01-02)
-------------------

Bug fixes:

- Fix weird nav scrollbars on mobile
  [agitator]


1.6.22 (2016-11-09)
-------------------

New features:

- Add default content type icon to add menu only. Add missing npm dependency.
  [alecm]

Bug fixes:

- Unset select width and display
  [agitator]

- Isolate the autotabs class for ``ul`` elements to ``.autotabs ul.autotoc-nav``.
  Fixes an issue, where list elements in an inline TinyMCE content area were displayed wrong.
  [thet]

- Fix buttons alignment in ordered selection widget
  [ale-rt]


1.6.21 (2016-06-07)
-------------------

Bug fixes:

- Remove references to discarded offcanvas feature
  [davilima6]


1.6.20 (2016-05-25)
-------------------

Bug fixes:

- Set news lead image background for transparent images
  https://github.com/plone/plonetheme.barceloneta/issues/107
  [staeff]


1.6.19 (2016-05-15)
-------------------

New:

- Add styles for manage portlets jumplist
  [davilima6]

Fixes:

- Use ``.alert.status`` selector as an alternative to ``.portalMessage``.
  This class is used by the structure pattern.
  [thet]

- Make search button grow with the search buttons text.
  Fixes an issue where translated button texts were not fitting into the button.
  [kkhan, thet]


1.6.18 (2016-03-31)
-------------------

New:

- Add missing caret styles.
  [thet]

- Extended form styles for input type="email".
  [agitator]

- Isolate calendar portlet styles.
  [agitator]

- Added invisible-grid table styles.
  [agitator]

- Action control panel specific rendering.
  [ebrehault]

Fixes:

- Improved "feel" for the Site Setup (@@overview-controlpanel)
  https://github.com/plone/Products.CMFPlone/issues/1435
  [pigeonflight]

- Fix code analysis errors reported by http://jenkins.plone.org/view/Pkgs/job/package-plonetheme.barceloneta
  [gforcada]
- Drop toolbar for anonymous users.
- Fixed html validation:
  - the banner role is unnecessary for element header,
  - element main does not need a role attribute,
  - the contentinfo role is unnecessary for element footer.
  [maurits]


1.6.17 (2016-02-27)
-------------------

New:

- Modernize pagination markup and switches deprecated ``listingBar`` CSS class to ``pagination``.
  [davilima6]

Fixes:

- Move hero to content
  Issue https://github.com/plone/Products.CMFPlone/issues/974
  [gyst]

- Add ``barceloneta-mixin-font`` to the registerless profile.
  [pcdummy]

- Inline ``style`` tags in head are no more skipped
  [keul]

- Follow best practice for readme.rst
  [allcaps]

- Center the leadimage on the modal window.
  Partially close `#321`_.
  [keul]

- Fix filenames for roboto-lightitalic.ttf, -mediumitalic.ttd
  and -bolditalic.ttf to match those in less files
  [datakurre]


1.6.16 (2016-01-08)
-------------------

Fixes:

- Add 2014 Roboto
  [allcaps]

- Fix @font-face. Load eot, svg and woff.
  [allcaps]

- Add Roboto fonts with full glyph set
  [allcaps]

- Add weight to all fonts (contributes to `#24`_).
  [allcaps]

- Restore the principal aka jumbotron background.
  [allcaps]

- Fix sitemap layout. Drop the columns. (closes `#57`_).
  [allcaps]

- Remove trailing comma's in Grunt file.
  [allcaps]

- Use border radius variables in portlets.
  [allcaps]

- Mismatched properties and values.
  [allcaps]

- Ignore diff of map file.
  [allcaps]


1.6.15 (2015-11-28)
-------------------

Fixes:

- Fixed some css rules (missing clearfixes, aligning thumbs, ...).
  https://github.com/plone/plonetheme.barceloneta/issues/62
  [fgrcon]

- Added css-rules for thumbnails in listings and portlets.
  Related to `#1226`_.
  [fgrcon]

- Underline links in #content-core (criterion 1.4.1).
  [polyester]

- Increased contrast, eliminated contrast-checker false positives.
  [polyester]

- Title under thumb in albumview (closes `#1091`_).
  [polyester]

- Don't include diazo bundle in backend theme.
  [instification]

- Discard duplicated ids for columns (closes `#1105`_)
  [davilima6]

- Add comment to alert on duplicate resource registering
  [davilima6]


1.6.14 (2015-09-27)
-------------------

- Fix in barceloneta word wrap in event listing.
  [sneridagh]


1.6.13 (2015-09-20)
-------------------

- Add spaces beetween checks and labels in search filter (closes `#982`_).
  [rodfersou]

- Center buttons on ordered selection lists (closes `#1017`_).
  [rodfersou]

- Center checkboxes on user/group matrix (closes `#1003`_).
  [rodfersou]

- Remove hero-element from index.html. Instead include a view @@hero.
  Fixes https://github.com/plone/Products.CMFPlone/issues/974
  [pbauer]

- Harmonize plone.app.discussion styles and discussion.plone.less styles
  refs (refs `#764`_)
  [ichim-david]

- Fix display of date widget arrows and footer buttons (refs `#891`_).
  [ichim-david]

- Clean Gruntfile.js, package.json and HOWTO_DEVELOP.rst of grunt
  plugins and information which this package no longer uses since
  commit 9f5434
  [ichim-david]

- provide basic table styles
  [vangheem]

- Fixed (refs `#979`_ and `#981`_) related to text not wrapping when unusual
  (and artificial) text with no white-space exists in the page
  [sneridagh]

- Fixed styling problems when figcaption is very long
  [sneridagh]

- Renamed the news.plone.less into behaviors.plone.less as it no longer make
  sense
  [sneridagh]


1.6.12 (2015-09-12)
-------------------

- Fix display of album_view title links (closes `#911`_).
  [ichim-david]


1.6.11 (2015-09-08)
-------------------

- Bring back document byline (closes `#741`_).
  [rodfersou]

- Prefer rules with CSS selectors over XPath whenever possible
  [davilima6]


1.6.10 (2015-09-07)
-------------------

- Add a pared down version of barceloneta to include in your theme to save you
  making a custom backend theme.
  [djay]


1.6.9 (2015-08-22)
------------------

- Hide searchbox, personaltools, breadcrumbs in print.css
  [gomez]

- Updated font-weight on portlet headers
  [pigeonflight]

- Update font-weight on portlet management items
  [vangheem]

- Updated to index.html: link to plone.com opens in new window/tab
  [tkimnguyen]


1.6.8 (2015-07-18)
------------------

- New control panel overview and portlet layout.
  [sneridagh]

- Fixed bug in portlet navigation due to a CSS error.
  [sneridagh]

- Fix problem with CSS leaking from the cp overview to the portlet.
  [sneridagh]

- Fix map.
  [sneridagh]

- Added a:hover styles for h1 h2 h3.
  [agitator]

- Role for gigantic is complementary.
  [bloodbare]

- Do not use absolute prefix to reference index.html to copying themes
  does not reference original theme file.
  [vangheem]

- Toolbar fixes.
  [bloodbare]

- Various mobile fixes.
  [agitator]

- Update index.html. Change plone.org link to plone.com.
  [tkimnguyen]

- Do not uppercase the colophon.
  [gforcada]


1.6.7 (2015-06-05)
------------------

- provide more sane default widths and heights to select[multiple] and
  textareas
  [vangheem]

- hide crud-form select header by default
  [vangheem]

- remove loader since it is in mockup now
  [vangheem]

- tweak manage portlets styles
  [vangheem]

- fixed rules for copying content.
  [hvozdovych]


1.6.6 (2015-05-13)
------------------

- provide some spacing between event summary and content
  [vangheem]


1.6.5 (2015-05-05)
------------------

- Fix extending barceloneta with xi:include
  [pbauer]


1.6.4 (2015-05-04)
------------------

- fix in and out widget button style
  [vangheme]

- no one likes the star for required field label, try circle
  [vangheem]

- add plone-loader style so you can add decent loader to javascript
  [vangheem]

- add styles for search form
  [vangheem]

- Cleanup: Remove unused resources.
  [thet]

- Fix toggling navigation at mobile widths.
  [davisagli]

- Remove sticky footer (it required a hardcoded height, which does not work
  for an element that may have varying content).
  [davisagli]

- Add clearfix to `.row`.
  [davisagli]

- pat-modal pattern has been renamed to pat-plone-modal
  [jcbrand]


1.6.3 (2015-03-26)
------------------

- Add language selector widget
  [bloodbare]


1.6.2 (2015-03-21)
------------------

* Change font family of ``form.widgets.IRichText.text`` textareas to monospace.
  This affects the texteditor only in non-Richtext mode and helps editing e.g.
  Restructured Text.
  [thet]

* Change ``min-height`` of textarea fields from auto to ``4em`` (description,
  etc.), respectively ``12em`` for IRichText widgets (e.g. when displayed
  without a visual editor).
  [thet]

* Return to being a clean Diazo theme so that we are a safe starting point for
  people building their own themes and a good practice example that works when
  copying the theme in the TTW theme editor.
  [optilude, bloodbare]


1.6.1 (2014-11-01)
------------------

* Remind committers to add changelog entries. I'm not your monkey.
  [esteele]


1.6.0 (2014-04-20)
------------------

* Initial release
  [esteele]

.. _`#741`: https://github.com/plone/Products.CMFPlone/issues/741
.. _`#764`: https://github.com/plone/Products.CMFPlone/issues/764
.. _`#891`: https://github.com/plone/Products.CMFPlone/issues/891
.. _`#911`: https://github.com/plone/Products.CMFPlone/issues/911
.. _`#979`: https://github.com/plone/Products.CMFPlone/issues/979
.. _`#981`: https://github.com/plone/Products.CMFPlone/issues/981
.. _`#982`: https://github.com/plone/Products.CMFPlone/issues/982
.. _`#1003`: https://github.com/plone/Products.CMFPlone/issues/1003
.. _`#1017`: https://github.com/plone/Products.CMFPlone/issues/1017
.. _`#1091`: https://github.com/plone/Products.CMFPlone/issues/1091
.. _`#1105`: https://github.com/plone/Products.CMFPlone/issues/1105
.. _`#1226`: https://github.com/plone/Products.CMFPlone/issues/1226
.. _`#24`: https://github.com/plone/plonetheme.barceloneta/issues/24
.. _`#57`: https://github.com/plone/plonetheme.barceloneta/issues/57
.. _`#321`: https://github.com/plone/plone.app.contenttypes/issues/321
