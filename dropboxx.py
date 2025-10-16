import dropbox

ACCESS_TOKEN = "sl.u.AGACUp8Q6EqWTJBqIru_KnrzZzAVT5t0Kt3g2nBlrR1I-HoJaQS0dKv3SC7bg2o6gdtZQtpa-tW5irYJI9epqTE3m3uGhfFxlkzweLSvy61lxVNo0lTGoCnM5kQwIV2JTG4N78xtUdnUzdIHEtrv1NCUg4uqXM11kANktD_vexDRwKpyv7YxQpemb1TLOIgze7JbU83bnLjpEJAKDPCEJCXeC-o_kEENEyKz4Pmyj-qTGtXCXpKL66G7LAUfHtI6gfGOEE0M8jYLlkEwUSldZeSwLLCdnltGeO9tg2eTxWT4I229BwRqI5bwwTf-wo3PxnImxH6B525KRnWNMBc4c7egK2ZCC860ZwG0QN2Pe6XAY1z19p6XpsJJ8gPxk8gOLdmu4-ocbtwcyZ-6xm8on-3UY10Q_Zl6ROLZVkItfcBExjzxAuvGvvj6rVYuwGTyUnusXxwpreeBkiUDa79t2kXxZusoNLqteCOQJr682o97VgfXdHwnIOUOoaL7K0CGyU6jxRvfrG-rNJNDDZTgqeR8T9FOuV853bKq2KnskN3EZ3k8AmiWIPIgHJlhAfpN1arErMZ4S6i87nFOysk6kruhs9qTLgvpHBZ_Hh12LrGYr1p7HPfotInEy2g6gV1pWpWnPAshp_SNhLdVwag1VGsTslas2oWbtOCu3hyyu3xQGZV1U0b0XpzxI5QDdjSYAT1nBeJvJHqgHWvKJKmec2nSOABZNw1F87YhMmMZT83lrmLidkOCwpT6jNxCEj58GgAnsu2lo1hvLnjSc1ks6ljQUy_-AhLWYBKofPFw6HUgvu_m33nTnXGbHtBxg3dWG8lCnjU52XKJLkCULhL6v5UD4laqLPfrnKIa_dHzzT2lfHNDt8cUV92MXvkWKOH-CzsnotGcI5NcWMe84gUmBzbKowDBg-jmRTFdeWQ3B6zZVGr5-A9sONQy5T6rskOgKLCAxUJwlCdMyDtroNlJc1m9oRwjHjViz2jU1H3Xg8bIVRfnU2NLFlZFDSJ5ZGeLylHTooxMPL7oiSAzEZL1kqLAxXWSb_nz4df5rrMCsP41UFY82bNkkpMsoam8_mmSvn-B2S4_nfGkVY3F7sZ56F9jRedJUc_PKA5SIDa7QjBkeSIWZOlTG4pMCxWZOZmZy62YLVJM3y3rEeaVXC-gl4q1Q04UbeI54KKwpJiWooW-E95_qgbU10U0iEn2ChO2NIX94lz1VVXD1T2M3nikCTpw9UzY-RYSb46ZBrXXUnSDs7cj94kNNYwbs4__7mjCM64AHA1Crp_p7mO-0v3uyMKRD8EZYRmyumLPZENtjBg8vEjFUAtnZTmQhKvnvk8XhnnwRtH105pGZwZgT-YKEQR2HIg1LIHkFPPC8GibEuM_-SkZDn-Ue1Jm3ZNp5ItI3PeUeLkyx_AOK4M2PGZIYEFfIXwxiWuZUb50QNervPxUOg"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

def upload_file(local_path, dropbox_path):
    with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    print(f"Uploaded '{local_path}' to Dropbox as '{dropbox_path}'")

def download_file(dropbox_path, local_path):
    metadata, res = dbx.files_download(path=dropbox_path)
    with open(local_path, 'wb') as f:
        f.write(res.content)
    print(f"⬇Downloaded '{dropbox_path}' from Dropbox to '{local_path}'")

if __name__ == "__main__":
    upload_file("example.txt", "/example.txt")

    download_file("/example.txt", "downloaded_example.txt")
