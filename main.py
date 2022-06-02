import requests
from credentials import *
from lichessApi import *
username = "Emanuele_FF"


def testing():
    # print(getRealTimeUserStatus())
    print(getUserPublicData(username))
    print(getRatingHistory(username))
    print(getPerformanceStatistic(username,"bullet"))
    print(getTeamMembers(team_id))
    print(getCrosstable(username, "Alessio_PoliTO"))
    print(getUsers([username,"Alessio_PoliTO"]))
    print(getDailyPuzzle())
    print(getUserDashboard(username,365))
    print(getTeamJoinRequest(token,team_id))
    print(messageTeamMembers(token,team_id,"Ciao"))
    print(getProfile(token))


def main():
    testing()
    pass


if __name__ == "__main__":
    print(token)
    main()

