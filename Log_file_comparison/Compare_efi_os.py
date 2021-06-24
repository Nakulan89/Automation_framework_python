import efi_log
import os_log

efi_values = []
os_values = []
for efi_outer_key, efi_outer_value in efi_log.main_dict1.items():
    for efi_inner_key in efi_outer_value:
        efi_words = efi_outer_value[efi_inner_key]
        efi_values.append(efi_words)


for os_outer_key, os_outer_value in os_log.main_dict1.items():
    for os_inner_key in os_outer_value:
        os_words = os_outer_value[os_inner_key]
        os_values.append(os_words)

print("Comparing both the efi and os log for common parameter: ")

for x, y in zip(efi_values, os_values):
    if x == y:
        print("The {} values in both the log files are : {}".format("Common", x, y))
    else:
        print("The {} values in both the log files are : {} ".format("Uncommon", x, y))



