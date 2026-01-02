import requests
import pytest

# This is a 'fixture' - it provides the base URL so you don't repeat it
@pytest.fixture
def base_url():
    return "https://pokeapi.co/api/v2/pokemon/"

def test_pikachu_data_is_correct(base_url):
    # 1. Act: Search for 'pikachu'
    response = requests.get(f"{base_url}pikachu")
    data = response.json()
    # 2. Assert: Check response status
    assert response.status_code == 200
    # 3. Assert: Validate specific data points
    assert data["name"] == "pikachu"
    assert data["id"] == 25
    # Validate neseted data: Check if 'electric' is in the types list
    types = [t["type"]["name"] for t in data["types"]]
    assert "electric" in types
def test_invalid_pokemon_returns_404(base_url):
    # Act: Search for something that doesn't exist
    response = requests.get(f"{base_url}non-existent-pokemon")
    # Assert: Should return a 404 Not Found
    assert response.status_code == 404
@pytest.mark.parametrize("pokemon_name, expected_id", [
    ("bulbasaur", 1),
    ("charmander", 4),
    ("squirtle", 7),
    ("mew", 151)
])
def test_multiple_pokemon_ids(base_url, pokemon_name, expected_id):
    response = requests.get(f"{base_url}{pokemon_name}")
    assert response.status_code == 200
    assert response.json()["id"] == expected_id         