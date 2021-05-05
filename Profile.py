from User import User
import csv
from pathlib import Path

class Profile:
    '''
            In this class, you can initialize your profile.
            Users can also view each other's profiles.
    '''

    profile_list = []
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

    @staticmethod
    def creat_profile(name):
        print('------------------------ creat a profile --------------------------')
        id = input(' **Enter** id')
        email = input('Enter your email:')
        phone_number = input('Enter phone_number:')
        bio = input('Enter your bio:')

        with open('profile_file.csv', 'a') as file_post:
            fields_name = ['id', 'user_name', 'email', 'phone_number', 'bio']
            csv_writer = csv.DictWriter(file_post, fieldnames=fields_name)
            if Path('profile_file.csv').stat().st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow({'id': id, 'user_name': name, 'email': email,
                                 'phone_number': phone_number, 'bio': bio})
        profile = Profile(email, phone_number, bio, name, None, None, None)
        Profile.profile_list.append(profile)
        return profile

    '''In this function,you can view each other profile'''
    @staticmethod
    def show_profile(name):
        with open("profile_file.csv", 'r') as profile_file:
            reader = csv.DictReader(profile_file)
            for row in reader:
                if row['user_name'] == name:
                    print(f"Id of profile: {row['id']} , user_name: {row['user_name']}"
                          f" email: {row['email']} , phone_number: {row['phone_number']}"
                          f" 'bio': {row['bio']}.")
