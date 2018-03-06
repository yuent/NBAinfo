import bs4, requests

def getNBAscores():
    res = requests.get('http://www.espn.com/nba/scoreboard')
    soup = bs4.BeautifulSoup(res.text)
    allScores = soup.find_all('div', class_='scoreboards')
    print(allScores)

getNBAscores()
