from flask_login import UserMixin
import pandas as pd

users_csv_path = 'database/users.csv'


class User(UserMixin):
    '''
    The user class of type Usermixin from flask_login handles
    the user information.
    param: Oauth unique ID, name, email
    methods: get(user_id): Checks if the user exists in the
             database
             create(user_id, name, email): Creates a new user
             in the database
    '''

    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email

    @staticmethod
    def get(user_id):
        '''
        This module checks if the user exists in the database.
        param: user_id
        return : Object of the User class with required details
        '''

        user_information = pd.read_csv(users_csv_path)
        specific_user_details = \
            user_information.loc[user_information['user_id'] == user_id]

        return User(specific_user_details['user_id'][0],
                    specific_user_details['name'][0],
                    specific_user_details['email'][0])

    @staticmethod
    def create(id_, name, email):
        '''
        Creates a user if not already present in the database.
        param: google oauth user_id, name, email
        return: True if successfully added to the database
        return: False if any error while adding to the database
        '''
        try:
            user_information = pd.read_csv(users_csv_path)
            current_user = pd.DataFrame({'user_id': [id_], 'name': [name],
                                         'email': [email]})
            user_information = pd.concat([user_information, current_user])
            user_information.to_csv(users_csv_path, index=None)
            return True
        except BaseException as error:
            print('An exception occurred while creating User\
            CSV: {}'.format(error))
