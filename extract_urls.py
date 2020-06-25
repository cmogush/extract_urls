import os, csv, re
from pathlib import Path

src = r"C:\Users\Chris\Desktop\Python Scripts\extract_urls\test_dir"
dest = src

def extract_urls(text):
    """returns a list of all urls from file"""
    pattern = r"[ftp|http]{3,4}[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(pattern, text)
    return urls

def write_csv(fieldnames, rows, output_name):
    """write the csv to file"""
    with open(dest + '/' + output_name + '.csv', 'w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def main():
    rows = []
    for file in os.listdir(src):
        with open(src + "/" + file, 'r') as f:
            text = f.read().replace('\n', '') # read the file in as a string
            urls = extract_urls(text)
            f, e = os.path.splitext(os.path.basename(file))
            for url in urls:
                row = {'file': f, 'extension': e, 'url': url}
                rows.append(row)
    fieldnames = ['file', 'extension', 'url']
    write_csv(fieldnames, rows, 'url_report')

if __name__ == '__main__':
    main()