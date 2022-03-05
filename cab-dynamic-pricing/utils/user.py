from flask_login import UserMixin
import software_configuration as cfg
import pandas as pd


class User(UserMixin):
    '''
    The user class of type Usermixin from flask_login handles the user information.
    param: Oauth unique ID, name, email
    methods: get(user_id): Checks if the user exists in the database
             create(user_id, name, email): Creates a new user in the database
    '''
    
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email
        self.user_information=pd.DataFrame('../data/user.csv')

    @staticmethod
    def get(user_id):
        '''
        This module checks if the user exists in the database.
        param: user_id
        return : Object of the User class with required details
        '''
        
        specific_user_details=self.user_information.loc[self.user_information['user_id']==self.id]
        
        return User(specific_user_details['user_id'], specific_user_details['name'], specific_user_details['email'])

    @staticmethod
    def create(id_, name, email):
        '''
        Creates a user if not already present in the database. 
        param: google oauth user_id, name, email
        return: True if successfully added to the database
        return: False if any error while adding to the database
        '''        
        
        try:
            
            user_details={'user_id': id_, 'name':name, 'email':email}
            df_user = pd.DataFrame.from_dict(user_details)
            self.user_information.append(df_user, ignore_index=True)
            self.user_information.to_csv('../data/user.csv')
            
            return True
        
        except:
            return False


