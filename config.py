from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["MYSQL_USER"]
database = os.environ["MYSQL_DATABASE"]
password = os.environ["MYSQL_PASSWORD"]
host = os.environ["MYSQL_HOST"]

DATABASE_CONNECTION_URI = f"mysql://{user}:{password}@{host}/{database}"