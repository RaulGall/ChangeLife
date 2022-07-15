from __future__ import annotations
from flask_wtf import FlaskForm
import json
from os.path import exists


class BusinessLayer:
    __roles_test = []
    __personality_test = []
    __data_manager: DataManager

    def __init__(self):
        self.__data_manager = FileDataManager('data')
        self.__personality_test, self.__roles_test = self.__data_manager.load_data()


    def add_personality_test(self, test: FlaskForm):

        test_result = {field.short_name: field.data for field in test
                       if field.short_name != 'csrf_token'}
        self.__personality_test.append(test_result)
        self.__data_manager.save_data(self.__personality_test,
                                      self.__roles_test)


    def add_role_test(self, test: FlaskForm):

        test_result = {field.short_name: field.data for field in test
                       if field.short_name != 'csrf_token'}
        self.__roles_test.append(test_result)
        self.__data_manager.save_data(self.__personality_test,
                                      self.__roles_test)


    def get_personality_test(self):
        return self.__personality_test

    def get_roles_test(self):
        return self.__roles_test

    def get_calculate_distance(self, email: str):
        user_personality_test = self.__get_user(email)
        distance = []

        for roles_test in self.__roles_test:
            role_distances = []
            for key, value in user_personality_test.items():
                if key in roles_test.keys():
                    role_distances.append(abs(value - roles_test[key]))

            distance_value = -1
            if len(role_distances) > 0:
                distance_value = sum(role_distances) / len(role_distances)

            distance.append((roles_test['rolename'], distance_value))
        distance.sort(key=lambda tup: tup[1])
        return distance

    def __get_user(self, email: str):
        personality_test = {}
        for user in self.__personality_test:
            if user['email'] == email:
                personality_test = user
        return personality_test


class DataManager:
    def save_data(self, personality_test, roles_test):
        pass

    def load_data(self):
        pass


class FileDataManager(DataManager):
    def __init__(self, path: str):
        self.__path = path

    def save_data(self, personality_test, roles_test):
        personality_json_object = json.dumps(personality_test, indent=4)
        roles_json_object = json.dumps(roles_test, indent=4)

        self.__save_file('personality_test', personality_json_object)
        self.__save_file('roles_test', roles_json_object)

    def __save_file(self, file_name:str, data):
        file_path = self.__get_file_path(file_name)
        with open(file_path, 'w') as outfile:
            json.dump(data, outfile)

    def load_data(self):
        personality_test = self.__load_file('personality_test')
        roles_test = self.__load_file('roles_test')

        return personality_test, roles_test

    def __load_file(self, file_name:str):
        file_path = self.__get_file_path(file_name)
        if exists(file_path):
            with open(file_path) as json_file:
                data = json.load(json_file)
                return json.loads(data)

        return []

    def __get_file_path(self, file_name):
        return self.__path + '/' + file_name + '.json'