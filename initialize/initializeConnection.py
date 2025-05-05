from initialize.connect import connect
from initialize.config import load_config

def initialize_con():
    config = load_config()  # Load config from config.py
    return connect(config)  # Use the connect function defined in connect.py