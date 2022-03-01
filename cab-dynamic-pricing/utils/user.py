from flask_login import UserMixin
import software_configuration as cfg
import pandas as pd


class User(UserMixin):
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email
        self.user_information=pd.DataFrame('../data/user.csv')

    @staticmethod
    def get(user_id):
        
        specific_user_details=self.user_information.loc[self.user_information['user_id']==self.id]
        
        return User(specific_user_details['user_id'], specific_user_details['name'], specific_user_details['email'])

    @staticmethod
    def create(id_, name, email):
        try:
            
            user_details={'user_id': id_, 'name':name, 'email':email}
            df_user = pd.DataFrame.from_dict(user_details)
            self.user_information.append(df_user, ignore_index=True)
            self.user_information.to_csv('../data/user.csv')
            
            return True
        
        except:
            return False


