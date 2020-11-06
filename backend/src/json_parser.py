""" Module for working with json files. """
import os
import json


class JSONParser:
    """ Class for working with json files. """
    def __init__(self):
        """ Init method. """
        self.this_folder = os.path.dirname(os.path.abspath(__file__))

    def get_json(self, name: str) -> str:
        """
        Method for getting json file. Name must be like 'name.json'.
        Return json: str.
        """
        if self.__is_exist(name):
            with open(f'{self.this_folder}\\..\\data\\{name}', 'r', encoding="utf-8") as f:
                return f.read()
        else:
            with open(f'{self.this_folder}\\..\\data\\{name}', 'w', encoding="utf-8") as f:
                empty_json = {
                    "Основное": []
                }
                json.dump(empty_json, f, ensure_ascii=False, indent=2)
                return str(empty_json)

    def update_json(self, name: str, new_json: dict) -> bool:
        """
        Update existing json files and return True.
        If something goes wrong, return False.
        """
        if self.__is_exist(name):
            with open(f'{self.this_folder}\\..\\data\\{name}', 'w', encoding="utf-8") as f:
                json.dump(new_json, f, ensure_ascii=False, indent=2)
            return True
        else:
            return False

    def __is_exist(self, name):
        """ Checking for file existence. """
        return name in os.listdir(path=f'{self.this_folder}\\..\\data')