import log
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

    """ In this function, initialize attributes """
    def __init__(self, email, phone_number, bio, user_name=None, password=None, friends=None, log_in=None):
        """
        :param email: email of the user that saved in the profile
        :param phone_number: phone_number of the user that saved in the profile
        :param bio: bio of the user that saved in the profile
        """

        self.email = email
        self.phone_number = phone_number
        self.bio = bio

    '''In this function, creat a profile for user name that logged'''
    @classmethod
    def creat_profile(cls, user_name):
        while True:
            phone_number_format = '^9[\d]{9}$'
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
            print("you have not this file please create a file with name profile_file.csv "
                  "and set first row with this items (user_name,email,phone_number,bio)")
        profile = cls(email, phone_number, bio, user_name, None, None, None)
        return profile

    '''In this function, set new email'''
    def set_email(self, new_email):
        email_format = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not re.search(email_format, new_email):
            print('incorrect email address format!')
        else:
            self.email = new_email

    '''In this function, set new phone number'''
    def set_phone_number(self, new_phone):
        phone_number_format = '^9[\d]{9}$'
        if not re.search(phone_number_format, new_phone):
            print('incorrect phone number format!')
        else:
            self.phone_number = new_phone

    '''In this function, set new bio '''
    def set_bio(self, new_bio):
        self.bio = new_bio

    '''In this function, edited profile that created before...'''
    def edit_profile(self, select, new_email=None, new_phone=None, new_bio=None):
        if select == '1':
            self.update_email(new_email)
            return self
        elif select == '2':
            self.update_phone(new_phone)
            return self
        elif select == '3':
            self.update_bio(new_bio)
            return self
        else:
            print("your choose is wrong!")

    '''In this function, updated email of profile and changed value in profile_file.csv'''
    def update_email(self, new_email):
        try:
            post_changed = pd.read_csv('profile_file.csv')
            location = 0
            with open('profile_file.csv', 'r+') as profile_file:
                reader = csv.DictReader(profile_file)
                for row in reader:
                    if row['email'] == self.email:
                        log.info_logger.info(f'profile with email:{self.email} is update.')
                        self.set_email(new_email)
                        print("Your email is changed.")
                        email = self.email
                        post_changed.loc[location, 'email'] = email
                        post_changed.to_csv('profile_file.csv', index=False)
                    location += 1
        except Exception:
            print("you can not open this file and changed these value please check a file with name profile_file.csv "
                  "is exists and what happened!! ")

    '''In this function, updated phone number of profile and changed value in profile_file.csv'''
    def update_phone(self, new_phone):
        try:
            post_changed = pd.read_csv('profile_file.csv')
            location = 0
            with open('profile_file.csv', 'r+') as profile_file:
                reader = csv.DictReader(profile_file)
                for row in reader:
                    print(self.phone_number)
                    if row['phone_number'] == self.phone_number:
                        log.info_logger.info(f'profile with phone number:{self.phone_number} is update.')
                        self.set_phone_number(new_phone)
                        print('////////', self.phone_number)
                        print("Your phone number is changed.")
                        phone = self.phone_number
                        print('>>>>>>>', phone)
                        post_changed.loc[location, 'phone_number'] = phone
                        post_changed.to_csv('profile_file.csv', index=False)
                    location += 1
        except Exception:
            print("you can not open this file and changed these value please check a file with name profile_file.csv "
                  "is exists and what happened!! ")

    '''In this function, updated bio of profile and changed value in profile_file.csv'''
    def update_bio(self, new_bio):
        try:
            post_changed = pd.read_csv('profile_file.csv')
            location = 0
            with open('profile_file.csv', 'r+') as profile_file:
                reader = csv.DictReader(profile_file)
                for row in reader:
                    print(self.bio)
                    if row['bio'] == self.bio:
                        log.info_logger.info(f'profile with bio:{self.bio} is update.')
                        self.set_bio(new_bio)
                        print('////////', self.bio)
                        print("Your bio is changed.")
                        bio = self.bio
                        print('>>>>>>>', bio)
                        post_changed.loc[location, 'bio'] = bio
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
            print("you have not this file please create a file with name profile_file.csv"
                  " and set first row with this items (user_name,email,phone_number,bio)")

    '''In this function, view my profile  '''
    def show_my_profile(self):
        print(f'<<<<<<<<<<<<<<< {self.user_name} --->logged and see my profile.')
        module_show_file.show_profInfo(self.user_name)

    '''In this function, view each other profile'''
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

    '''In this function, checked the user name created a profile before! '''
    @staticmethod
    def check_profile(user_name):
        with open("profile_file.csv", 'r') as user_file:
            reader = csv.DictReader(user_file)
            for row in reader:
                if row['user_name'] == user_name:
                    return 0
            else:
                return 1

