import pytest
from custom_components.opm_status.sensor import fetch_opm_status

def test_fetch_opm_status():
    """Test fetching OPM status."""
    status, posted_date, applicable_day = fetch_opm_status()
    assert status is not None
    assert posted_date is not None
    assert applicable_day is not None