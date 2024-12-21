"""Constants for Push Over Glances."""

from typing import Final

DOMAIN = "pushoverglances"
PLATFORMS = [
    Platform.NOTIFY
]

CONFIG_ENTRY_VERSION = 1
DATA_HASS_CONFIG: Final = "pushover_hass_config"
DEFAULT_NAME: Final = "Pushover Glances"

ATTR_COUNT = 'count'
ATTR_PERCENT = 'percent'
ATTR_SUBTEXT = 'subtext'

CONF_USER_KEY: Final = "user_key"