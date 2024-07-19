import configparser

config = configparser.ConfigParser()
config.read("config.ini")

base_url = config.get("pytest", "BASE_URL")
