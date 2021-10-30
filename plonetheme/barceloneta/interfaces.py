from plone.theme.interfaces import IDefaultPloneLayer
from zope.deprecation import deprecated

@deprecated("Use IDefaultPloneLayer directly")
class IBarcelonetaLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer and a plone skin
    marker.
    """
