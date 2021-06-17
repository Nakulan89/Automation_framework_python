import argparse
import configparser
import csv
import re
import subprocess

my_parser = argparse.ArgumentParser(description="get the user value to print number of url", prefix_chars='-')
my_parser.add_argument('value', type=int, help='value is a minimum url present in the txt file. Please enter integer '
                                               'value in cmd as a argument')

args = my_parser.parse_args()

user_value = args.value

parser = configparser.ConfigParser()
parser.read("C:\\Users\\Aravind\\PycharmProjects\\pythonProject\\Web_site\\weburl.ini")
user_url = parser.get("website_url", "LogFile")

url_pattern = "w{3}.\w+.\w+"

user_req_url = []
lt = []
count = 0

with open(user_url, "r") as url:
    for web_url in url:
        required_urls = re.findall(url_pattern, web_url)
        lt.append(required_urls)
        if required_urls != user_req_url:
            for i in required_urls:
                count = count + 1
                if count <= user_value:
                    process = subprocess.run(["nslookup", i], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode()
                    print(process)
    else:
        print("File contains only {} url".format(count))

with open("C:\\Users\\Aravind\\PycharmProjects\\pythonProject\\Web_site\\ip_results.csv", mode='w') as url_data:
    field_names = ['SL.NO', 'TEXT URL', 'IP ADDRESS']
    writer = csv.DictWriter(url_data, fieldnames=field_names)
    writer.writeheader()

    for serial_num in range(1, count+1):
        writer.writerow({field_names[0]: serial_num, field_names[1]: list(filter(lambda x: x, lt[serial_num+1]))})
