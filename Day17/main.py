# # Class is Blueprint of object

# class User:
#     def __init__(self):
#         print("User Created Successfuly!")

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Dhruvil"

# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Nakrani"

# # Constructor

# # class Car:
# #     def __init__(self):
# #         # initialise attributes

class User:
    def __init__(self, user_id, username):
         self.id = user_id
         self.usename = username
         self.followers = 0
         self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Dhruvil")
user_2 = User("002", "Nakrani")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)