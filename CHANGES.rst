Changelog
=========

1.6.13 (2015-09-20)
-------------------

- Add spaces beetween checks and labels in search filter (closes `#982`_).
  [rodfersou]

- Center buttons on ordered selection lists (closes `#1017`_).
  [rodfersou]

- Center checkboxes on user/group matrix (closes `1003`_).
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
.. _`#982`: https://github.com/plone/Products.CMFPlone/issues/982
.. _`#1003`: https://github.com/plone/Products.CMFPlone/issues/1003
.. _`#1017`: https://github.com/plone/Products.CMFPlone/issues/1017
