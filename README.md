# OIUploader
A python3 application to upload files to open-webui - Windows version.
This program uses the open-webui APIs.
Program can load large files > 5Mb.


![image](https://github.com/user-attachments/assets/d504e749-9706-4998-b23d-ce56e92d191e)

SETUP:
 1. Clone the repo to your local environment
 2. Edit the dotenv file with your URL and open-webui sk-key
 3. Save the local dotenv file as .env

When used behind a proxy server, you need to extend the time_outs. I added the following to my proxy server:

                proxy_connect_timeout 60m;
                proxy_read_timeout 60m;


USE:
 1. Run the application
 2. Click "Select file" will open a selection window - select the file you want to upload
 3. The "File to upload" will update with the file name and location. If the file is incorrect, Click "Select file" again
 4. After selection the file, the "Upload file" button will be enabled. Click it to send the file to you local Open-webui environment

 The file will be uploaded and then scanned into Open-webui - This process takes a long time as it scans the entire database.
 Once both uploading and scanning are complete, the checkboxes will be checked and "Upload file" button will be disabled.

WARNING:
Uploading files and scanning takes a long time - I have had it take >10 minutes. The window may show as 'Not responding', but the process is running on your server.

TODO:
1. Have scanner only scan the new file, not entire directory.
2. Make Linux version.
3. Fix checkboxes to update individually - currently only checked after full processing is complete
4. Add status bar to show progress

FINAL NOTE:
Personally, I use pyinstaller to make this into an executable on my desktop. I didn't provide the exe so everyone can review the code and make your own decisions. 
