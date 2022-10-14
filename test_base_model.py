#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print("-1-")
print(my_model)
print("-2-")
print(my_model.created_at)
print("-3-")
my_model_json = my_model.to_dict()
print(my_model_json)
print("-4-")
print("JSON of my_model:")
print("-5-")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, (my_model_json[key]), my_model_json[key]))

print("-6-")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print("-7-")
print(my_new_model)
print("-8-")
print(my_new_model.created_at)
print("-9-")

print("--")
print(my_model is my_new_model)
