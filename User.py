import csv
import basehash
import pandas as pd
from pathlib import Path
import module_show_file

class User:

    '''
    In This class, users can register or log in also
     you can follow your friends or let your friends to follow you.
    '''

    user_list = []
    friends_list = []
    hash_fn = basehash.base36()

    '''In this function: initialize attributes'''
    def __init__(self, user_name, password, friends, login_flg):
        '''
        :param user_name: Name of user
        :param password: password of user
        :param friends: friends of user
        '''

        self.user_name = user_name
        self.password = password
        self.friends = friends
        self.login_flg = login_flg

    '''In this function,you can log out to your page'''
    def logout(self):
        try:
            assert self.login_flg
            self.login_flg = False
            print('Logged out successfully...')
        except:
            print('You are not logged in yet!')

    '''In this function,changed your password'''
    def change_password(self):
        change = pd.read_csv('User_Information.csv')
        location = 0
        new_password = input("Please enter new password:")
        hash_old_pass = User.hash_fn.hash(self.password)
        hash_new_pass = User.hash_fn.hash(new_password)

        with open("User_Information.csv", 'r') as user_file:
            reader = csv.DictReader(user_file)
            for row in reader:
                if row['user_name'] == self.user_name and row['password'] == hash_old_pass:
                    self.password = hash_new_pass
                    print("Your password is changed.")
                    change.loc[location, 'password'] = hash_new_pass
                    change.to_csv('User_Information.csv', index=False)
                location += 1

    '''In this function, you can follow your friends '''
    @staticmethod
    def following():
        try:
            user_name = input("please enter user_name that you want to follow:")
            obj_user_name = next(element for element in User.user_list if element.user_name == user_name)
            User.friends_list.append(obj_user_name)
        except:
            print('You have no desire to following anyone')

        with open('following_list.csv', 'a', newline='') as following_data:
            fields_name = ['user_name']
            csv_writer = csv.DictWriter(following_data, fieldnames=fields_name)
            if Path('following_list.csv').stat().st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow({'user_name': user_name})
        return User.friends_list

    '''In this function, you can unfollow your friends '''
    @staticmethod
    def unfollow():
        print('********* show your following ************')
        module_show_file.following_list()
        print('Who do you want to unfollow?')
        person = input('Enter your user name:')
        lines = list()

        with open('following_list.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == person:
                        lines.remove(row)
                        print('unfollow your friend!')
        with open('following_list.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    @staticmethod
    def menu_following():
        print("Suggested list of people you can follow: ")
        print('user_name:')
        for i in User.user_list:
            print(f'{i.user_name}')
        while True:
            print('1- follow 2- unfollow 3-Exit :')
            follow = input('enter choose to follow or unfollow:')
            if follow == '1':
                print('Who do you want to follow?')
                User.following()
            elif follow == '2':
                User.unfollow()
            elif follow == '3':
                break
            continue

    @staticmethod
    def show_following():
        module_show_file.following_list()

    '''In this function, you can register and go to your page'''
    @staticmethod
    def register():
        count = 0
        '''Enter your information of user from input'''
        user_name = input("Enter User Name:").lower()
        password = input("Enter Password:").lower()
        confirm = input("Enter Password again:").lower()

        if password == confirm:
            password = confirm

            '''hashing your password'''
            pass_hash = User.hash_fn.hash(password)
            #print("*****Welcome to your account that created*****")

        '''If enter your password wrong you can just try 3 times'''
        while password != confirm and count < 3:
            my_user = user_name
            print("your password is wrong try a gain!!")
            print('user_name:', my_user)
            confirm = input("verify password again:")
            if count == 2:
                print('try againes after 10 minute your access is lucked')
            if password == confirm:
                break
            count += 1

        '''Save Information of users in User_Information file'''
        with open('User_Information.csv', 'a', newline='') as user_data:
            fields_name = ['user_name', 'password']
            csv_writer = csv.DictWriter(user_data, fieldnames=fields_name)
            if Path('User_Information.csv').stat().st_size == 0:
                csv_writer.writeheader()
            if not 'user_name':
                csv_writer.writerow({'user_name': user_name, 'password': pass_hash})
                print("*****Welcome to your account that created*****")
            else:
                print('This user name is register before!')

        user = User(user_name, password, None, None)
        User.user_list.append(user)
        return user

    ''' In this function,you can log in to your page'''
    @staticmethod
    def login(user_name, password):
        '''check the user name or password is exist'''
        with open("User_Information.csv", 'r') as user_file:
            reader = csv.reader(user_file)
            for row in reader:
                if user_name == row[0]:
                    if password == User.hash_fn.unhash(row[1]):
                        User.login_flg = True
                        print("welcome to your page...")
                        return True
                        break
                    else:
                        User.login_flg = False
                        return False


