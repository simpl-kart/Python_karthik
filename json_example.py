import json
############json is hugely popular and it's the format for storing the data like how mp3 is the format for storing music
data={"name" : "Karthik", "age":40}  ####This looks like a dictionary in python but actually it's of string object type
json_string = json.dumps(data)
print json_string
print type(json_string) 