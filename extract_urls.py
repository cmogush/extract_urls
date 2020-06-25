import os, csv, re
from pathlib import Path

src = r"C:\Users\Chris\Desktop\Python Scripts\extract_urls\test_dir"
dest = src

def extract_urls(text):
    """returns a list of all urls from file"""
    pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(pattern, text)
    return urls

def get_data(src):
    """returns a list of dictionaries to convert to csv rows"""
    rows = []
    #iterate over the directory
    for file in os.listdir(src):
        with open(file, 'r') as f:
            f, e = os.path.splitext(os.path.basename(file))
            data = f.readlines()
    #TODO: get urls
    # row = filename, extension, url
    return rows

#TODO: compile into a dictionary to write to CSV

