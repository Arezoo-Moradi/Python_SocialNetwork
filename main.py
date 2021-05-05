'''
                                    created by: Arezoo Moradi
'''

from User import User
from Profile import Profile
import post
import csv

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
        print('**********1-register 2.login 3.show post 4.show profile 5.change_password : ************')
        print('*********** please choose a number between 1,2,3,4,5 ************')
        choise1 = input('Enter the number:')
        """--------------------------------------------------------------------------------------"""
        if choise1 == '1':
            print('>>>>>>>>>>>>>>>>>>>>Register')
            person = User.register()
        elif choise1 == '2':
            print('>>>>>>>>>>>>>>>>>>>>>Log in')
            user_name = input('please enter your user_name:')
            password = int(input("please enter your password:"))
            user = User.login(user_name, password)
            user_name = user.user_name
            if user:
                while True:
                    print('>>>>>>>>>>>>>>>>>>>>>>>>> Accesses >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    print('1. access to posts 2.access to following 3.access to profile 4.exit')
                    print('choose between 1,2,3,4')
                    choice = input("please choose:")
                    if choice == '1':
                        print('>>>>>>>>>>>>>>>>>Access to Posts')
                        print("1.create post 2.change post 3.delete post 4.add comment 5.show post 6.exit")
                        choose = input('choose number:')
                        if choose == "1":
                            print('>>>>>>>>>>>>>Creat a post')
                            post.Post.creat_post(user_name)
                        elif choose == "2":
                            print('>>>>>>>>>>>>>Changed a post')
                            post.Post.change_post(user_name)
                        elif choose == "3":
                            print('>>>>>>>>>>>>>Deleted a post')
                            post.Post.delete_post(user_name)
                        elif choose == "4":
                            print('>>>>>>>>>>>>>Added Comment')
                            post.Post.add_comment(user_name)
                        elif choose == "5":
                            print('>>>>>>>>>>>>>>>>Show Post')
                            post.Post.show_post(user_name)
                        elif choose == "6":
                            break
                    elif choice == '2':
                        print('>>>>>>>>>>>>>>>>>>In this section you can follow person and show following')
                        print("1-following 2-show following 3-exit")
                        print('please choose a number between 1,2,3')
                        choise2 = input('Enter the number:')
                        if choise2 == '1':
                            User.menu_following()
                        elif choise2 == '2':
                            print('>>>>>>>>>>>>>>>>>>>>>>Show following')
                            User.show_following()
                        elif choise2 == '3':
                            break
                    elif choice == '3':
                        print('>>>>>>>>>>>>>>>Access to profile')
                        print('1-creat_profile 2- show_profile 3-exit')
                        print('please choose a number between 1,2,3')
                        choise3 = input('Enter the number:')
                        if choise3 == '1':
                            print('>>>>>>>>>>>>>>>creat a Profile')
                            Profile.creat_profile(user_name)
                        elif choise3 == '2':
                            print('>>>>>>>>>>>>>>>show profile')
                            Profile.show_profile(user_name)
                        elif choise3 == '3':
                            break
                    elif choice == '4':
                        break
            else:
                print('Enter your password wrong! Try again...')

        elif choise1 == '3':
            print('>>>>>>>>>>>>>>>>>>>>>>>>>> show posts each other')
            print('Whose posts do you want to see?')
            with open("User_Information.csv", 'r') as user_file:
                reader = csv.DictReader(user_file)
                for row in reader:
                    print(f"user name:{row['user_name']}")
            person = input('select person:')
            print('>>>>>>>>>>>>>>>See posts another person')
            post.Post.show_post(person)
            print('Do you want to like or add comments?')
            print('Add like or comment select 1 else select 2 ......')
            select = input('Enter select:')
            if select == '1':
                print('>>>>>>>>>>>>Add comment or like for post each other')
                post.Post.access_post(person)
            else:
                break

        elif choise1 == '4':
            print('>>>>>>>>>>>>>>>>>> show profile each other')
            with open("User_Information.csv", 'r') as user_file:
                reader = csv.DictReader(user_file)
                for row in reader:
                    print(f"user name:{row['user_name']}")
            print('Whose profile do you want to see?')
            person = input('select person:')
            Profile.show_profile(person)

        elif choise1 == '5':
            User.change_password(person)
        else:
            print('Error: your choose is wrong!!')
        continue

        """-----------------------------------------------------------------------------------------"""
    elif choise == '2':
        if user:
            user.logout()
        else:
            print('you are not log in!')
    else:
        break







