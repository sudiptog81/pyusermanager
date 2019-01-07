"""
Sudipto Ghosh <sudipto.ghosh.pro>
"""

from datetime import datetime


class User():

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.type = "user"

    def saveprofile(self):
        file = open("database\\profiles.csv", "a")
        file.write(
            f"\n{self.type},{self.name},{self.age},{self.email},{datetime.now()}")
        file.close()


class Member(User):

    def __init__(self, name, age, email, memberId):
        super().__init__(name, age, email)
        self.memberId = memberId
        self.name = str(memberId) + " " + name
        self.type = "member"
