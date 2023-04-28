##FINDS AND RETURNS METHODS AND URLS

import chardet
import codecs
import json
import check_format

def returns_methods_urls():
    # Open the file in binary mode to detect the encoding
    with open('VSR.json', 'rb') as f:
        # Use chardet to detect the encoding
        result = chardet.detect(f.read())
    
    # Open the file again in text mode with the detected encoding
    with codecs.open('VSR.json', 'r', encoding=result['encoding']) as f:
        data = json.load(f)

    for item in data['item']:
        if 'request' in item:
            request = item['request']
            method = request['method']
            url = request['url']['raw']
            print(f"Method: {method}\nURL: {url}\n")


def main():
    print("Main Function")

if __name__ == "__main__":
    check_format.check_format_func()
    returns_methods_urls()
