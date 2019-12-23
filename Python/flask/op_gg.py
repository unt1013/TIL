from flask import Flask, render_template, request, escape
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/op_gg")
def op_gg():
    username = request.args.get('userName')

    url = f"https://www.op.gg/summoner/userName={username}" 

    req = requests.get(url).text
    data = BeautifulSoup(req, 'html.parser')

    userTier = data.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank").text
    userScore = data.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.LeaguePoints").text
    userWin = data.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins").text
    friendlyUser = data.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.SummonersMostGame.Box > div.Content > table > tbody > tr:nth-child(1) > td.SummonerName.Cell.left_select_played_with_summoner > a").text

    return render_template('op_gg.html', username = username, userTier = userTier, userScore = userScore, userWin = userWin, friendlyUser = friendlyUser)

if __name__ == "__main__" :
    app.run(debug=True)