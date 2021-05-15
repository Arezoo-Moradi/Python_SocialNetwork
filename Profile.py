from User import User
import csv
from pathlib import Path
import re
import pandas as pd
import module_show_file

class Profile:
    '''
            In this class, you can initialize your profile.
            Users can also view each other's profiles.
    '''

    # profile_list = []
    """ In this function, initialize attributes """
    def __init__(self, email, phone_number, bio, user_name=None, password=None, friends=None, log_in=None):
        """

        :param email: email of the user that saved in the profile
        :param phone_number: phone_number of the user that saved in the profile
        :param bio: bio of the user that saved in the profile
        """

        '''inherent attribute from User class and initialize'''
        User.__init__(self, user_name, password, friends, log_in)

        self.email = email
        self.phone_number = phone_number
        self.bio = bio

    @classmethod
    def creat_profile(cls, user_name):
        while True:
            phone_number_format = '^09[\d]{9}$'
            phone_number = input('Enter your phone number:')
            if not re.search(phone_number_format, phone_number):
                print('incorrect phone number format!')
            else:
                break
        while True:
            email_format = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            email = input('Enter your email address:')
            if not re.search(email_format, email):
                print('incorrect email address format!')
            else:
                break
        bio = input('Enter your bio:')
        try:
            with open('profile_file.csv', 'a') as file_post:
                fields_name = ['user_name', 'email', 'phone_number', 'bio']
                csv_writer = csv.DictWriter(file_post, fieldnames=fields_name)
                if Path('profile_file.csv').stat().st_size == 0:
                    csv_writer.writeheader()
                csv_writer.writerow({'user_name': user_name, 'email': email,
                                     'phone_number': phone_number, 'bio': bio})
        except Exception:
            print("you have not this file please create a file with name profile_file.csv and set first row with this items "
                  "(user_name,email,phone_number,bio)")
        profile = cls(email, phone_number, bio, user_name, None, None, None)
        return profile

    def set_email(self, new_email):
        email_format = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not re.search(email_format, new_email):
            print('incorrect email address format!')
        else:
            self.email = new_email

    def set_phone_number(self, new_phone):
        phone_number_format = '^09[\d]{9}$'
        if not re.search(phone_number_format, new_phone):
            print('incorrect phone number format!')
        else:
            self.phone_number = new_phone

    def set_bio(self, new_bio):
        self.bio = new_bio

    def edit_profile(self, select, new_email=None, new_phone=None, new_bio=None):
        try:
            if select == '1':
                self.set_email(new_email)
                self.update_file()
            elif select == '2':
                self.set_phone_number(new_phone)
                self.update_file()
            elif select == '3':
                self.bio == new_bio
                self.update_file()
            elif select == '4':
                self.set_email(new_email)
                self.set_phone_number(new_phone)
                self.bio == new_bio
                self.update_file()
            else:
                print("your choose is wrong!")
        except Exception:
            print("your choose is wrong! Try again..")

    def update_file(self):
        try:
            post_changed = pd.read_csv('profile_file.csv')
            location = 0
            with open('profile_file.csv', 'r') as profile_file:
                reader = csv.DictReader(profile_file)
                for row in reader:
                    if row['email'] == self.email:
                        self.email == self.set_email()
                        print("Your email is changed.")
                        post_changed.loc[location, 'email'] = self.email
                        post_changed.to_csv('profile_file.csv', index=False)
                        location += 1
                    elif row['phone_number'] == self.phone_number:
                        self.phone_number == self.set_phone_number()
                        print("Your phone_number is changed.")
                        post_changed.loc[location, 'phone_number'] = self.phone_number
                        post_changed.to_csv('profile_file.csv', index=False)
                        location += 1
                    elif row['bio'] == self.bio:
                        self.bio == self.set_bio()
                        print("Your bio is changed.")
                        post_changed.loc[location, 'bio'] = self.bio
                        post_changed.to_csv('profile_file.csv', index=False)
                        location += 1
        except Exception:
            print("you can not open this file and changed these value please check a file with name profile_file.csv "
                  "is exists and what happened!! ")

    def add_to_file(self):
        try:
            with open('profile_file.csv', 'a') as file_post:
                fields_name = ['user_name', 'email', 'phone_number', 'bio']
                csv_writer = csv.DictWriter(file_post, fieldnames=fields_name)
                if Path('profile_file.csv').stat().st_size == 0:
                    csv_writer.writeheader()
                csv_writer.writerow({'user_name': self.user_name, 'email': self.email,
                                     'phone_number': self.phone_number, 'bio': self.bio})
        except Exception:
            print("you have not this file please create a file with name profile_file.csv and set first row with this items "
                  "(user_name,email,phone_number,bio)")

    '''In this function,you can view each other profile'''
    def show_my_profile(self):
        print(f'<<<<<<<<<<<<<<< {self.user_name} --->logged and see my profile.')
        module_show_file.show_profInfo(self.user_name)


    def show_profile(self, person):
        try:
            with open("profile_file.csv", 'r') as profile_file:
                reader = csv.DictReader(profile_file)
                print(f'<<<<<<<<<<<<<<< {self.user_name} ----> logged and see your profile --->>>{person}')
                for row in reader:
                    if row['user_name'] == person:
                        print(f"user_name: {row['user_name']}"
                              f" email: {row['email']} , phone_number: {row['phone_number']}"
                              f" 'bio': {row['bio']}.")
        except Exception:
            print("you can not open this file and show these value please check a file with name profile_file.csv "
                  "is exists and what happened!! ")





