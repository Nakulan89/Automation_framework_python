import re
import time
from time import strftime


def main():

    log_file_path = 'C:\\Users\\Aravind\\PycharmProjects\\pythonProject\\sfbios.log'

    export_file_path = "C:\\Users\\Aravind\\PycharmProjects\\pythonProject\\"

    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

    file = "\\" + "Parser Output " + time_now + ".txt"
    export_file = export_file_path + file

    regex = '(<property name="(.*?)">(.*?)<\\/property>)'

    parse_data(log_file_path, export_file, regex, read_line=True)


def parse_data(log_file_path, export_file, regex, read_line=True):

    match_list = []
    with open(log_file_path, 'r') as file:
        if read_line:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)
                    print(match_text)
        else:

            data = file.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group()
                match_list.append(match_text)
                print(match_text)
    file.close()

    with open(export_file, "w+") as file:
        file.write("EXPORTED DATA:\n")
        match_list_clean = list(set(match_list))
        for item in range(0, len(match_list_clean)):
            print(match_list_clean[item])
            file.write(match_list_clean[item] + "\n")
    file.close()


if __name__ == '__main__':
    main()
