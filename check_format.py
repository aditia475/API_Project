##CHECK FOR POSTMAN COLLECTION FORMAT

import chardet
import codecs
import json

def check_format_func():
    # Open the file in binary mode to detect the encoding
    with open('VSR.json', 'rb') as f:
        # Use chardet to detect the encoding
        result = chardet.detect(f.read())
    
    # Open the file again in text mode with the detected encoding
    with codecs.open('VSR.json', 'r', encoding=result['encoding']) as f:
        data = json.load(f)

    if 'item' and 'info' in data:
        print("Postman Collection is in correct Format.")
    else:
        print("Postman Collection is not in correct Format.")
        
        


##def main():
##    print("Main Function")
##
##if __name__ == "__main__":
##    check_format_func()


