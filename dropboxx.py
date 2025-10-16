import dropbox

ACCESS_TOKEN = "token"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

def upload_file(local_path, dropbox_path):
    with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    print(f"Uploaded '{local_path}' to Dropbox as '{dropbox_path}'")

def download_file(dropbox_path, local_path):
    metadata, res = dbx.files_download(path=dropbox_path)
    with open(local_path, 'wb') as f:
        f.write(res.content)
    print(f"Downloaded '{dropbox_path}' from Dropbox to '{local_path}'")

if __name__ == "__main__":
    upload_file("example.txt", "/example.txt")

    download_file("/example.txt", "downloaded_example.txt")
