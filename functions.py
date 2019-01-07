"""
Sudipto Ghosh <sudipto.ghosh.pro>
"""

from classes import User, Member
from random import randint
from sys import exit
from pandas import read_csv


def getUserInfo():
    """
    Prompt the user for input
    """
    name = str(input("Name: "))
    age = int(input("Age: "))
    email = str(input("E-mail: "))
    user = User(name, age, email)
    print(f"User Registration Successful for {user.name}")
    user.saveprofile()


def getMemberInfo():
    """
    Prompt the member for input
    """
    name = str(input("Name: "))
    age = int(input("Age: "))
    email = str(input("E-mail: "))
    memberId = randint(10000, 1000000)
    member = Member(name, age, email, memberId)
    print(
        f"Member Registration Successful for {member.name}")
    member.saveprofile()


def printDB():
    """
    Print data from data store
    """
    db = read_csv("database\\profiles.csv").drop(
        ['timestamp', 'email'], axis=1)
    print(db)


def __init__():
    """
    Initialize the application
    """
    choice = str(input("Intention (user or member): "))
    if choice == "user":
        getUserInfo()
    elif choice == "member":
        getMemberInfo()
        printDB()
    else:
        print("invalid intention")
    exit_choice = str(input("Restart (r) Quit (q) : "))
    if exit_choice == "r":
        __init__()
    else:
        exit()
