import json
import os
from dotenv import dotenv_values, find_dotenv, load_dotenv

path = find_dotenv(".env")

config = {
    **dotenv_values(path),
    **os.environ,  # override loaded values with environment variables
}
# print(config)
