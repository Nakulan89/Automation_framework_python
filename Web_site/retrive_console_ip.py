import weburl as ip_web
import re

ip_web.lt = list(filter(lambda x: x, ip_web.lt))
ft = ["".join(hj) for hj in ip_web.lt]
ip_pattern = '([0-9]{3}.[0-9]+.[0-9]+.[0-9]+|[0-9]{2}.[0-9]+.[0-9]+.[0-9]+)'
rf = ip_web.process.split()
fk = []
dt = {}
for j in rf:
    if ip_web.i == ft[0]:
        rt = j.strip('\t\r\n')
        if re.findall(ip_pattern, rt) != fk:
            gh = re.findall(ip_pattern, rt)
    if ip_web.i == ft[1]:
        rt = j.strip('\t\r\n')
        if re.findall(ip_pattern, rt) != fk:
            gl = re.findall(ip_pattern, rt)
    if ip_web.i == ft[2]:
        rt = j.strip('\t\r\n')
        if re.findall(ip_pattern, rt) != fk:
            gp = re.findall(ip_pattern, rt)
    if ip_web.i == ft[3]:
        rt = j.strip('\t\r\n')
        if re.findall(ip_pattern, rt) != fk:
            go = re.findall(ip_pattern, rt)
