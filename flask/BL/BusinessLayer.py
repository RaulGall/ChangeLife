from typing import List
from flask_wtf import FlaskForm

class BusinessLayer:
    __roles: List[dict]
    __personality_test = []

    def BusinessLayer(self):
        self.__roles = List[dict]
        self.__personality_test = []
        print("BL created")

    def addPersonalityTest(self, test:FlaskForm):

        test_result = {field.short_name: field.data for field in test
                       if field.short_name != 'csrf_token'}
        self.__personality_test.append(test_result)
        print(self.__personality_test)

    def getPersonalityTest(self):
        return self.__personality_test
