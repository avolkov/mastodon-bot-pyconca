import configparser

from mastodon import Mastodon

config = configparser.ConfigParser()

config.read('cred.ini')

def read_temp():
    pass


if __name__ == '__main__':

    mastodon = Mastodon(
        access_token=config['config']['access_token'],
        api_base_url=config['config']['url']
    )

#mastodon.toot("Hello, world")