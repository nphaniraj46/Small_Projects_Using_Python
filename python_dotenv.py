import os 
from dotenv import load_dotenv

load_dotenv()

Apikey=os.getenv('Openapikey')
db_password=os.getenv('dbpassword')

print(f'Loaded apikey {Apikey}')
print(f'Loaded dbpassword {db_password}')