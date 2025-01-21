
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "--- add your mongodb atlas url ----"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
try:
    data = read_yaml_file(SCHEMA_FILE_PATH)
    print(len(data['numerical_columns']))

except Exception as e:
    print(e)

