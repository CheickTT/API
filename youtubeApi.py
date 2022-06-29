import requests
from pyyoutube import Api
import pprint

api = Api(api_key='AIzaSyCfnmdQQ8Fmglivkngk4KgXY18Ftb6Y7pI')#AIzaSyCfnmdQQ8Fmglivkngk4KgXY18Ftb6Y7pI
channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(channel_by_id.items[0].to_dict())