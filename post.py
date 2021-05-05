from User import User
from Profile import Profile
import datetime
import csv
import pandas as pd
from pathlib import Path


class Post:
    '''
        In this class, the User can create, edit, and delete my posts.
        Users can also view and comment on each other's posts.
    '''

    post_id = []

    '''In this function, initialize attributes'''
    def __init__(self, id_post, text, date, production_time, comments, like, user_name=None, password=None, friends=None, log_in=None, email=None, phone_number=None, bio=None):
        """
        :param text: Contains post content
        :param date: Date the post was published
        :param production_time: Time the post is published
        :param number_comments: The number of comments that has each post
        """

        '''inherent attribute from User and Profile class and initialize'''
        User.__init__(self, user_name, password, friends, log_in)
        Profile.__init__(self, email, phone_number, bio)

        self.id_post = id_post
        self.text = text
        self.date = date
        self.production_time = production_time
        self.comments = comments
        self.like = like

    '''In this function, you can creat your posts and add your pages '''
    @staticmethod
    def creat_post(name):
        id_post = input('Enter id of the post:')
        txt = input('Enter text of the post:')
        Post.post_id.append(id_post)
        d = datetime.datetime.today()
        date = d.strftime('%d-%m-%Y')
        production_time = d.strftime("%H:%M:%S")
        comments = None
        like = None
        with open('post_file.csv', 'a') as file_post:
            fields_name = ['user name','id_post', 'txt', 'date', 'production_time', 'comments', 'like']
            csv_writer = csv.DictWriter(file_post, fieldnames=fields_name)
            if Path('post_file.csv').stat().st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow({'user name': name, 'id_post': id_post, 'txt': txt, 'date': date,
                                 'production_time': production_time, 'comments': comments, 'like': like})
        post = Post(id_post, txt, date, production_time, None, None)
        return post

    '''In this function, you can edit or delete your post that you want '''
    @staticmethod
    def change_post(name):
        post_changed = pd.read_csv('post_file.csv')
        location = 0
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            for row in reader:
                print(f"user name: {row['user name']}, Id of post: {row['id_post']} , text: {row['txt']} .")
        print('which post do you want to changed? please select the id of post?')
        id = input("Please enter the id of post:")
        new_txt = input("Please enter the new text:")

        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            for row in reader:
                if row['user name'] == name and row['id_post'] == id:
                    txt = new_txt
                    print("Your txt is changed.")
                    post_changed.loc[location, 'txt'] = txt
                    post_changed.to_csv('post_file.csv', index=False)
                location += 1

    @staticmethod
    def delete_post(name):
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            for row in reader:
                print(f"user name:{row['user name']}, Id of post: {row['id_post']} , text: {row['txt']} .")

        lines = list()
        id = input("Please enter the id of post, you want to delete:")
        with open('post_file.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == id:
                        lines.remove(row)
                        print('remove your post!')

        with open('post_file.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    @staticmethod
    def add_comment(name):
        add_com = pd.read_csv('post_file.csv')
        location = 0
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            for row in reader:
                print(f"user name:{row['user name']}, Id of post: {row['id_post']} , text: {row['txt']} .")
        id = input('Enter id of post:')
        new_comments = input("Please enter the comment:")
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            for row in reader:
                if row['user name'] == name and row['id_post'] == id:
                    comments = new_comments
                    print("Your comment is added.")
                    add_com.loc[location, 'comments'] = comments
                    add_com.to_csv('post_file.csv', index=False)
                location += 1

    '''In this function, you can view and comment on each other's posts '''
    @staticmethod
    def show_post(name):
        print('show posts ')
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            for row in reader:
                if row['user name'] == name:
                    print(f"user name:{row['user name']}, Id of post: {row['id_post']} , text: {row['txt']}"
                          f" ,date: {row['date']} , production_time: {row['production_time']},"
                          f" comments: {row['comments']} , like: {row['like']} ")

    @staticmethod
    def like(name):
        count_like = 0
        print('If you want to like post select 1 else select 2:')
        select = input('Enter your select:')
        if select == '1':
            add_like = pd.read_csv('post_file.csv')
            location = 0
            with open("post_file.csv", 'r') as post_file:
                reader = csv.DictReader(post_file)
                for row in reader:
                    print(f"user name:{row['user name']}, Id of post: {row['id_post']}.")
            id = input('Enter id of post:')
            with open("post_file.csv", 'r') as post_file:
                reader = csv.DictReader(post_file)
                for row in reader:
                    if row['user name'] == name and row['id_post'] == id:
                        count_like += 1
                        likes = count_like
                        print("You liked post.")
                        add_like.loc[location, 'like'] = likes
                        add_like.to_csv('post_file.csv', index=False)
                    location += 1

        else:
            print('you dont like post!')

    @staticmethod
    def access_post(name):
        print('Add comment: select 1 >>>>>>>>')
        print('Add like: select 2 >>>>>>>>>>')
        select = input('Enter select:')
        if select == '1':
            print(">>>> add comment")
            Post.add_comment(name)
        elif select == '2':
            print(">>>> add like")
            Post.like(name)
        else:
            print('you dont add comment or liked the post!')










