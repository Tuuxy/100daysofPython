class User:

    def __init__(self, user_id, username):
        self.id = user_id 
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1,"Tuuxy")
user_2 = User(2,"Karys")

user_1.follow(user_2)

print(f"User ID: {user_1.id}, {user_1.username} followers: {user_1.followers}, following: {user_1.following}")
print(f"User ID: {user_2.id}, {user_2.username} followers: {user_2.followers}, following: {user_2.following}")