import module_show_file
from User import User
from Profile import Profile
from post import Post
import csv
import Access_OwnInfo
import Access_AnotherInfo

def access_anotherinfo(user):

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
            user.post = Post.show_post(user, person)
            print('Do you want to like or add comments?')
            print('Add like or comment select 1 else select 2 ......')
            select = input('Enter select:')
            if select == '1':
                print('>>>>>>>>>>>>Add comment or like for post each other')
                print('Add comment: select 1 >>>>>>>>')
                print('Add like: select 2 >>>>>>>>>>')
                select = input('Enter select:')
                if select == '1':
                    module_show_file.show_post_file(person)
                    id = input('Enter id of post:')
                    new_comments = input("Please enter the comment:")
                    user.post = Post.access_post(user.user_name, person, select, id, new_comments)
                elif select == '2':
                    print('If you want to like post select 1 else select 2:')
                    select1 = input('Enter your select:')
                    if select1 == '1':
                        module_show_file.show_post_file(person)
                        id = input('Enter id of post:')
                        user.post = Post.access_post(user.user_name, person,select, id, None)
                    else:
                        print('you dont like post!')

            else:
                break
        elif select == '2':
            print('>>>>>>>>>>>>>>>>>> show profile each other')
            module_show_file.show_userInfo()
            print('Whose profile do you want to see?')
            person = input('select person:')
            user.profile = Profile.show_profile(user, person)
        elif select == '3':
            break
        else:
            print('Error: your choose is wrong!!')
        continue