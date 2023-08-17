import requests
import random
import string
file_url = "https://ciclovivo.com.br/wp-content/uploads/2018/10/iStock-536613027-1024x683.jpg"

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
   

def download_file_from_n_link():
    r = requests.get(file_url, stream = True)
    if 'jpg' in file_url:
        name = str(get_random_string(6)) + ".jpg"
    elif 'png' in file_url:
        name = str(get_random_string(6)) + ".png"
    elif 'webp' in file_url:
        name = str(get_random_string(6)) + ".webp"    
    elif 'jpeg' in file_url:
        name = str(get_random_string(6)) + ".jpeg"
    else:
        name = str(get_random_string(6)) + ".bin"
    with open(name, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    
    with open(name, "rb") as f:
        blob = f.read()
        
    return blob
                

download_file_from_n_link()

