from User import User
from Profile import Profile
import datetime
import csv
import pandas as pd
from pathlib import Path
import module_show_file


class Post:
    '''
        In this class, the User can create, edit, and delete my posts.
        Users can also view and comment on each other's posts.
    '''

    post = []

    '''In this function, initialize attributes'''
    def __init__(self, text, date, production_time, comments, like, user_name=None, password=None, friends=None, log_in=None, email=None, phone_number=None, bio=None):
        """
        :param text: Contains post content
        :param date: Date the post was published
        :param production_time: Time the post is published
        :param number_comments: The number of comments that has each post
        """

        '''inherent attribute from User and Profile class and initialize'''
        '''User.__init__(self, user_name, password, friends, log_in)
        Profile.__init__(self, email, phone_number, bio)
'''
        self.text = text
        self.date = date
        self.production_time = production_time
        self.comments = comments
        self.like = like



    '''In this function, you can creat your posts and add your pages '''
    @classmethod
    def creat_post(cls, name, txt):
        file_path = "post_file.csv"
        df_post = pd.read_csv(file_path)
        df_post_indexed = df_post.set_index("id_post", drop=True)
        #todo txt delet shude
        d = datetime.datetime.today()
        date = d.strftime('%d-%m-%Y')
        production_time = d.strftime("%H:%M:%S")
        comments = None
        like = None

        row_post = [
            [name, df_post_indexed.index[-1] + 1, txt, date, production_time, comments, like]]

        with open(file_path, 'a', newline='') as csv_post:
            csv_writer = csv.writer(csv_post)
            # writing the data row
            csv_writer.writerows(row_post)
        post = cls(txt, date, production_time, None, None)
        return post

    '''In this function, you can edit or delete your post that you want '''
    def change_post(self, user_log):
        module_show_file.show_post_file(user_log)
        '''print('which post do you want to changed? please select the id of post?')
        id = input("Please enter the id of post:")
        #person = input('Enter the person that you want to changing his post:')
        new_txt = input("Please enter the new text:")'''

        post_changed = pd.read_csv('post_file.csv')
        location = 0
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            for row in reader:
                #if user_log == person:
                if row['user_name'] == user_log and row['id_post'] == id:
                    txt = new_txt
                    print("Your txt is changed.")
                    post_changed.loc[location, 'txt'] = txt
                    post_changed.to_csv('post_file.csv', index=False)
                location += 1
                '''else:
                    print('you can not changed posts another person!!!')
                    break'''

    @staticmethod
    def delete_post(user_log):
        module_show_file.show_post_file(user_log)

        lines = list()
        id = input("Please enter the id of post, you want to delete:")
        person = input('Enter the person that you want to delete his post:')
        with open('post_file.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if user_log == person:
                        if field == id:
                            lines.remove(row)
                            print('remove your post!')
                    else:
                        print('you can not delete posts another person!!!')

        with open('post_file.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    @staticmethod
    def add_comment(user_log, person):
        module_show_file.show_post_file(person)
        id = input('Enter id of post:')
        new_comments = input("Please enter the comment:")
        d = datetime.datetime.today()
        date_comment = d.strftime('%d-%m-%Y')
        time_comment = d.strftime("%H:%M:%S")
        add_com = pd.read_csv('post_file.csv')
        location = 0
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            for row in reader:
                if row['user_name'] == person and row['id_post'] == id:
                    comments = new_comments
                    print("Your comment is added.")
                    add_com.loc[location, 'user_log'] = user_log
                    add_com.loc[location, 'date_comment'] = date_comment
                    add_com.loc[location, 'time_comment'] = time_comment
                    add_com.loc[location, 'comments'] = comments
                    add_com.to_csv('post_file.csv', index=False)
                location += 1

    @staticmethod
    def show_mypost(user_log):
        print('show posts ')
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            print(f'<<<<<<<< {user_log} ----> logged and see my posts.')
            for row in reader:
                if row['user_name'] == user_log:
                    print(f"user_name:{row['user_name']}, Id of post: {row['id_post']} , text: {row['txt']}"
                          f" ,date: {row['date']} , production_time: {row['production_time']},"
                          f" comments: {row['comments']} , like: {row['like']} ")

    '''In this function, you can view and comment on each other's posts '''
    @staticmethod
    def show_post(user_log, person):
        print('show posts ')
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            print(f'>>>>>>>>{user_log} ----> logged and see your posts ----> {person}')
            for row in reader:
                if row['user_name'] == person:
                    print(f"user_name:{row['user_name']}, Id of post: {row['id_post']} , text: {row['txt']}"
                          f" ,date: {row['date']} , production_time: {row['production_time']},"
                          f" comments: {row['comments']} , like: {row['like']} ")

    @staticmethod
    def like(user_log, person):
        count_like = 0
        print('If you want to like post select 1 else select 2:')
        select = input('Enter your select:')
        if select == '1':
            add_like = pd.read_csv('post_file.csv')
            location = 0
            module_show_file.show_post_file(person)
            id = input('Enter id of post:')
            with open("post_file.csv", 'r') as post_file:
                reader = csv.DictReader(post_file)
                for row in reader:
                    if row['user_name'] == person and row['id_post'] == id:
                        count_like += 1
                        likes = count_like
                        print("You liked post.")
                        add_like.loc[location, 'user_log'] = user_log
                        add_like.loc[location, 'like'] = likes
                        add_like.to_csv('post_file.csv', index=False)
                    location += 1

        else:
            print('you dont like post!')

    @staticmethod
    def access_post(user_log, person):
        print('Add comment: select 1 >>>>>>>>')
        print('Add like: select 2 >>>>>>>>>>')
        select = input('Enter select:')
        if select == '1':
            print(">>>> add comment")
            Post.add_comment(user_log, person)
        elif select == '2':
            print(">>>> add like")
            Post.like(user_log, person)
        else:
            print('you dont add comment or liked the post!')










