"""
Pushover platform for notify via glances - small notifications
for apple iWatch for example!

#
glances1:
  sequence:
    - service: notify.pushoverglances
      data_template:
        message: "Rst msg"
        title: "Rst ttl"
        data:
          count: "100"
          precent: "100"
          subtext: "Rst subtxt"
#
glances2:
  sequence:
    - service: notify.pushoverglances
      data_template:
        message: "{{states('sensor.amir_work_to_home')}}msg"
        title: "{{states('sensor.amir_work_to_home')}} ttl"
        data:
          count: "{{states('sensor.amir_work_to_home')}}"
          precent: "{{(states('sensor.amir_work_to_home' ) | int) * 2}}"
          subtext: "{{((states('sensor.amir_work_to_home' ) | int) * 3)}}"
#


"""

import logging
import http.client, urllib
import time
import datetime

from pushover_complete import PushoverAPI, BadAPIRequestError

from homeassistant.components.notify import (
    ATTR_DATA,
    ATTR_TITLE,
    BaseNotificationService,
)
from homeassistant.const import CONF_API_KEY
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import (
    ATTR_COUNT,
    ATTR_PERCENT,
    ATTR_SUBTEXT,
    CONF_USER_KEY,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)


async def async_get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
):
    """Get the Pushover notification service."""
    if discovery_info is None:
        return None
    pushover_api: PushoverAPI = hass.data[DOMAIN][discovery_info["entry_id"]]
    print(discovery_info)
    return PushoverGlanceService(
        hass, pushover_api, discovery_info[CONF_USER_KEY], discovery_info[CONF_API_KEY]
    )


class PushoverGlanceService(BaseNotificationService):
    """Implement the notification service for Pushover."""

    def __init__(
        self, hass: HomeAssistant, pushover: PushoverAPI, user_key: str, api_token: str
    ) -> None:
        """Initialize the service."""
        self._hass = hass
        self._user_key = user_key
        self._api_token = api_token
        self.pushover = pushover

    def send_message(self, message="", **kwargs):
        """Send a message to a user."""

        ts = time.time()
        rTimefull = datetime.datetime.fromtimestamp(ts).strftime("%H:%M")

        data = kwargs.get(ATTR_DATA)
        myTitle = kwargs.get(ATTR_TITLE, rTimefull)
        # Set connection for API
        conn = http.client.HTTPSConnection("api.pushover.net:443")

        urlbuilder = {"token": self._api_token}
        urlbuilder["user"] = self._user_key

        if myTitle:
            urlbuilder["title"] = myTitle

        if message != "":
            urlbuilder["text"] = str(message)
            _LOGGER.debug("message = %s", str(message))

        if data is not None and ATTR_COUNT in data:
            myCount = data.get(ATTR_COUNT, None)
            _LOGGER.debug("myCount = %s", str(myCount))
            urlbuilder["count"] = str(myCount).strip("''")

        if data is not None and ATTR_PERCENT in data:
            myPercent = data.get(ATTR_PERCENT, None)
            _LOGGER.debug("myPercent = %s", str(myPercent))
            urlbuilder["percent"] = str(myPercent).strip("''")

        if data is not None and ATTR_SUBTEXT in data:
            mySubText = data.get(ATTR_SUBTEXT, None)
            _LOGGER.debug("mySubText = %s", str(mySubText))
            urlbuilder["subtext"] = str(mySubText).strip("''")

        _LOGGER.debug("Building = %s", str(urlbuilder))
        conn.request(
            "POST",
            "/1/glances.json",
            urllib.parse.urlencode(urlbuilder),
            {"Content-type": "application/x-www-form-urlencoded"},
        )
        try:
            reponse = conn.getresponse()
            _LOGGER.debug("response = %s", str(reponse.read()))
            if reponse.status != 200:
                _LOGGER.error("Error sending pushover glances notification")
                raise BadAPIRequestError
            _LOGGER.debug("got it!")
        except ValueError as val_err:
            _LOGGER.error(str(val_err))
        except BadAPIRequestError:
            _LOGGER.exception("Could not send pushover glances notification")
