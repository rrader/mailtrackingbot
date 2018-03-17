import argparse
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
config.read('secret.ini')

parser = argparse.ArgumentParser(description="aiohttp server example")
parser.add_argument('--path')
parser.add_argument('--port')

db = configparser.ConfigParser()
db.read('db.ini')
