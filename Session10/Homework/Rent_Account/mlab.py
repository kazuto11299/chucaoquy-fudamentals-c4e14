import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds161016.mlab.com:61016/rent_game_account

host = "ds161016.mlab.com"
port = 61016
db_name = "rent_game_account"
user_name = "admin"
password = "admin"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
