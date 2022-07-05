from data import cv_data


class Database:
    def __init__(self):
        self.__personal = cv_data['personal']
        self.__experience = cv_data['experience']
        self.__education = cv_data['education']

    @property
    def get_personal_data(self):
        return self.__personal

    @property
    def get_experience_data(self):
        return self.__experience

    @property
    def get_education_data(self):
        return self.__education


db = Database()
