import requests as r
from bs4 import BeautifulSoup
import json
import os
import time
from pprint import pprint
import traceback
from datetime import datetime
import pandas as pd

def get_reformatted_headers(headers_file):
    with open(headers_file, 'r') as f:
        headers_data = f.read()
    headers_dict = {}
    for i in headers_data.split('\n'):
        if len(i.split(':')) > 1:
            headers_dict[i.split(':')[0]] = i.split(': ')[1]
    return headers_dict