import pytest
from main import app
import tmdb_client
from tmdb_client import call_tmdb_api
from unittest.mock import Mock

# To test other pages, input ('input page', 200)
@pytest.mark.parametrize('n, result', (
   ('top_rated', 200),
   ('upcoming', 200),
   ('popular', 200),
   ('now_playing', 200)
))

def test_homepage(monkeypatch, n, result):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')