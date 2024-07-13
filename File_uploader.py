# File uploader
import os
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv, dotenv_values
# from pathlib import Path

file_ids = ''
headers={'Authorization': f'Bearer {os.getenv("API_KEY")}'}
print(headers)
# Upload file


class File_uploader():
        
    def scanner(self):
        resp = requests.get(f'{os.getenv("URL")}/rag/api/v1/scan', headers=headers )

        if resp.status_code == 200:
            print ("Successful scan update")
        
        else:
            print ("Failed scan update")

        return resp.status_code

    def load_file(self, file):
        
        f = open(file, 'rb')

        files = {"file": (file, f)}

        resp = requests.post(f'{os.getenv("URL")}/rag/api/v1/doc', files=files, headers=headers )
        print(resp.text)
        print("status code " + str(resp.status_code))

        if resp.status_code == 200:
            print ("Success")
            print(f"response: {json.loads(resp.text)}")
            data = json.loads(resp.text)
            file_ids = data['filename']
            #scanner()
            print (file_ids)
        else:
            print ("Failure")
        
        return resp.status_code

if __name__ == "__main__":
    load_file(sys.argv)
    sys.exit(app.exec())

def __init__(self, file):
    self.file = file
