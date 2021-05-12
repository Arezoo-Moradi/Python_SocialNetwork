import csv
import module_show_file
import datetime
import csv
import pandas as pd
from pathlib import Path
import re
import pandas as pd

def update_csv(file_path, value_to_update,updated_value):
    df = pd.read_csv(file_path)
    df.replace(to_replace=value_to_update, value=updated_value, inplace=True)
    df.to_csv(file_path, mode='w')

def Edit_profile(user_log):
    module_show_file.show_profInfo(user_log)
    with open("profile_file.csv", 'r') as prof_file:
        reader = csv.DictReader(prof_file)
        for row in reader:
            email = row['email']
            phone_number = row['phone_number']
            bio = row['bio']

    print('select changed---> 1.email 2.phone number 3.bio 4.Exit')
    select = input('select number:')
    if select == '1':
        while True:
            email_format = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            new_email = input('Enter update email address:')
            if not re.search(email_format, new_email):
                print('incorrect email address format!')
            else:
                break
        update_csv('profile_file.csv', email, new_email)
        print('update your email!!!!')

    elif select == '2':
        while True:
            phone_number_format = '^09[\d]{9}$'
            new_phone_number = input('Enter your phone number:')
            if not re.search(phone_number_format, new_phone_number):
                print('incorrect phone number format!')
            else:
                break
        update_csv('profile_file.csv', phone_number, new_phone_number)
        print('update your phone number!!!!')
    elif select == '3':
        new_bio = input('Enter new bio:')
        update_csv('profile_file.csv', bio, new_bio)
        print('update your bio!')
    else:
        print('you do not update value!!!!!')




Edit_profile('sasi')