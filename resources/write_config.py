import pathlib
from configparser import ConfigParser

config = ConfigParser()

config.add_section('main')

config.set('main', 'REGULAR_ACCOUNT', ' DU5001780')
config.set('main', 'REGULAR_PASSWORD', 'test1234')
config.set('main', 'REGULAR_USERNAME', 'btrad5149')

config.set('main', 'PAPER_ACCOUNT', 'YOUR_ACCOUNT_NUMBER')
config.set('main', 'PAPER_PASSWORD', 'YOUR_ACCOUNT_PASSWORD')
config.set('main', 'PAPER_USERNAME', 'YOUR_ACCOUNT_USERNAME')

new_directory = pathlib.Path("config/").mkdir(parents=True, exist_ok=True)

with open('config/config.ini', 'w+') as f:
    config.write(f)

