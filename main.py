import requests
from credentials import *
from lichessApi import *
username = "Emanuele_FF"


def main():
    print(getProfile(token))
    print(getUserPublicData(username))
    print(getRatingHistory(username))
    print(getPerformanceStatistic(username,"bullet"))
    print(getTeamMembers(team_id))
    print(getCrosstable(username, "Alessio_PoliTO"))
    print(getDailyPuzzle())
    print(getUserDashboard(username,365))
    print(getTeamJoinRequest(token,team_id))
    print(getProfile(token))
    print(messageTeamMembers(token,team_id,"Ciao"))
    pass


if __name__ == "__main__":
    main()

