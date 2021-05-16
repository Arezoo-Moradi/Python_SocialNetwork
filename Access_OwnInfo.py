import module_show_file
from User import User
from Profile import Profile
from post import Post
import csv
import Access_OwnInfo
import Access_AnotherInfo

def access_owninfo(user):

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
                user.post = Post.creat_post(user.user_name, txt)
            elif choose == "2":
                print('>>>>>>>>>>>>>Changed a post')
                print('////////////////////////')
                module_show_file.show_post_file(user.user_name)
                print('////////////////////////')
                print('which post do you want to changed? please select the id of post?')
                id = input("Enter the id of post:")
                new_txt = input("Please enter the new text:")
                user.post = Post.change_post(user, new_txt, id)
            elif choose == "3":
                print('>>>>>>>>>>>>>Deleted a post')
                module_show_file.show_post_file(user.user_name)
                print('which post do you want to deleted? please select the id of post?')
                id = input("Enter the id of post:")
                user.post = Post.delete_post(user, id)
            elif choose == "4":
                print('>>>>>>>>>>>>>>>>Show Post')
                user.post = Post.show_my_post(user)
            elif choose == "5":
                break
        elif choice == '2':
            print('>>>>>>>>>>>>>>>>>>In this section you can follow person and show following')
            print("1-following 2-show following 3-exit")
            print('please choose a number between 1,2,3')
            choise2 = input('Enter the number:')
            if choise2 == '1':
                user.menu_following()
            elif choise2 == '2':
                print('>>>>>>>>>>>>>>>>>>>>>>Show following')
                user.show_following()
            elif choise2 == '3':
                break
        elif choice == '3':
            print('>>>>>>>>>>>>>>>Access to profile')
            print('1-creat_profile 2- show_profile 3-exit')
            print('please choose a number between 1,2,3')
            choise3 = input('Enter the number:')
            if choise3 == '1':
                check = Profile.check_profile(user.user_name)
                if check:
                    print('>>>>>>>>>>>>>>>creat a Profile')
                    user.profile = Profile.creat_profile(user.user_name)
                    print('Edited profile that created 1-edit 2-no edit')
                    choise = input('enter your choise:')
                    if choise == '1':
                        print('>>>>>>>>>>>>>>>Edit profile')
                        print('select Edited 1-email 2-phone 3-bio 4- Exit')
                        while True:
                            select = input('Enter your select:')
                            if select == '1':
                                email = input('Enter new email:')
                                user.profile = Profile.edit_profile(user.profile, select, email, None, None)
                                continue
                            elif select == '2':
                                phone = input('Enter new phone:')
                                user.profile = Profile.edit_profile(user.profile, select, new_phone=phone, new_email=None, new_bio=None)
                                continue
                            elif select == '3':
                                bio = input('Enter new bio:')
                                user.profile = Profile.edit_profile(user.profile, select,  new_bio=bio, new_phone=None, new_email=None,)
                                continue
                            elif select == '4':
                                break
                            else:
                                print('your select is wrong!')

                    elif choise == '2':
                        break
                else:
                    print(f'This profile is exists for the ---->{user.user_name}! '
                          f'you can not creat again profile for his/her!')
            elif choise3 == '2':
                print('>>>>>>>>>>>>>>>show profile')
                user.profile = Profile.show_my_profile(user)
            elif choise3 == '3':
                break
        elif choice == '4':
            user.change_password()

        elif choice == '5':
            break
        else:
            print('Error: your choose is wrong!!')
        continue