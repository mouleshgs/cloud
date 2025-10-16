import dropbox

ACCESS_TOKEN = "sl.u.AGCMPIG22dSuFhWwC518Kdn_TlmIoApnASlPHVsdbwbhlM9P9-QusKQcUMmYru5QCK_GD3o_8bwKghJhvgg1a58p4YDlX37KP_qCmr1UD0N6jaizMUa_V6PveFR4zz4qDJf8s223sIyMcZyXa9AXSaSJE6OfpC026ZgwpIZQJ7_m5epU9tE2Ylfd6i14n5d7cSJYhFDZiu63aPlkmygGKuXi-xqdtoHQ7fyCQZPkiyMotxRRHXTcpISu6lgEMVgMlPX_uHg6EJheH-P-f0MPwxiyjjjW4CSLjp2EZ_C9Fdv3etrmIHZqDMoSSucIQ799t3fbR88lghVMiqqmUNKYYbQ_Deq6-f0AWOfo6Vpiv6x3oZBywkl_Lwkah_2i6dcGi6jyARQ79osO8qlvI5DHOJ8IjA63OBsQWSr5qGhs8WFIzgq4JPEogl6Y4OVBxFqX4oLve93FRBUWzmDBr10mOfaV5O467ZRggFra6n8WaAZD6UybvdkiXkNY4K4BIknxlh53QjW9EPmydKd9FvaOVME3sDm9QSvGcT_WIPNtl2PicwWK6yZouZjm93Bv0X7nTmmnRFeWzuog2sXO1T6Wx6rNR4GaQSMklB5FkQ2f7H8UHPqsBIou6oNs7DeW5wp_Ifb2JJ5jD0JKPAoAW47AYBVP2ncrlc1An1gyJUF667_gXXQQj53Uu3-pi1j98G3vZjxVfGdi9Igk2SiyEoQXxba1Pfeptwj-gKFzHonKunrpZUwVNbN9B5qu62bIiqYCqv5SRu8XwB2xx357B3W1_A8IRKPRvf2L0d8b53jIWEv120KBHLikcjpTtbHkHkURyjqrJz3c17nZGcrFpNtbp5xDlkauY5B8MgQ0Km6Jr9YbcRfCXLwsylmWVAKnW3J7c2m4-8nKRZMFF4vZcreUunJe48B_0Hu5ZgaGM7x3fykx_XElX8Ijb72I34gi42TqNmJAgyYVNIAeCkjFtl_5b0c7ndBKuxVqX9jo4e5UqgpUDhgsAoISj4mCVwZAJiYHTuzizHFeRzkRVv1LjvVIJWBAIfkqH4TbkTZ9_h1YO05BO6e6_Qi--HsVzU9M50FcYz8H4NaB-TksyhcScYhRsDP_h2lc2nIhq3HqZmDW4kysYgDRGujXvLFQ_6tK8g577lKxQ4tyMQQF25i_leoDX_8Rxldom0ibd8v353TdRmcArq-CDA8klHsYeWAm8E-RUGAOvxKoUh4dVvDFXtDLbyw55_NXxoH-rRlQJskmNUhreYIL9tDNSErDSffK2oV8cL12n9VfTlcy7P0uveeRZ2lrMm-2r5GfwCqMZ-aM1hYGFiEcos_2bpKi8jChL8H06D9MwYdGDH3a0TFFYPXTx0ebbZmI1gqyBw0Hxjqspjb9Nj5-6aNjhbnp5Jsb5eJofePf_dwJ3t5VDwKMZVCf5EekxDB0sXUA6nHM37rgKOsNKw"

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
