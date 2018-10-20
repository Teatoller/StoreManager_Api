# class UserModel():
#     user_id =1   
    
    
#     def __init__(self, username, email, password):
#         """  """
#         self.user_id = UserModel.user_id
#         self.username = username
#         self.email = email
#         self.password = password
#         UserModel.user_id += 1
   
   
#     def resultant(self):
#         """ """
#         return dict(
#             user_name=self.username,
#             user_email=self.email,
#             user_password=self.password,            
#         )


# class ListDatabase():
#     """ Database Model for methods """
#     PRODUCTS = []
#     SALES = []
#     USERS = []

#     @classmethod
#     def get_user_id(cls, user_id):
#         """ Iterates and loops USERS list and return the user """
#         for user_id in cls.USERS:
#             if username.user_id == user_id:
#                 return username

#     @classmethod
#     def get_user_by_name(cls, name):
#         """ Iterates and loops and returns all users in USERS list """
#         for user in cls.USERS:
#             if user.name == name:
#                 return user       