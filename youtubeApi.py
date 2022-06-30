import requests
from pyyoutube import Api
import sqlalchemy as db
import pandas as pd

"""This function create a dictionnary from a channel id
Test: check that a dictionnary is correctly returned from the function"""
def get_channel_dic(id):
    if(isinstance(id, str) is False):
        return 'The entered id is not valid. Id must be a string.'
    api = Api(api_key = 'AIzaSyCfnmdQQ8Fmglivkngk4KgXY18Ftb6Y7pI')
    channel_by_id = api.get_channel_info(channel_id = id )
    channel = channel_by_id.items[0].to_dict()
    return channel

"""This function returns a dictionnary with the title, url and creation date of the channel
Test: check that the function correctly returns a dictionnary with the title, url and creation date of the channel"""
def get_info(channel):
    channel = channel['snippet']
    return {'title' : channel['title'], 'customUrl' : channel['customUrl'], 'pubDate' : channel['publishedAt']}

#This function store the information in a database
#Test: printing out the data from the database after storing them
def store_channel_info(channel_dict,engine):
    df = pd.DataFrame.from_dict([channel_dict])
    df.to_sql('channel', con=engine, if_exists = 'replace', index = False)

channel = get_channel_dic("UCtJ3xivtW_ZxG0sOBz8HtyA")
channel_info = get_info(channel)
engine = db.create_engine('sqlite:///my_db.db)
store_channel_info(channel_info, engine)
result = engine.execute('SELECT * FROM channel;').fetchall()
print(pd.DataFrame(result))