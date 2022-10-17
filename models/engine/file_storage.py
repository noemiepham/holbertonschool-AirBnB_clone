# !/usr/bin/python3
"""import module"""
import json


class FileStorage():
    """class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns diction"""
        return FileStorage.__objects

    def new(self, obj):
        """set obj """
        obj_id = obj.id
        obj_name = obj.__class__.__name__
        FileStorage.__objects[obj_name + "." + str(obj_id)] = obj

    def save(self):
        """serializes"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF8") \
                as fil_name:
            json.dump(new_dict, fil_name)

    def reload(self):
        """deserializes"""
        from models.base_model import BaseModel
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(FileStorage.__file_path,
                      encoding="utf-8-sig") as file_name2:
                data = json.load(file_name2)
                cls = '__class__'
                for key, value in data.items():
                    FileStorage.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
