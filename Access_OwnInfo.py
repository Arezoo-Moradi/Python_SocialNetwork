import module_show_file
from User import User
from Profile import Profile
import post
import csv
import Access_OwnInfo
import Access_AnotherInfo

def access_owninfo(user_name):

    while True:
        print('>>>>>>>>>>>>>>>>>>>>> Accesses to my own information of pages  >>>>>>>>>>>>>>>>>>>>>')
        print('1. access to posts 2.access to following 3.access to profile 4.change_password 5.exit')
        print('choose between 1,2,3,4,5')
        choice = input("please choose:")
        if choice == '1':
            print('>>>>>>>>>>>>>>>>>Access to Posts')
            print("1.create post 2.change post 3.delete post 4.show post 5.exit")
            choose = input('choose number:')
            if choose == "1":
                print('>>>>>>>>>>>>>Creat a post')
                txt = input('Enter text of the post:')
                post.Post.creat_post(user_name, txt)
            elif choose == "2":
                print('>>>>>>>>>>>>>Changed a post')
                post.Post.change_post(user_name)
            elif choose == "3":
                print('>>>>>>>>>>>>>Deleted a post')
                post.Post.delete_post(user_name)
            elif choose == "4":
                print('>>>>>>>>>>>>>>>>Show Post')
                post.Post.show_mypost(user_name)
            elif choose == "5":
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
            print('1-creat_profile 2- Edit_profile 3- show_profile 4-exit')
            print('please choose a number between 1,2,3,4')
            choise3 = input('Enter the number:')
            if choise3 == '1':
                print('>>>>>>>>>>>>>>>creat a Profile')
                Profile.creat_profile(user_name)
            elif choise3 == '2':
                print('>>>>>>>>>>>>>>>Edit profile')
                Profile.Edit_profile(user_name)
            elif choise3 == '3':
                print('>>>>>>>>>>>>>>>show profile')
                Profile.show_myprofile(user_name)
            elif choise3 == '4':
                break
        elif choice == '4':
            user = User(user_name, password, None, True)
            User.change_password(user)
        elif choice == '5':
            break
        else:
            print('Error: your choose is wrong!!')
        continue