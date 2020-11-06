""" Module for working with json files """
import os
import json


class JSONParser:
    """ Class for working with json files """
    def __init__(self):
        """ Init method """
        self.this_folder = os.path.dirname(os.path.abspath(__file__))

    def get_json(self, name: str):
        """
        Method for getting json file. Name must be like 'name.json'
        Return json: str
        """
        if name in os.listdir(path=f'{self.this_folder}\\..\\data'):
            with open(f'{self.this_folder}\\..\\data\\{name}', 'r', encoding="utf-8") as f:
                return f.read()
        else:
            with open(f'{self.this_folder}\\..\\data\\{name}', 'w', encoding="utf-8") as f:
                empty_json = {
                    "Основное": []
                }
                json.dump(empty_json, f, ensure_ascii=False, indent=2)
                return str(empty_json)
