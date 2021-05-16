'''
                                    created by: Arezoo Moradi
'''
import log
import module_show_file
from User import User
from Profile import Profile
import post
import csv
import Access_OwnInfo
import Access_AnotherInfo

NAME = input("Please Enter your name:")
print("*****\||/***** Welcome:", NAME)
while True:
    print("1. Sign in ")
    print("2. Sign up ")
    print("3. Exit")
    print('************ please choose a number between 1,2,3  **************')
    choise = input('Enter the number:')

    user = None
    if choise == '1':
        print('********** ********* ********* 1-register 2.login *********** ************ ************')
        print('*********** ************** please choose a number between 1,2 ************ ************')
        choise1 = input('Enter the number:')
        """--------------------------------------------------------------------------------------"""
        if choise1 == '1':
            print('>>>>>>>>>>>>>>>>>>>>Register')
            user_name = input("Enter User Name:").lower()
            check = User.check_user(user_name)
            if check:
                password = input("Enter Password:").lower()
                confirm = input("Enter Password again:").lower()
                person = User.register(user_name, password, confirm)
                log.info_logger.info(f"user with user_name: {user_name} register.")
            else:
                print(f'{user_name} ---->>>> is register before!')

        elif choise1 == '2':
            print('>>>>>>>>>>>>>>>>>>>>>Log in')
            user_name = input('please enter your user_name:')
            password = int(input("please enter your password:"))
            is_logged_in = User.login(user_name, password)
            if is_logged_in == False:
                print("Enter your password wrong! Try again...")
            elif is_logged_in == True:
                user = User(user_name, password, None, True)
                print('Access to my pages and information select 1 >>>>>> ')
                print('Access someone another page select 2 >>>>>>>>>>>>>>')
                select = input('Enter your select:')
                if select == '1':
                    Access_OwnInfo.access_owninfo(user)
                elif select == '2':
                    Access_AnotherInfo.access_anotherinfo(user)
                else:
                    print('your choice is wrong!!')
                    continue

        """-----------------------------------------------------------------------------------------"""
    elif choise == '2':
        User.logout(user)
    else:
        break







