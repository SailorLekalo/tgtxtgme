import csv


class player:
    def __init__(self,id, nickname,level,health_points,status,infight):
        self.id = id
        self.level = level
        self.nickname = nickname
        self.health_points = health_points
        self.status = status
        self.infight = infight

def FindPlayerById(id):
    with open('test_players.csv', newline='') as player_database:
        players = csv.reader(player_database, delimiter=',')
        for row in players:
            if(str(row[0])==str(id)):
                return player(row[0],row[1],row[2],row[3],row[4],row[5])

def SaveCondition(player):
    with open('test_players.csv', newline='') as player_database:
        players = csv.reader(player_database, delimiter=',')
        new_base = []
        for row in players:
            if(str(row[0])==str(player.id)):
                row[0],row[1],row[2],row[3],row[4],row[5] = player.id,\
                                                            player.nickname,\
                                                            player.level,\
                                                            player.health_points,\
                                                            player.status,\
                                                            player.infight
            new_base.append(row)
    with open('test_players.csv', 'w', newline='') as player_database:
        writer = csv.writer(player_database,delimiter=',')
        writer.writerows(new_base)

