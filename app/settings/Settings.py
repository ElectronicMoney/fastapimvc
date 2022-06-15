from dotenv import dotenv_values
# The function dotenv_values works more or less the same way as 
# load_dotenv, except it doesn't touch the environment, 
# it just returns a dict with the values parsed from the .env file.
settings = dotenv_values(".env") 


APP_NAME     = settings.get("APP_NAME")
APP_URL      = settings.get("APP_URL")
API_HOST      = settings.get("API_HOST")
API_PORT      = settings.get("API_PORT")
SECRETE_KEY  = settings.get("SECRETE_KEY")
LOCAL_DB_URL = settings.get("LOCAL_DB_URL")
DB_HOST      = settings.get("DB_HOST")
DB_PORT      = settings.get("DB_PORT")
DB_USERNAME  = settings.get("DB_USERNAME")
DB_PASSWORD  = settings.get("DB_PASSWORD")
DB_NAME      = settings.get("DB_NAME")

