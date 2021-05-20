import pytest
import requests
import json

from pytest_bdd import scenarios, when, then

URL = "https://api-football-v1.p.rapidapi.com/v3/players"
HEADERS = {
            'x-rapidapi-key': "abe8b4c5d8msh9283322f2a4cbc8p1043f7jsnf567d5f51908",
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
        }

scenarios('../features/get_players.feature')

@pytest.fixture()
@when('the football api is queried with "<team>" and "<season>"')
def get_players(team, season):
    headers = HEADERS
    response = requests.get(URL + '?team=' + team + '&season=' + season, headers=headers)
    return response

@then('the response status code is 200')
def get_response_code(get_players):
    assert get_players.status_code == 200

@then('the response shows the "<players>" which are part of the team')
def get_players_data(get_players, players):
    data = get_players.json()
    players_data = {}
    players = players.replace("\'", "\"")
    players = json.loads(players)
    for player in data['response']:
        players_data[player['player']['name']] = player['player']['photo']
    for key in players_data:
        assert players_data[key] == players[key]