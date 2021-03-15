#!/usr/bin/env python3
import time

from TrelloEngine.TrelloCore import TrelloCore
import json
def Main():
    with open(".env","r") as file:
        key =json.load(file)
    test = TrelloCore(app_key=key["api_key"], token=key["token"])


if __name__ == '__main__':
    Main()