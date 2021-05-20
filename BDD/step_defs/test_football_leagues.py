import pytest
import requests
import json

from pytest_bdd import scenarios, when, then

URL = "https://api-football-v1.p.rapidapi.com/v3/leagues"
HEADERS = {
            'x-rapidapi-key': "abe8b4c5d8msh9283322f2a4cbc8p1043f7jsnf567d5f51908",
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
        }

scenarios('../features/get_leagues.feature')
@pytest.fixture()
@when('the football api is queried with "<team>"')
def get_leagues(team):
    headers = HEADERS
    response = requests.get(URL + '?team=' + team, headers=headers)
    return response


@then('the response status code is 200')
def get_response_code(get_leagues):
    assert get_leagues.status_code == 200


@then('the response shows the "<leagues>" the team is a part of')
def get_response_data(get_leagues, leagues):
    data = get_leagues.json()
    league_data = data['response']
    leagues_data = {}
    leagues = leagues.replace("\'", "\"")
    leagues = json.loads(leagues)
    for league in league_data:
        leagues_data[league['league']['name']] = league['league']['logo']
    for key in leagues_data:
        assert leagues_data[key] == leagues[key]
