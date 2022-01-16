from flask import Blueprint
import requests


stream = requests.get('http://10.5.5.9/gp/gpControl/execute?p1=gpStream&c1=start')