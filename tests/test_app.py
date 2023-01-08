import requests
import pytest

def test_missing_keys_in_json():
    r = requests.post(
        "http://10.0.0.197:8000/score",
        json={"some-key":"some-value"})
    assert r.ok is False

def test_bad_values_in_json():
    r = requests.post(
        "http://10.0.0.197:8000/score",
        json={"x1":"5","x2":4})
    assert r.ok is False

def test_good_input():
    r = requests.post(
        "http://10.0.0.197:8000/score",
        json={"x1":5,"x2":4})
    assert r.json()["sum"] == 9
