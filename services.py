import json

def get_client_data():
    with open('./data/client.json') as f:
        return json.load(f)

def get_achievements_data():
    with open('./data/whyus.json') as f:
        return json.load(f) 

def get_location_data():
    with open('./data/map.json') as f:
        return json.load(f) 

def get_services_data():
    with open('./data/services.json') as f:
        return json.load(f)  