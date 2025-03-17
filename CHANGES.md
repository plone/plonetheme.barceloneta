# Changelog

<!--
   You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
-->

<!-- towncrier release notes start -->

## 3.2.3 (2025-03-18)


### Bug fixes:

- Switch from npm to pnpm. @petschki

  Update `TinyMCE=7.7.1`. @petschki

  Update Developer documentation. @petschki #392

## 3.2.2 (2025-01-27)


### Bug fixes:

- Fix DeprecationWarnings. [maurits] #4090


### Internal:

- TinyMCE = 7.6.1
  [petschki] #389

## 3.2.1 (2024-12-17)


### Bug fixes:

- Upgrade TinyMCE 7.6.0
  [petschki] #384


### Internal:

- Upgrade development dependencies.
  [petschki] #384

## 3.2.0 (2024-10-30)


### Bug fixes:

- Upgrade dependencies.
  [petschki] #382

## 3.2.0a6 (2024-09-03)


### Bug fixes:

- Upgrade dependencies.
  [petschki] #380

## 3.2.0a5 (2024-08-01)


### New features:

- Add styles for details/summary based collapsibles.
  Add support for labels wrapping input fields.

  Ref: https://github.com/plone/Products.CMFPlone/pull/3976 #374
- [yurj] Add the portal_url parameter to be used with Diazo rules and implement it in backend.xml #376

## 3.2.0a4 (2024-04-26)


### New features:

- TinyMCE 7.0
  this is a version bump only. There are no CSS changes from TinyMCE 6 -> 7
  [petschki] #371


### Bug fixes:

- Remove deprecated SVG font resources
  [petschki] #357
- Fix sticky `.formControls` to not break modals with buttons.
  [petschki] #367

## 3.2.0a3 (2024-01-23)


### Bug fixes:

- pat-plone-modal works fine now and also this would remove "nav-link dropdown-item" classes, unstyling the menu entries
  [yurj] #358
- Sticky formControls in edit forms.
  Dependency updates.
  [petschki] #361

## 3.2.0a2 (2023-12-12)


### Bug fixes:

- Sanitize color variables to more Bootstrap like approach with main `$primary` color.
  [petschki] #251
- Upgrade dependencies.
  [petschki] #356


## 3.2.0a1 (2023-10-24)


### New features:

- Upgrade TinyMCE styles to version 6
  [petschki] #350


## 3.1.6 (2023-10-24)


### Internal:

- Fix typo (BS version) in README
  [petschki] #0


## 3.1.5 (2023-09-19)


### Bug fixes:

- Update Bootstrap to ``5.3.2``
  [petschki] #346


## 3.1.4 (2023-07-30)


### Bug fixes:

- Update Bootstrap to ``5.3.1``
  [petschki] #343


### Internal:

- Update configuration files.
  [plone devs] cfffba8c


### Documentation:

- Fix broken links in the readme.
  [maurits] #338


## 3.1.3 (2023-06-05)


### New features:

- Update to Bootstrap 5.3 final release.
  [petschki] #333


### Bug fixes:

- Add "!optional" to extended grid breakpoints selectors to avoid errors when `$grid-breakpoints` is customized.
  [petschki] #329


## 3.1.2 (2023-04-18)

### New features:

- Upgrade Bootstrap `5.3.0-alpha3`
  [petschki] (#325)

### Internal:

- Update configuration files. [plone devs] (7032e1d4)

## 3.1.1 (2023-03-31)

### New features:

- Update to Bootstrap 5.3.0-alpha2. [toalba,lenadax] (#324)

## 3.1.0 (2023-03-05)

### New features:

- Simplify alert related styles. [lenadax] (#321)
- Adopt colormode related variables from Bootstrap 5.3. [lenadax]
  (#321)
- Update Bootstrap -> 5.3.0 [agitator] (#320)

### Bug fixes:

- Fix Diazo rule problem with undefined footer_portlets and
  footer_portlets_count variables. See:
  <https://community.plone.org/t/error-theme-inherited-from-barceloneta-footer-portlets-count/8455>
  (#239)

## 3.0.0 (2022-12-03)

### New features:

- Update Bootstrap -> 5.2.3 [petschki] (#316)

## 3.0.0b6 (2022-10-04)

### New features:

- Bootstrap 5.2.2 [petschki] (#313)

### Bug fixes:

- Add TinyMCE ui styles in non-inline mode. [petschki] (#307)
- Add content table styles [MrTango] (#311)

## 3.0.0b5 (2022-09-09)

### Bug fixes:

- Fix npm release, rm npmignore, use explicit whitelist in
  package.json, rm legacy scss [MrTango] (#306)

## 3.0.0b4 (2022-09-09)

### Bug fixes:

- prefix icon ptch in index.html with ++theme++barceloneta to prevent
  broken icon in other themes [MrTango] (#304)

## 3.0.0b3 (2022-09-07)

### Bug fixes:

- Include tinymce-formats.css in theme, so that they have an effect.
  [MrTango] (#301)

- Define max-height for toolbar dropdown so it scrolls if item list is
  too long. [petschki] (#302)

- disable diazo for manage-viewlets view, because Diazo is messing with viewlets and viewlet manager, which is more confusing than helpful
  [MrTango] (#303)

## 3.0.0b2 (2022-07-21)

### New features:

- Update Bootstrap 5.2.0 [petschki] (#300)

### Bug fixes:

- Show footer portlets when managing all portlets from
  @@manage-portlets [frapell] (#281)

## 3.0.0b1 (2022-06-24)

### New features:

- Example for extra styles that get automatically populated to the
  TinyMCE formats menu added. [agitator] (#282)
- Reimplement dropout toolbar submenus and collapsed icons. Create CSS
  variables for Plone colors. [petschki, agitator] (#283)
- Update to Bootstrap 5.2.0-beta1 and make use of CSS variables.
  [agitator] (#286)
- Global sections: add support for css variables and color modes
  barceloneta, dark, light [agitator] (#288)

### Bug fixes:

- Fix columns-order when only col-one is displayed. [pbauer] (#279)
- Fix text wrapping of long toolbar labels. [agitator] (#289)
- Toolbar width and wrapping tweaks. [agitator] (#292)
- Ensure pointer cursor on toolbar toggle icon. [petschki] (#294)

## 3.0.0a11 (2022-04-08)

### New features:

- Styling for liveSearch results with images. [agitator] (#278)

## 3.0.0a10 (2022-04-07)

### New features:

- moved toolbar css from mockup to barceloneta [petschki] (#267)
- Optimize image floating for content [MrTango] (#269)
- Mobile navigation as offcanvas sidebar and integration of search
  into main navigation. [agitator] (#271)
- Sticky footer [agitator] (#274)
- update title and preview for Plone 6 [petschki] (#275)

### Bug fixes:

- Reintroduce diff-styles for CMFEditions [pbauer] (#268)
- Update main grid breakpoint to lg. [agitator] (#277)

## 3.0.0a9 (2022-01-28)

### New features:

- del favicons from index.html and rules [talarias] (plip-favicon)

### Bug fixes:

- Be more specific where replacing the head title element [ale-rt]
  (#264)

## 3.0.0a8 (2021-12-01)

### New features:

- Refactored the scss for the alerts. [klye] (#250)

### Bug fixes:

- Remove unused IBarcelonetaLayer. [agitator] (#254)
- Add print styles. Disable important for utility classes. Enable
  negative margin utility classes. [agitator] (#255)

## 3.0.0a7 (2021-10-29)

### New features:

- Make loading of webfont optional. Move Barceloneta specific styles
  out of base.scss. Update to Bootstrap 5.1.3. [agitator] (#253)

### Bug fixes:

- event listing datecard style [petschki] (#252)

## 3.0.0a6 (2021-10-16)

### New features:

- Added npm packaging info [agitator] (#251)

## 3.0.0a5 (2021-09-15)

### New features:

- Update to Bootstrap 5.1.0 [petschki] (#247)
- Update to Bootstrap 5.1.1 [petschki] (#248)

## 3.0.0a4 (2021-08-04)

### Bug fixes:

- Optimize responsive header behavior. [agitator] (#1)

## 3.0.0a3 (2021-08-04)

### New features:

- Update to Bootstrap 5.0.1 [agitator] (#241)
- Update to Bootstrap 5.0.2 Update sitenav with Bootstrap defaults and
  cleanup. [agitator] (#243)

## 3.0.0a2 (2021-06-14)

### New features:

- Rework contenttype views. Update to Bootstrap 5.0.0-beta3
  [agitator] (#236)
- Update to Bootstrap 5.0.1 [agitator] (#238)

## 3.0.0a1 (2021-04-20)

### New features:

- Remove hero move to top from rules. [jensens] (hero)
- Change Templates to Bootstrap 5. [agitator, santonelli] (#137)
- Change to relative xml include path to make external includes
  possible [gomez] (#212)
- Add styling for comments. [santonelli] (#225)
- Update markup for document byline [santonelli] (#235) (#235)
- Use CSS class grid marker in body tag and Bootstrap mixins to
  define the grid, instead injecting them with Diazo. This will
  work even without Diazo and is more flexible. [MrTango] (#245)

### Bug fixes:

- Update `lodash` via @dependabot notification. [jensens] (#209)
- Cleanup code base:
  - Black code style,
  - Remove unnecessary code snippets, e.g. the magic utf8 header not
    needed in Python 3 and unused ZCML namespaces,
  - Remove skins.xml GS import step,
  - Remove unused less resource directory. (#229)
- Also leave `#edit-bar` intact when copying the toolbar html into the
  theme using backend.xml, as was fixed two years to in the normal
  rules.xml. [fredvd] (#3191)

## 2.1.6 (2019-10-21)

### Bug fixes:

- Revert "Fix the different width of Hide and Show button in action
  control panel" [vincentfretin] (#187)

## 2.1.5 (2019-10-12)

### Bug fixes:

- Load zcml of `plone.resource` for our use of the `plone:static`
  directive. [maurits] (#2952)

## 2.1.4 (2019-06-27)

### Bug fixes:

- Allow long photoAlbumEntryTitle entries to break to fit width.
  [agitator] (#183)

## 2.1.3 (2019-06-19)

### Bug fixes:

- Fix submenu width for long entries [agitator] (#182)

## 2.1.2 (2019-03-06)

### Bug fixes:

- Navigation style and overflow improvements [agitator] (#180)
- Further navigation style improvements - increase button touch area
  [agitator] (#181)

## 2.1.1 (2019-02-13)

### Bug fixes:

- Fix sitemap links (#173)
- Sitenav style improvements (#176)
- Fix overlapping css issue of Remove and Save button in pattern
  option of Resource Registries (#1111)

## 2.1.0 (2019-02-08)

### New features:

- Added styles for multilevel dropdown navigation [agitator] (#2516)

### Bug fixes:

- Fix the different width of Hide and Show button in action control
  panel (#2480)

## 2.0.0 (2019-01-15)

### Bug fixes:

- Make final release. [maurits] (#170)
- Initialize towncrier. [gforcada] (#2548)

## 2.0.0a1 (2018-11-05)

Breaking changes:

- Re-ordering of content columns: Have content container before
  column1 before column2. [tmassman]

### New features:

- Additional footer portlets show in a doormat footer. [tmassman]

## 1.9.1 (2018-10-08)

### Bug fixes:

- Do not strip the `#edit-bar` section from the toolbar. Refs:
  https://github.com/plone/Products.CMFPlone/issues/2322 [thet]

## 1.9.0 (2018-09-26)

### New features:

- Integrated plone.app.event styles and further cleanup. [agitator]

## 1.8.2 (2018-07-26)

### Bug fixes:

- Fix nested navigation tree and icon visibility [petschki]

## 1.8.1 (2018-04-08)

### Bug fixes:

- Fix missing colons in less variables [pnicolli]

## 1.8 (2018-02-05)

### New features:

- Pagination: made label and arrows easier to customise. [iham]

### Bug fixes:

- fix overlapping of images when portlets exist
  https://github.com/plone/Products.CMFPlone/issues/2179 [fgrcon]
- Fix horizontal scrollbar issue on some screen sizes. [agitator,
  davilima6]
- Remove duplicate definition of container size variables [agitator,
  davilima6]
- Added extra large & extra small break points [agitator, davilima6]

## 1.7.5 (2017-11-25)

### New features:

- Add more HTML text based input types. [thet]
- Fix disabled styles for readonly and disabled inputs, selects,
  textareas and fieldsets. [thet]
- Define variable `cursor-disabled` in variables.less for better
  reuse. [thet]
- Add theme classifier. [tmassman]

## 1.7.4 (2017-09-03)

Breaking changes:

- Simplify `contents.plone.less`. Contenttype icons now use the
  `::before` instead of `::after` pseudo element selector. [thet]

### New features:

- Do not use nested selectors for contenttype-icons, so that they can
  be shown anywhere, also outside the Plone main wrappers. Still use
  specific styles for the toolbar. This solves a problem, where
  contenttype-icons couldn't be shown in DOM nodes injected by
  JavaScript outside the main Plone wrapper. [thet]

### Bug fixes:

- Force state colors everywhere. Fixes #133. [thet]
- Limited printed data to page content only #139. [enkidulan]
- Fixed vertical align of nav items thumbs in navigation portlet
  #137. [enkidulan]
- Change `:before` and `:after` to `::before` and `::after` to follow
  CSS3 specs. [thet]

## 1.7.3 (2017-07-04)

### New features:

- Added Bootstrap-Dropdown default styles. [agitator]

## 1.7.2 (2017-07-03)

### New features:

- remove paperclip fontello icon for file types (is being replaced by
  mimetype icons) remove superfluous bullets in portlets ... fix icons
  in select default page pop up
  <https://github.com/plone/Products.CMFPlone/issues/1734> [fgrcon]

### Bug fixes:

- Fix position of checkboxes with long fieldhelp [agitator]

## 1.7.1 (2017-03-28)

### Bug fixes:

- Added styles for input type number. [agitator]

## 1.7 (2017-02-20)

### Bug fixes:

- Remove redundant PickADate rules. [thet]

## 1.6.23 (2017-01-02)

### Bug fixes:

- fix weird nav scrollbars on mobile [agitator]

## 1.6.22 (2016-11-09)

### New features:

- Add default content type icon to add menu only. Add missing npm
  dependency. [alecm]

### Bug fixes:

- Unset select width and display [agitator]
- Isolate the autotabs class for `ul` elements to
  `.autotabs ul.autotoc-nav`. Fixes an issue, where list elements in
  an inline TinyMCE content area were displayed wrong. [thet]
- Fix buttons alignment in ordered selection widget [ale-rt]

## 1.6.21 (2016-06-07)

### Bug fixes:

- Remove references to discarded offcanvas feature [davilima6]

## 1.6.20 (2016-05-25)

### Bug fixes:

- Set news lead image background for transparent images
  <https://github.com/plone/plonetheme.barceloneta/issues/107>
  [staeff]

## 1.6.19 (2016-05-15)

New:

- Add styles for manage portlets jumplist [davilima6]

Fixes:

- Use `.alert.status` selector as an alternative to `.portalMessage`.
  This class is used by the structure pattern. [thet]
- Make search button grow with the search buttons text. Fixes an issue
  where translated button texts were not fitting into the button.
  [kkhan, thet]

## 1.6.18 (2016-03-31)

New:

- Add missing caret styles. [thet]
- Extended form styles for input type="email". [agitator]
- Isolate calendar portlet styles. [agitator]
- Added invisible-grid table styles. [agitator]
- Action control panel specific rendering. [ebrehault]

Fixes:

- Improved "feel" for the Site Setup (@@overview-controlpanel)
  <https://github.com/plone/Products.CMFPlone/issues/1435>
  [pigeonflight]
- Fix code analysis errors reported by
  <http://jenkins.plone.org/view/Pkgs/job/package-plonetheme.barceloneta>
  [gforcada]
- Drop toolbar for anonymous users.
- Fixed html validation:
  - the banner role is unnecessary for element header,
  - element main does not need a role attribute,
  - the contentinfo role is unnecessary for element footer.
  [maurits]

## 1.6.17 (2016-02-27)

New:

- Modernize pagination markup and switches deprecated `listingBar` CSS
  class to `pagination`. [davilima6]

Fixes:

- Move hero to content Issue
  <https://github.com/plone/Products.CMFPlone/issues/974> [gyst]
- Add `barceloneta-mixin-font` to the registerless profile.
  [pcdummy]
- Inline `style` tags in head are no more skipped [keul]
- Follow best practice for readme.rst [allcaps]
- Center the leadimage on the modal window. Partially close
  [#321](https://github.com/plone/plone.app.contenttypes/issues/321).
  [keul]
- Fix filenames for roboto-lightitalic.ttf, -mediumitalic.ttd and
  -bolditalic.ttf to match those in less files [datakurre]

## 1.6.16 (2016-01-08)

Fixes:

- Add 2014 Roboto [allcaps]
- Fix @font-face. Load eot, svg and woff. [allcaps]
- Add Roboto fonts with full glyph set [allcaps]
- Add weight to all fonts (contributes to
  [#24](https://github.com/plone/plonetheme.barceloneta/issues/24)).
  [allcaps]
- Restore the principal aka jumbotron background. [allcaps]
- Fix sitemap layout. Drop the columns. (closes
  [#57](https://github.com/plone/plonetheme.barceloneta/issues/57)).
  [allcaps]
- Remove trailing comma's in Grunt file. [allcaps]
- Use border radius variables in portlets. [allcaps]
- Mismatched properties and values. [allcaps]
- Ignore diff of map file. [allcaps]

## 1.6.15 (2015-11-28)

Fixes:

- Fixed some css rules (missing clearfixes, aligning thumbs, ...).
  <https://github.com/plone/plonetheme.barceloneta/issues/62>
  [fgrcon]
- Added css-rules for thumbnails in listings and portlets. Related to
  [#1226](https://github.com/plone/Products.CMFPlone/issues/1226).
  [fgrcon]
- Underline links in #content-core (criterion 1.4.1). [polyester]
- Increased contrast, eliminated contrast-checker false positives.
  [polyester]
- Title under thumb in albumview (closes
  [#1091](https://github.com/plone/Products.CMFPlone/issues/1091)).
  [polyester]
- Don't include diazo bundle in backend theme. [instification]
- Discard duplicated ids for columns (closes
  [#1105](https://github.com/plone/Products.CMFPlone/issues/1105))
  [davilima6]
- Add comment to alert on duplicate resource registering [davilima6]

## 1.6.14 (2015-09-27)

- Fix in barceloneta word wrap in event listing. [sneridagh]

## 1.6.13 (2015-09-20)

- Add spaces between checks and labels in search filter (closes
  [#982](https://github.com/plone/Products.CMFPlone/issues/982)).
  [rodfersou]
- Center buttons on ordered selection lists (closes
  [#1017](https://github.com/plone/Products.CMFPlone/issues/1017)).
  [rodfersou]
- Center checkboxes on user/group matrix (closes
  [#1003](https://github.com/plone/Products.CMFPlone/issues/1003)).
  [rodfersou]
- Remove hero-element from index.html. Instead include a view @@hero.
  Fixes <https://github.com/plone/Products.CMFPlone/issues/974>
  [pbauer]
- Harmonize plone.app.discussion styles and discussion.plone.less
  styles refs (refs
  [#764](https://github.com/plone/Products.CMFPlone/issues/764))
  [ichim-david]
- Fix display of date widget arrows and footer buttons (refs
  [#891](https://github.com/plone/Products.CMFPlone/issues/891)).
  [ichim-david]
- Clean Gruntfile.js, package.json and HOWTO_DEVELOP.rst of grunt
  plugins and information which this package no longer uses since
  commit 9f5434 [ichim-david]
- provide basic table styles [vangheem]
- Fixed (refs
  [#979](https://github.com/plone/Products.CMFPlone/issues/979) and
  [#981](https://github.com/plone/Products.CMFPlone/issues/981))
  related to text not wrapping when unusual (and artificial) text with
  no white-space exists in the page [sneridagh]
- Fixed styling problems when figcaption is very long [sneridagh]
- Renamed the news.plone.less into behaviors.plone.less as it no
  longer make sense [sneridagh]

## 1.6.12 (2015-09-12)

- Fix display of album_view title links (closes
  [#911](https://github.com/plone/Products.CMFPlone/issues/911)).
  [ichim-david]

## 1.6.11 (2015-09-08)

- Bring back document byline (closes
  [#741](https://github.com/plone/Products.CMFPlone/issues/741)).
  [rodfersou]
- Prefer rules with CSS selectors over XPath whenever possible
  [davilima6]

## 1.6.10 (2015-09-07)

- Add a pared down version of barceloneta to include in your theme to
  save you making a custom backend theme. [djay]

## 1.6.9 (2015-08-22)

- Hide searchbox, personaltools, breadcrumbs in print.css [gomez]
- Updated font-weight on portlet headers [pigeonflight]
- Update font-weight on portlet management items [vangheem]
- Updated to index.html: link to plone.com opens in new window/tab
  [tkimnguyen]

## 1.6.8 (2015-07-18)

- New control panel overview and portlet layout. [sneridagh]
- Fixed bug in portlet navigation due to a CSS error. [sneridagh]
- Fix problem with CSS leaking from the cp overview to the portlet.
  [sneridagh]
- Fix map. [sneridagh]
- Added a:hover styles for h1 h2 h3. [agitator]
- Role for gigantic is complementary. [bloodbare]
- Do not use absolute prefix to reference index.html to copying themes
  does not reference original theme file. [vangheem]
- Toolbar fixes. [bloodbare]
- Various mobile fixes. [agitator]
- Update index.html. Change plone.org link to plone.com.
  [tkimnguyen]
- Do not uppercase the colophon. [gforcada]

## 1.6.7 (2015-06-05)

- provide more sane default widths and heights to select[multiple]
  and textareas [vangheem]
- hide crud-form select header by default [vangheem]
- remove loader since it is in mockup now [vangheem]
- tweak manage portlets styles [vangheem]
- fixed rules for copying content. [hvozdovych]

## 1.6.6 (2015-05-13)

- provide some spacing between event summary and content [vangheem]

## 1.6.5 (2015-05-05)

- Fix extending barceloneta with xi:include [pbauer]

## 1.6.4 (2015-05-04)

- fix in and out widget button style [vangheme]
- no one likes the star for required field label, try circle
  [vangheem]
- add plone-loader style so you can add decent loader to javascript
  [vangheem]
- add styles for search form [vangheem]
- Cleanup: Remove unused resources. [thet]
- Fix toggling navigation at mobile widths. [davisagli]
- Remove sticky footer (it required a hardcoded height, which does not
  work for an element that may have varying content). [davisagli]
- Add clearfix to `.row`. [davisagli]
- pat-modal pattern has been renamed to pat-plone-modal [jcbrand]

## 1.6.3 (2015-03-26)

- Add language selector widget [bloodbare]

## 1.6.2 (2015-03-21)

- Change font family of `form.widgets.IRichText.text` textareas to
  monospace. This affects the texteditor only in non-Richtext mode and
  helps editing e.g. Restructured Text. [thet]
- Change `min-height` of textarea fields from auto to `4em`
  (description, etc.), respectively `12em` for IRichText widgets (e.g.
  when displayed without a visual editor). [thet]
- Return to being a clean Diazo theme so that we are a safe starting
  point for people building their own themes and a good practice
  example that works when copying the theme in the TTW theme editor.
  [optilude, bloodbare]

## 1.6.1 (2014-11-01)

- Remind committers to add changelog entries. I'm not your monkey.
  [esteele]

## 1.6.0 (2014-04-20)

- Initial release [esteele]
