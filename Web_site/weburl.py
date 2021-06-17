import argparse
import configparser
import re
import subprocess


my_parser = argparse.ArgumentParser(description="get the user value to print number of url", prefix_chars='-')
my_parser.add_argument('value', type=int, help='number denote the url')

args = my_parser.parse_args()

user_value = args.value

parser = configparser.ConfigParser()
parser.read("C:\\Users\\Aravind\\PycharmProjects\\pythonProject\\Web_site\\weburl.ini")
user_url = parser.get("website_url", "LogFile")

url_pattern = "w{3}.\w+.\w+"

user_req_url = []
count = 0

with open(user_url, "r") as url:
    for web_url in url:
        required_urls = re.findall(url_pattern, web_url)
        if required_urls != user_req_url:
            for i in required_urls:
                count = count + 1
                if count >= user_value:
                    process = subprocess.run(["nslookup", i], stdout=subprocess.PIPE).stdout.decode()
                    print(process)
    else:
        print("File contains only {} url".format(count))

















