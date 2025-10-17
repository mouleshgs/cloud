import dropbox

ACCESS_TOKEN = "sl.u.AGDXl1ZpNLIPrzwLx-E-5GemadCULSeg-IxJju6aqkhe_JFF2wTvnLtHDP2ZrsjmJsWZLKkLLZwnAQ5YuL4MvZsOREzDaH3XWsR1DpVGYsW_KSolbQ_mYa7MTLyaluO5isfjxxVstomXJzZV240W2rvxeg339TqMaPb57aZGzM6radyP4gzXkKhb8djSnVR9fHfVMEyHvbEcvLLnx_n6St3sFeGyj7y145sVaVYci9UW0lgLDPkvbLGevztAmrxVix9gddzAybHqHc6xLJVu5q2OTvvrUYLAazih6BldFIrpr7_ajCfH5FjI3zvAhHJ6vNRRsXL2aNRN3S2_-xlTEywYJlo6FP0-ZOkrB-vT76Qut2KHLrSWPzNJVtF_olDzM5Ny9vYabBNOzFe4NE304oAAVdLY8oFVoX0o5Ad6qdJi4XjvxiDb5IfIoVzblZDqcnsK2m9ujkb8ohK5J2xlEpdEfZJyh8DUgPVXn0X9VO82zDVCsEuBrknfxEP-5zR5IrlXvd3fH0w87JjhNsoAzRk5u3oD3y4bmuNltCxhWGwxPdAIOKWt350mnWTRGHa4O6qkS6F3eg7CRYmJ0cEdxNnCylc2vpWCXnWKk-9Q1v3eapAIm1nK3dQ3ZIZPWnt5FMYjijQmFA9ZxiJe-aO4BIqSsTbnPvlVsz_TGtqaMls_JICFeMuXhdwPZCztQ7nayeBwhQ76Flpgw1TuHjSdSTygNXwC0c-GkbSHTJtEmVj3gGlj6uQQoCMEYfdjZMW3irnOojFx00f2WN7tdfJNgya_sp4oJDc2sRAmvBGQaNhhI1Eqi47ETZ8DGZsKKvM9vd0bBQmT791536ISouQpqoIk00hdjxqRtSLnrBTYGfKVNfVgy02hY1rIQ3JBRz88XwfSXtqs7BJBPuFXijYO00WbUG2rJeFhvVHG0PvWGI_bJI1b1YPAT44oF5b01D4I5IOFF4pqdc8OgrHrP9PrF4Upk4TqpJHns3z5tCSHNYghJRFbERRCG_wPBd5wwLczrAmWX5zx7-iY4aPFVxnbYTr9aqdXiaPTlQYvSA6n_NlLF-MGYciNNUxouVwbwuRmq4GRmnvQ3UqypUz1eM4FerqqxbTGd9mHGLO6wf-1jipwr7DtQ8juWeLiBuoxr8d8St5neklzMSq6sRyV-DzYJF4mOLFyEuihqQcXAnZ2Y7IBVi0tKxQ8fupELe4tpPNh_2tu_Dqjv3KXEND3MWMIFCGeOrrvN1ujDX1165mbyqlDl5Uq4z2AQ3EEnH_YBvrQq9GdUnBKTXJXqScVqInRE6jJRYX9KX8W4AlXoEI7uVXFvtxD_32jvpdF57MHCirVJ4_V7ozvRzYiAXSB2H5Br7fkCkmUzCM0ZJnJkYZqaFml3JlCoZi0SKqMXrpxdRCGIf29Z-HmrSSf4AmcXky0ut9sB0FvqGjkwlu39BGp7h4TjQ"

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

