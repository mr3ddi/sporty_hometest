import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestJsonPlaceholderAPI:

    def test_get_single_post(self):

        post_id = 1
        url = f"{BASE_URL}/posts/{post_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["id"] == post_id
        assert "title" in data
        assert "body" in data
        assert "application/json" in response.headers["Content-Type"]

    def test_get_non_existent_resource(self):
        invalid_id = 999999
        url = f"{BASE_URL}/posts/{invalid_id}"

        response = requests.get(url)

        assert response.status_code == 404
        assert response.json() == {}

    def test_create_post(self):
        url = f"{BASE_URL}/posts"
        payload = {
            "title": "Matt",
            "body": "Janusz",
            "userId": 33
        }

        response = requests.post(url, json=payload)
        assert response.status_code == 201

        data = response.json()
        print(data)
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert "id" in data

    @pytest.mark.parametrize("user_id, expected_name", [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch")
    ])
    def test_get_users_parametrized(self, user_id, expected_name):

        url = f"{BASE_URL}/users/{user_id}"

        response = requests.get(url)

        assert response.status_code == 200
        data = response.json()

        assert data["id"] == user_id
        assert data["name"] == expected_name