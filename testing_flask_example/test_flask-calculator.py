'''
Flask Calculator testing example
ldconejo, with code from: https://flask.palletsprojects.com/en/1.1.x/testing/
'''

import flask
import pytest

import main

@pytest.fixture
def client():
    '''
    This is the client fixture that Pytest will use
    to test our code
    '''
    with main.app.test_client() as client:
        yield client

def test_add_get(client):
    '''
    Shows a basic GET operation
    asserting the entire HTML string
    '''
    # Note that get() is really the GET method
    rv = client.get('/add')
    # This is a REALLY long line, probably not the best idea
    # the line was captured using the -s option in Pytest
    expected = b'<html>\n<head>\n<title>Calculator</title>\n</head>\n<body>\n    <a id="add" href="/add">Add numbers</a>\n    <a id="retrieve" href="/retrieve">Retrieve a total</a>\n    <h1>Calculator</h1>\n    <h2>Add them up!</h2>\n    \n    <!--p>Total: <span id="total">FILL ME</span></p-->\n    <p>Total: <span id="total">0</span></p>\n    <form method="POST">\n        <label for="number">Number: </label><input type="number" id="number" name="number">\n        <input type="submit" value="Add It!">\n    </form>\n    <!-- Add this for saving progress-->\n    <form method="POST" action="/save">\n        <input type="submit" value="Save It!">\n    </form>\n\n</body>\n</html>'
    assert expected in rv.data

def test_add_post_simple(client):
    rv = client.post('/add', data=dict(number="3"))
    expected = b'<p>Total: <span id="total">3</span></p>\n'
    assert expected in rv.data

def test_add_post_with_session(client):
    '''
    Showcases accessing and modifying a session during testing
    '''
    with main.app.test_client() as c:
        with c.session_transaction() as sess:
            sess['total'] = 10
        rv = c.post('/add', data=dict(number="3"))
        assert flask.session['total'] == 13
