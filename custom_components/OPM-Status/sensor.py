"""Sensor platform for OPM Status."""
from __future__ import annotations

import logging
import requests
from bs4 import BeautifulSoup
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME

from .const import DOMAIN, DEFAULT_NAME

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(minutes=15)  # Adjust update interval as needed

URL = "https://www.opm.gov/policy-data-oversight/snow-dismissal-procedures/current-status/"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up the OPM Status sensor from a config entry."""
    coordinator = OPMStatusCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([OPMStatusSensor(coordinator, entry)])


class OPMStatusCoordinator(DataUpdateCoordinator):
    """Class to manage fetching OPM status data."""

    def __init__(self, hass: HomeAssistant):
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name="OPM Status",
            update_interval=SCAN_INTERVAL,
        )

    async def _async_update_data(self):
        """Fetch data from the OPM website."""
        try:
            response = requests.get(URL)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            status = soup.select_one("div.page-content h2").text.strip()
            posted_date = (
                soup.find("p", string=lambda s: "Posted" in s).text.split("Posted")[1].strip()
            )
            applies_date = (
                soup.find("p", string=lambda s: "Applies" in s).text.split("Applies")[1].strip()
            )
            return {
                "status": status,
                "posted_date": posted_date,
                "applies_date": applies_date,
            }
        except Exception as err:
            raise UpdateFailed(f"Error fetching OPM status data: {err}") from err


class OPMStatusSensor(CoordinatorEntity, SensorEntity):
    """Representation of an OPM Status sensor."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: OPMStatusCoordinator, config_entry: ConfigEntry):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._config_entry = config_entry
        self._attr_unique_id = f"{DOMAIN}_status"
        self._attr_name = config_entry.data.get(CONF_NAME, DEFAULT_NAME)

    @property
    def native_value(self):
        """Return the current OPM status."""
        return self.coordinator.data["status"]

    @property
    def extra_state_attributes(self):
        """Return additional attributes."""
        return {
            "posted_date": self.coordinator.data["posted_date"],
            "applies_date": self.coordinator.data["applies_date"],
        }
