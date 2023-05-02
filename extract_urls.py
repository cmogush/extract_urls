import os, csv, re, PyPDF2
from pathlib import Path

src = r"C:\Users\Chris\Desktop\Edison\Link Checks\Textbook Links\TB-AK-and-AWB"
dest = src
rows = []

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

def process_file(full_path, file):
    fname, ext = os.path.splitext(file)
    if ext == ".pdf":
        try:
            with open(full_path + "/" + file, "rb") as f:
                read_pdf = PyPDF2.PdfFileReader(f)
                page = read_pdf.pages[0]
                text = page.extractText().replace('\n', '')
                urls = extract_urls(text)
                for url in urls:
                    row = {'path': full_path, 'file': fname, 'extension': ext, 'url': url}
                    rows.append(row)
                print("{} processed".format(file))
        except:
            print("{} does not contain text".format(file))
    else:
        with open(full_path + "/" + file, 'r') as f:
            try:
                text = f.read().replace('\n', '')  # read the file in as a string
                urls = extract_urls(text)
                for url in urls:
                    row = {'path': full_path, 'file': fname, 'extension': ext, 'url': url}
                    rows.append(row)
                print("{} processed".format(file))
            except:
                print("{} does not contain text".format(file))

def dir_recursion(parentFolder, folder):
    full_path = os.path.join(parentFolder, folder)
    for entry in os.listdir(full_path):
        if os.path.isdir(os.path.join(full_path,entry)): # full path + entry needed
            dir_recursion(full_path, entry)
        else:
            process_file(full_path, entry)


def main():
    dir_recursion("", src)
    fieldnames = ['path', 'file', 'extension', 'url']
    write_csv(fieldnames, rows, 'url_report')
    print('url_report written')

if __name__ == '__main__':
    main()