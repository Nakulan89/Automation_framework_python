main_dict1 = {}
inter_dict1 = {}
main_key1 = ''
search_key_11 = "Socket Designation"
k1 = "socket_desg"
search_key_12 = "Configuration"
k2 = "Config"
search_key_13 = "Operational Mode"
k3 = "Operation_mod"
search_key_14 = "Location"
k4 = "Loc"
search_key_15 = "Installed Size"
k5 = "Ins_size"
search_key_16 = "Maximum Size"
k6 = "Max_size"
search_key_17 = "Pipeline Burst"
k7 = "Support_type"
search_key_18 = "Installed SRAM Type"
k8 = "Ins_type"
search_key_19 = "Speed"
k9 = "speed"
search_key_20 = "Error Correction Type"
k10 = "Error_correct"

with open("C:\\Users\\Aravind\\PycharmProjects\\pythonProject\\Log_file_comparison\\log_os.log", "r") as os_parm:
    for line in os_parm.readlines():
        if search_key_11 in line:
            val = line.split(':')[1].strip()
            main_key1 = val
            inter_dict1 = {k1: val}
        if search_key_12 in line:
            val = line.split(':')[1].strip()
            inter_dict1[k2] = val
        if search_key_13 in line:
            val = line.split(':')[1].strip()
            inter_dict1[k3] = val
        if search_key_14 in line:
            val = line.split(':')[1].strip()
            inter_dict1[k4] = val
        if search_key_15 in line:
            val = line.split(':')[1].strip()
            inter_dict1[k5] = val
        if search_key_16 in line:
            val = line.split(':')[1].strip()
            inter_dict1[k6] = val
        if search_key_17 in line:
            val = search_key_17
            inter_dict1[k7] = val
        if search_key_18 in line:
            val = line.split(':')[1].strip()
            inter_dict1[k8] = val
        if search_key_19 in line:
            val = line.split(':')[1].strip()
            inter_dict1[k9] = val
        if search_key_20 in line:
            val = line.split(':')[1].strip()
            inter_dict1[k10] = val
            main_dict1[main_key1] = inter_dict1
