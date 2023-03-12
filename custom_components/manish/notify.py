import logging
from manish import MaNish
from manish.template import *
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.notify import (
    ATTR_TARGET, ATTR_TITLE, PLATFORM_SCHEMA, BaseNotificationService)

ATTR_PHONE_ID = "phone_number_id"
ATTR_TOKEN = "token"
ATTR_TEMPLATE = "template"
ATTR_LANGUAGE= "language"

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(ATTR_TARGET): cv.string,
    vol.Required(ATTR_PHONE_ID): cv.string,
    vol.Required(ATTR_TOKEN): cv.string,
    vol.Required(ATTR_TEMPLATE): cv.string,
    vol.Required(ATTR_LANGUAGE): cv.string,
    vol.Optional(ATTR_TITLE): cv.string,
})

def get_service(hass, config, discovery_info=None):
    """Get the custom notifier service."""
    target = config.get(ATTR_TARGET)
    title = config.get(ATTR_TITLE)
    token = config.get(ATTR_TOKEN)
    phone_number_id = config.get(ATTR_PHONE_ID)
    template = config.get(ATTR_TEMPLATE)
    language = config.get(ATTR_LANGUAGE)


    return ManishNotificationService(target, title, token, phone_number_id, template, language)

class ManishNotificationService(BaseNotificationService):
    
    def __init__(self, target, title, token, phone_number_id, template, language):
        """Initialize the service."""
        self._targets = target.split(',')
        self._title = title
        self._token = token
        self._phone_number_id = phone_number_id
        self._template = template
        self._language = language
        self._manish = MaNish(self._token,self._phone_number_id)

    def send_message(self, message="", **kwargs):
        """Send a message to the target."""
        try:
            for target in self._targets:
                _LOGGER.info("Sending message to %s: %s", target, message)
                body = Component(type="body",parameters=[Parameter(type="text",text = message)])
                result = self._manish.send_template(components=TemplateEncoder().encode([body]),recipient_id=target,template=self._template,lang=self._language)
                _LOGGER.warning("Whatsapp: " + str(result))
        except Exception as e:
            _LOGGER.error("Sending message to %s: %s has failed with the following error %s", self._target, message, str(e))