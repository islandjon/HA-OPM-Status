# OPM Status Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/docs/faq/custom_repositories)

The **OPM Status Integration** fetches the current reporting status, post date, and applicable date from the [U.S. Office of Personnel Management (OPM)](https://www.opm.gov/policy-data-oversight/snow-dismissal-procedures/current-status/). This integration is especially useful for federal employees to stay updated on office closures, delays, or telework requirements during inclement weather or other events.

---

## Features
- Retrieves the current OPM status.
- Captures the posted date and the day the status applies to.
- Automatically updates in Home Assistant.

---

## Installation

### Via [HACS](https://hacs.xyz/)
1. Open HACS in Home Assistant.
2. Go to **Integrations**.
3. Click the three dots in the top-right corner and select **Custom repositories**.
4. Add this repository URL: `https://github.com/islandjon/HA-OPM-Status`.
5. Select **Integration** as the category and click **Add**.
6. Find **OPM Status** in the HACS integrations list and install it.

### Manual Installation
1. Download the latest release from this repository.
2. Extract the `opm_status` folder to your `custom_components` directory inside your Home Assistant configuration folder:
   ```
   custom_components/opm_status/
   ```
3. Restart Home Assistant.

---

## Configuration

1. After installation, restart Home Assistant.
2. Add the following to your `configuration.yaml` file:
   ```yaml
   sensor:
     - platform: opm_status
   ```
3. Restart Home Assistant again.

---

## Available Sensors
This integration provides the following sensors:

| Sensor Name            | Description                                  |
|-------------------------|----------------------------------------------|
| `sensor.opm_status`     | Current reporting status (e.g., "Open")     |
| `sensor.opm_posted_date` | The date and time the status was posted.    |
| `sensor.opm_applies_date`| The day the status applies to.             |

### Example
```yaml
sensor:
  - platform: opm_status
```

### Lovelace Example
You can display the data using a card in your Home Assistant dashboard:
```yaml
type: entities
entities:
  - entity: sensor.opm_status
    name: Current Status
  - entity: sensor.opm_posted_date
    name: Posted Date
  - entity: sensor.opm_applies_date
    name: Applies To
```

---

## Contributing
Contributions are welcome! If you find a bug or have a feature request, feel free to [open an issue](https://github.com/islandjon/HA-OPM-Status/issues) or submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support
If you encounter issues or have questions, please reach out via the [GitHub repository](https://github.com/islandjon/HA-OPM-Status).
```
