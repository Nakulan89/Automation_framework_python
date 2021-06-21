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
ip_pattern = '([0-9]{3}.[0-9]+.[0-9]+.[0-9]+|[0-9]{2}.[0-9]+.[0-9]+.[0-9]+)'

user_req_url = []
lt = []
dt = {}
count = 0

with open(user_url, "r") as url:
    try:
        for web_url in url:
            required_urls = re.findall(url_pattern, web_url)
            if required_urls != user_req_url:
                for i in required_urls:
                    lt.append(i)
                    count += 1
                    if count <= user_value:
                        process = subprocess.run(["nslookup", i], stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE).stdout.decode()
                    for j in process.split(':'):
                        if i == lt[count - 1]:
                            rt = j.strip('\t\r\n')
                            if re.findall(ip_pattern, rt) != user_req_url:
                                dt[lt[count - 1]] = "".join(re.findall(ip_pattern, rt))
    except NameError:
        print("Number of url found in the text input file", count, "Please give the count a user argument")

try:
    with open("C:\\Users\\Aravind\\PycharmProjects\\pythonProject\\Web_site\\ip_results.csv", mode='w') as url_data:
        field_names = ['SL.NO', 'TEXT URL', 'IP ADDRESS']
        writer = csv.DictWriter(url_data, fieldnames=field_names)
        writer.writeheader()

        for serial_num in range(1, count + 1):
            writer.writerow({field_names[0]: serial_num, field_names[1]: lt[serial_num - 1],
                             field_names[2]: dt[lt[serial_num - 1]]})
except PermissionError:
    print("Please close the output excel file to overcome the permission error ")
