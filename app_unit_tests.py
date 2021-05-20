from unittest import TestCase
from app import get_headers, get_leagues, get_league_query, get_players, get_players_query

class TestApp(TestCase):
    def test_get_headers(self):
        actual_headers = {
            'x-rapidapi-key': "abe8b4c5d8msh9283322f2a4cbc8p1043f7jsnf567d5f51908",
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
        }
        headers = get_headers()
        assert headers == actual_headers

    def test_get_league_query(self):
        actual_league_query = {"team": "33"}
        league_query = get_league_query("33")
        assert league_query == actual_league_query

    def test_incorrect_get_league_query(self):
        with self.assertRaises(Exception) as context:
            get_league_query("test_team")
        self.assertTrue("team has to be a number" in str(context.exception))

    def test_get_players_query(self):
        actual_players_query = {"team": "33", "season": "2020"}
        players_query = get_players_query("33", "2020")
        assert players_query == actual_players_query

    def test_incorrect_team_players_query(self):
        with self.assertRaises(Exception) as context:
            get_players_query("test_team", "2020")
        self.assertTrue("team has to be a number" in str(context.exception))

    def test_incorrect_season_players_query(self):
        with self.assertRaises(Exception) as context:
            get_players_query("33", "test_season")
        self.assertTrue("season has to be a number greater than 1994 or less than 2021" in str(context.exception))

    def test_incorrect_number_season_players_query(self):
        with self.assertRaises(Exception) as context:
            get_players_query("33", "1990")
        self.assertTrue("season has to greater than 1994 or less than 2021" in str(context.exception))