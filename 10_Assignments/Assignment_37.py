# Import the `json` module and convert a Python dictionary 
# user = {"name": "Alice", "age": 25} into a JSON string using json.dumps().


import json

user = {"name": "Alice", "age": 25}
json_str = json.dumps(user)

print("JSON String:", json_str)