#!/usr/bin/python3


import json
import os
from models.base_model import BaseModel


class FileStorage:


    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        objts_dict = {}

        for key, obj in self.__objects.items():
            objts_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objts_dict, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                alm = f.read()
                dictr = json.loads(alm)
                for key, value in dictr.items():
                    value = dictr[key]
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[key] = obj
        else:
            pass
