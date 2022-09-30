import requests
import pytest

# Verify correct HTTP status code
def test_weather_api_status_code():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Houston&appid=32d8a864a70fd4564c382f710c3c1f05")
    assert response.status_code == 200

def test_ipregistry_status_code():
    response = requests.get("https://api.ipregistry.co/?key=5l1j91plkayy43qd")
    assert response.status_code == 200

# Verify response payload
def test_value_exists():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Houston&appid=32d8a864a70fd4564c382f710c3c1f05")
    response_body = response.json()
    assert response_body["name"] == "Houston"

fields1 = [
    "weather",
    "main",
    "sys"
]

@pytest.mark.parametrize("f", fields1)
def test_field_weather_exists(f):
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Houston&appid=32d8a864a70fd4564c382f710c3c1f05")
    response_body = response.json()
    assert f in response_body

fields2 = [
    "temp",
    "temp_min",
    "temp_max",
    "pressure",
    "humidity"
]

@pytest.mark.parametrize("f", fields2)
def test_field_temp_exists(f):
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Houston&appid=32d8a864a70fd4564c382f710c3c1f05")
    response_body = response.json()
    assert f in response_body["main"]

fields3 = [
    "sunrise",
    "sunset"
]

@pytest.mark.parametrize("f", fields3)
def test_field_sunrise_exists(f):
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Houston&appid=32d8a864a70fd4564c382f710c3c1f05")
    response_body = response.json()
    assert f in response_body["sys"]

def test_field_location_exists():
    response = requests.get("https://api.ipregistry.co/?key=5l1j91plkayy43qd")
    response_body = response.json()
    assert "location" in response_body

def test_field_city_exists():
    response = requests.get("https://api.ipregistry.co/?key=5l1j91plkayy43qd")
    response_body = response.json()
    assert "city" in response_body["location"]

# Verify response headers
def test_weather_api_response_headers():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Houston&appid=32d8a864a70fd4564c382f710c3c1f05")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def test_ipregistry_api_response_headers():
    response = requests.get("https://api.ipregistry.co/?key=5l1j91plkayy43qd")
    assert response.headers["Content-Type"] == "application/json"