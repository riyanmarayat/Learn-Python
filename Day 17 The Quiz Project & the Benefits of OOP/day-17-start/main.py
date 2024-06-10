# Part 155 How to create your own Class in Python
# class User:
#     pass
#
#
# user_1 = User()

# Part 156 Working with Attributes, Class Constructors and the __init__() Function
# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#
#
# user_1 = User("001", "angela")
#
# print(user_1.username)
#
# user_2 = User("002", "jack")

# Part 157 Adding Methods to a Class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)