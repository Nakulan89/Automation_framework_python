import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
    }
}

with open('data_file.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)

with open('data_file.json', 'r') as read_file:
    data = json.load(read_file)
    print(data)



