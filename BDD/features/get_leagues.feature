Feature: Get Leagues of which the specified team is a part of
  A football team usually participates in a large number of competitions,
  as a fan, I would like to know which competitions my team is a part of


  Scenario Outline: Football leagues the team is a part of
    When the football api is queried with "<team>"
    Then the response status code is 200
    And the response shows the "<leagues>" the team is a part of

    Examples: Leagues
    | team | leagues |
    |  33  | {'Community Shield': 'https://media.api-sports.io/football/leagues/528.png','FA Cup': 'https://media.api-sports.io/football/leagues/45.png','International Champions Cup': 'https://media.api-sports.io/football/leagues/26.png','League Cup': 'https://media.api-sports.io/football/leagues/48.png','Premier League': 'https://media.api-sports.io/football/leagues/39.png','UEFA Champions League': 'https://media.api-sports.io/football/leagues/2.png','UEFA Europa League': 'https://media.api-sports.io/football/leagues/3.png','UEFA Super Cup': 'https://media.api-sports.io/football/leagues/531.png'} |
    | 100  | {'Coupe de France': 'https://media.api-sports.io/football/leagues/66.png','Coupe de la Ligue': 'https://media.api-sports.io/football/leagues/65.png','Ligue 1': 'https://media.api-sports.io/football/leagues/61.png','Ligue 2': 'https://media.api-sports.io/football/leagues/62.png','National': 'https://media.api-sports.io/football/leagues/63.png','National 2 - Group B': 'https://media.api-sports.io/football/leagues/68.png'} |
    |   2  | {'Euro Championship': 'https://media.api-sports.io/football/leagues/4.png','Friendlies': 'https://media.api-sports.io/football/leagues/10.png','UEFA Nations League': 'https://media.api-sports.io/football/leagues/5.png','World Cup': 'https://media.api-sports.io/football/leagues/1.png','World Cup - Qualification Europe': 'https://media.api-sports.io/football/leagues/32.png'} |