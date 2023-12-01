import json

# Reading data from a JSON file
with open('GasDataExtraction.json') as file:
    data = json.load(file)

# Accessing values
print(data['Date'])  # Replace 'key' with the specific key in your JSON data
