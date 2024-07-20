from os import listdir, getcwd, path
import json

'''
        I just reused a past json read/writter i made, it would probably be easier if I used a txt 
        since its just one thing I want to save but later in the proejct I could want to change this.
'''

def read_data():
    if not path.exists("default.json"):
        
        default_data = {"voice":listdir(f"{getcwd()}/media/audio/")[0]}
        
        write_data(default_data)

    with open("default.json", "r") as read_file:
        data = json.load(read_file)

    return data

def write_data(data=None):
    if data:
        data = data

    with open("default.json", "w") as write_file:
        json.dump(data, write_file, indent=4)