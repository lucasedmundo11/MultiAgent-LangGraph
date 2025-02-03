import pytest
from flask import Flask
from app import app

"""
This module contains unit tests for the Flask application.
It uses pytest fixtures to create a test client for the app and 
includes tests for various API endpoints to ensure they return 
the expected responses.
"""

@pytest.fixture
def client():
    """Fixture to provide a test client for the Flask app."""
    with app.test_client() as client:
        yield client

# Test case to check the API success response
def test_api_success(client):
    response = client.post("/api", json={"message": "Test message"})
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert "response" in data

# Test case to check the API response when data is missing
def test_api_missing_data(client):
    response = client.post("/api", json={})
    assert response.status_code == 400

# Test case to check the API response when data format is invalid
def test_api_invalid_data_format(client):
    response = client.post("/api", data="Invalid data format")
    assert response.status_code == 400