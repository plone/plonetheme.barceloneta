from plone.app.theming import utils as theme_utils

import logging


logger = logging.getLogger(__name__)


def reload_theme(context):
    # Reload theme to add ajax_load theme parameter.
    if theme_utils.getCurrentTheme() == "barceloneta":
        theme = theme_utils.getTheme("barceloneta")
        theme_utils.applyTheme(theme)
        logger.info("Reloaded Barceloneta.")
