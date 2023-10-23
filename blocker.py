import time
from datetime import datetime as dt

host_temp ="hosts"
host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.twitter.com", "twitter.com"]

def check_if_exists(line):
    exists = False
    with open(host_temp, "r+") as file:
            content = file.readlines()
            for _line in content:
                if line == _line:
                    exists = True
                    break

    return exists


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        # print("Working Hours...")
        with open(host_temp, "r+") as file:
            # print(file)
            content = file.read()
            # print(content)
            for website in website_list:
                line = f"{redirect} {website} \n"
                exists = check_if_exists(line)
                if not exists:
                    file.write(line)
                    
    else: 
        with open(host_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours...")
    time.sleep(5)