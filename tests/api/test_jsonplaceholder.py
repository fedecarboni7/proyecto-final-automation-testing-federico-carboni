import pytest
import requests
from utils.logger import get_logger

BASE_URL = "https://jsonplaceholder.typicode.com"
logger = get_logger("api_tests")


@pytest.mark.api
def test_get_post_by_id():
    """Verify that GET /posts/1 returns a single post with the expected keys and id."""
    endpoint = f"{BASE_URL}/posts/1"
    logger.info(f"GET {endpoint}")
    response = requests.get(endpoint)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, dict)
    expected_keys = {"id", "userId", "title", "body"}
    assert expected_keys.issubset(json_data.keys())
    assert json_data["id"] == 1


@pytest.mark.api
def test_get_all_posts():
    """Verify that GET /posts returns a list of exactly 100 posts."""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100
    assert "id" in posts[0]


@pytest.mark.api
def test_create_post():
    """Verify that POST /posts creates a new post and returns it with an assigned id."""
    payload = {"title": "Test Post", "body": "This is a test", "userId": 1}
    logger.info(f"Creating post with payload: {payload}")
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == payload["title"]
    assert json_data["body"] == payload["body"]
    assert json_data["userId"] == payload["userId"]
    assert "id" in json_data


@pytest.mark.api
def test_delete_post():
    """Verify that DELETE /posts/1 returns status 200 and an empty object."""
    post_id = 1
    logger.info(f"Deleting post with id: {post_id}")
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json() == {}


@pytest.mark.api
def test_get_posts_by_user_chained():
    """Test encadenado: obtiene el primer usuario y luego busca sus posts."""
    user_response = requests.get(f"{BASE_URL}/users")
    users = user_response.json()
    first_user = users[0]
    user_id = first_user["id"]
    logger.info(f"Obtained userId: {user_id}")
    assert "id" in first_user

    posts_response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    assert posts_response.status_code == 200
    posts = posts_response.json()
    assert isinstance(posts, list)
    assert len(posts) >= 1
    assert all(post["userId"] == user_id for post in posts)
