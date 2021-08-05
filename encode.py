import requests as rq
"""
This could be use as backend
"""

ip = '78.108.216.58'
maxplayers = 64
resp = rq.get('http://' + ip + ':30120/players.json').json()

def main():
    def showplayers():
        players = str(len(resp))
        print('------------------------')
        print('Players: ' + players + '/' + str(maxplayers))
        print('------------------------')
    def playerinfo():
        json = rq.get('http://' + ip + ':30120/players.json')
        result = ''
        id = 18 #It doesn't matter where the ID comes from (maybe as input :D)
        for _ in json.json():
            if _['id'] == int(id):
                print('------------------------\nPLAYERINFO')
                identifiers = str(_['identifiers'])[2:-1]
                komma = identifiers.find(',')
                steamid = str(_['identifiers'])[2:komma + 1]
                #print(steamid)
                result += str('Steamname: ' + _['name'] + '\nID: ' + str(id) + '\nPing: ' + str(_['ping']) + 'ms' + '\nSteamid: ' + str(steamid))
                print(result)
                print('------------------------')

        else:  
            pass
    def status():
        emoji = ''
        request = rq.get('http://ip-api.com/json/' + ip).json()
        if request['status'] == 'fail':
            emoji = "offline"
        emoji = "online"
        print('------------------------')
        print('Serverstatus: ' + emoji)
        print('------------------------')
    status()
    playerinfo()
    showplayers()


if __name__ == '__main__':
    main()