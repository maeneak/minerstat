"""Constants for Minerstat."""
# Base component constants
NAME = "Minerstat"
DOMAIN = "minerstat"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"

ATTRIBUTION = "Data provided by https://minerstat.com/"
ISSUE_URL = "https://github.com/maeneak/minerstat/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [SENSOR]

MS_INFO = "info"
MS_HARDWARE = "hardware"

# Configuration and options
CONF_ENABLED = "enabled"
CONF_ACCESSCODE = "accesscode"
CONF_APIKEY = "apikey"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
