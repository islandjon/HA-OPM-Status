import requests
from datetime import datetime, timedelta
from homeassistant.helpers.entity import Entity
from homeassistant.util import dt as dt_util

OPM_STATUS_URL = "https://www.opm.gov/policy-data-oversight/snow-dismissal-procedures/current-status/"

def fetch_opm_status():
    """Fetch the OPM status from the website."""
    response = requests.get(OPM_STATUS_URL)
    response.raise_for_status()
    # Parse the response to extract the status, posted date/time, and applicable day
    # This is a placeholder for the actual parsing logic
    status = "Open"
    posted_date = datetime.now()
    applicable_day = datetime.now() + timedelta(days=1)
    return status, posted_date, applicable_day

class OPMStatusSensor(Entity):
    """Representation of an OPM Status Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None
        self._status = None
        self._posted_date = None
        self._applicable_day = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return "OPM Status"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "status": self._status,
            "posted_date": self._posted_date,
            "applicable_day": self._applicable_day,
        }

    def update(self):
        """Fetch new state data for the sensor."""
        self._status, self._posted_date, self._applicable_day = fetch_opm_status()
        self._state = self._status