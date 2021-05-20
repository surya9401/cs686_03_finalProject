import time
import os
from flask import Flask, request, render_template, url_for, flash, redirect
import requests
import json

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = "Secret Key"

@app.route('/')
def hello():
    print('Welcome to our final Project')

@app.route('/leagues', methods=['GET'])
def get_leagues():
    team = request.args.get('team')
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
    querystring = get_league_query(team)
    headers = get_headers()
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    leagues = data['response']
    leagues_data = {}
    for league in leagues:
        leagues_data[league['league']['name']] = league['league']['logo']
    return render_template('index.html', value=leagues_data)


@app.route('/players', methods=['GET'])
def get_players():
    team = request.args.get('team')
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    querystring = get_players_query(team, "2020")
    headers = get_headers()
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    players = {}
    for player in data['response']:
        players[player['player']['name']] = player['player']['photo']
    return render_template('index.html', value=players)


def get_headers():
    headers = {
        'x-rapidapi-key': "abe8b4c5d8msh9283322f2a4cbc8p1043f7jsnf567d5f51908",
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }
    return headers


def get_league_query(team):
    # add validation condition for team
    try:
        int(team)
    except:
        raise Exception("team has to be a number")
    return {"team": team}


def get_players_query(team, season):
    # add some validation conditions for team and season
    try:
        int(team)
    except:
        raise Exception("team has to be a number")

    try:
        int(season)
    except:
        raise Exception("season has to be a number greater than 1994 or less than 2021")

    if int(season) < 1994 or int(season) > 2020:
        raise Exception("season has to greater than 1994 or less than 2021")
    return {"team": team, "season": season}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
