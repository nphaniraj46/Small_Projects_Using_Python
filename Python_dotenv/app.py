import os 
from dotenv import load_dotenv

load_dotenv() # this loads the data we have in this .env file to this program

Apikey=os.getenv('Openapikey')
db_password=os.getenv('dbpassword')

print(f'Loaded apikey {Apikey}')
print(f'Loaded dbpassword {db_password}')
