import configparser
import io
import os
from mastodon import Mastodon

config = configparser.ConfigParser()

config.read('cred.ini')


def read_temp():
    fd = os.open("/dev/ttyACM0", os.O_NOCTTY | os.O_RDWR)
    tty_file = io.FileIO(fd, "r+")
    tty_wrapper = io.TextIOWrapper(tty_file)
    resp = tty_wrapper.readline().strip()
    tty_file.close()
    return resp


if __name__ == '__main__':

    mastodon = Mastodon(
        access_token=config['config']['access_token'],
        api_base_url=config['config']['url']
    )
    temp_c = read_temp()
    acct_id = mastodon.account_verify_credentials()['id']
    mastodon.toot(f"Hello, pycon! Current temperature is {temp_c}C")