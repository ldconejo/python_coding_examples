from pytest import fixture

from bs4 import BeautifulSoup

import main

@fixture
def client():
    with main.app.test_client() as client:
        yield client

def test_add_get(client):
    rv = client.get('/add')
    soup = BeautifulSoup(rv.data, "html.parser")
    assert soup.head.title.text == "Calculator"

    assert len(soup.find_all("p")) == 2

    assert soup.find_all("input", type=True)[1]["type"] == "submit"