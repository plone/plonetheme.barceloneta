from cgi import escape
from datetime import date
from urllib import unquote

from plone.memoize.view import memoize
from zope.component import getMultiAdapter
from zope.deprecation.deprecation import deprecate
from zope.i18n import translate
from zope.interface import implements, alsoProvides
from zope.viewlet.interfaces import IViewlet

from AccessControl import getSecurityManager
from Acquisition import aq_base, aq_inner

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.globals.interfaces import IViewView
from plone.app.layout.viewlets.common import ViewletBase


class HeroViewlet(ViewletBase):
    index = ViewPageTemplateFile('hero.pt')

    @property
    @memoize
    def page_title(self):
        '''
        Get the page title. If we are in the portal_factory we want use the
        "Add $FTI_TITLE" form (see #12117).

        NOTE: other implementative options can be:
         - to use "Untitled" instead of "Add" or
         - to check the isTemporary method of the edit view instead of the
           creation_flag
        '''
        if (hasattr(aq_base(self.context), 'isTemporary') and
                self.context.isTemporary()):
            # if we are in the portal_factory we want the page title to be
            # "Add fti title"
            portal_types = getToolByName(self.context, 'portal_types')
            fti = portal_types.getTypeInfo(self.context)
            return translate('heading_add_item',
                             domain='plone',
                             mapping={'itemtype': fti.Title()},
                             context=self.request,
                             default='Add ${itemtype}')

        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')
        return escape(safe_unicode(context_state.object_title()))

    def update(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        portal_title = escape(safe_unicode(portal_state
                                           .navigation_root_title()))
        if self.page_title == portal_title:
            self.site_title = portal_title
        else:
            self.site_title = u"%s &mdash; %s" % (self.page_title,
                                                  portal_title)
