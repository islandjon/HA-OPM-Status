import requests
from bs4 import BeautifulSoup
from homeassistant.helpers.entity import Entity

URL = "https://www.opm.gov/policy-data-oversight/snow-dismissal-procedures/current-status/"

def fetch_opm_status():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    status = soup.select_one("div.page-content h2").text.strip()
    posted_date = soup.find("p", string=lambda s: "Posted" in s).text.split("Posted")[1].strip()
    applies_date = soup.find("p", string=lambda s: "Applies" in s).text.split("Applies")[1].strip()
    return status, posted_date, applies_date

async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([OPMStatusSensor()])

class OPMStatusSensor(Entity):
    def __init__(self):
        self._name = "OPM Status"
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    def update(self):
        status, posted_date, applies_date = fetch_opm_status()
        self._state = status
        self._attributes = {
            "posted_date": posted_date,
            "applies_date": applies_date
        }
