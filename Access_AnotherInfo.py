import module_show_file
from User import User
from Profile import Profile
import post
import csv
import Access_OwnInfo
import Access_AnotherInfo

def access_anotherinfo(user_name):

    while True:
        print('>>>>>>>>>>>>>>>>>>>>> Access someone another page  >>>>>>>>>>>>>>>>>>>>>')
        print('1. see another posts 2. See another profile 3.exit')
        print('choose between 1,2,3')
        select = input("Enter select:")
        if select == '1':
            print('>>>>>>>>>>>>>>>>>>>>>>>>>> show posts each other')
            print('Whose posts do you want to see?')
            module_show_file.show_userInfo()
            person = input('select person:')
            print('>>>>>>>>>>>>>>>See posts another person')
            post.Post.show_post(user_name, person)
            print('Do you want to like or add comments?')
            print('Add like or comment select 1 else select 2 ......')
            select = input('Enter select:')
            if select == '1':
                print('>>>>>>>>>>>>Add comment or like for post each other')
                post.Post.access_post(user_name, person)
            else:
                break
        elif select == '2':
            print('>>>>>>>>>>>>>>>>>> show profile each other')
            module_show_file.show_userInfo()
            print('Whose profile do you want to see?')
            person = input('select person:')
            Profile.show_profile(user_name, person)
        elif select == '3':
            break
        else:
            print('Error: your choose is wrong!!')
        continue