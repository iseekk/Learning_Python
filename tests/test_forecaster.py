import pytest
import forecaster
import mock

PARAMETERS_TO_TEST = [
    ("rising", "It is going to rain"),
    ("falling", "Looks clear"),
]


@pytest.fixture()
def mock_ws():
    return mock.Mock()


@pytest.mark.parametrize("reading,expected", PARAMETERS_TO_TEST)
def test_forecaster1_reading(mock_ws, reading, expected):
    fc = forecaster.Forecaster1(mock_ws)
    mock_ws.barometer.return_value = reading
    assert fc.forecast() == expected


@pytest.mark.parametrize("reading,expected", PARAMETERS_TO_TEST)
def test_forecaster2_reading(monkeypatch, mock_ws, reading, expected):
    mock_ws.return_value = mock_ws
    mock_ws.barometer.return_value = reading
    monkeypatch.setattr(forecaster, "WeatherService", mock_ws)
    fc = forecaster.Forecaster2()
    assert fc.forecast() == expected


@pytest.mark.parametrize("reading,expected", PARAMETERS_TO_TEST)
def test_forecaster3_reading(monkeypatch, mock_ws, reading, expected):
    fc = forecaster.Forecaster3()
    monkeypatch.setattr(fc, "barometer", mock_ws)
    mock_ws.return_value = reading
    assert fc.forecast() == expected


@pytest.mark.parametrize("reading,expected", PARAMETERS_TO_TEST)
@mock.patch.object(forecaster.Forecaster3, "barometer")
def test_forecaster4_reading(mock_barometer, reading, expected):
    fc = forecaster.Forecaster3()
    mock_barometer.return_value = reading
    assert fc.forecast() == expected

