from ast import literal_eval


def human_bytes(B):

    B = B
    KB = 1024
    MB = KB ** 2
    GB = KB ** 3
    TB = KB ** 4

    if B < KB:
        return '{0} {1}'.format(B, 'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{} KB'.format(B // KB)
    elif MB <= B < GB:
        return '{} MB'.format(B // MB)
    elif GB <= B < TB:
        return '{} GB'.format(B // GB)
    elif TB <= B:
        return '{} TB'.format(B // TB)


main_dict1 = {}
inter_dict1 = {}
main_key1 = ''
search_key_11 = "SocketDesignation"
k1 = "socket_desg"
search_key_12 = "Cache Configuration"
k2 = "Config"
search_key_13 = "Write Back"
k3 = "Operation_mod"
search_key_14 = "Enabled Internal"
k4 = "Loc"
search_key_15 = "InstalledSize"
k5 = "Ins_size"
search_key_16 = "MaximumCacheSize"
k6 = "Max_size"
search_key_17 = "SupportedSRAMType"
k7 = "Support_type"
search_key_18 = "Cache SRAM Type"
k8 = "Ins_type"
search_key_19 = "CacheSpeed"
k9 = "speed"
search_key_20 = "Cache Error Correcting Type"
k10 = "Error_correct"

with open("C:\\Users\\Aravind\\PycharmProjects\\pythonProject\\Log_file_comparison\\log_efi.log", "r") as efi_parm:
    for line in efi_parm.readlines():
        if search_key_11 in line:
            val = line.split(':')[1].strip()
            main_key1 = val
            inter_dict1 = {k1: val}
        if search_key_12 in line:
            val = line.split(':')[1].strip()
            inter_dict1[k2] = val
        if search_key_13 in line:
            val = search_key_13
            inter_dict1[k3] = val
        if search_key_14 in line:
            val = search_key_14.split()[1]
            inter_dict1[k4] = val
        if search_key_15 in line:
            val = line.split(':')[1].strip()
            val = literal_eval(val)
            val = human_bytes(val)
            inter_dict1[k5] = val
        if search_key_16 in line:
            val = line.split(':')[1].strip()
            val = literal_eval(val)
            val = human_bytes(val)
            inter_dict1[k6] = val
        if search_key_17 in line:
            val = line.split(':')[1].strip()
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
