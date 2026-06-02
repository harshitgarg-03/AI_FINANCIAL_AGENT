from sqlalchemy import create_engine
from dotenv import load_dotenv

import os;

load_dotenv()

DATABASE_URL = os.getenv("");

engine = create_engine(DATABASE_URL);