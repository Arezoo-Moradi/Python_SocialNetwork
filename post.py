import log
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

    '''In this function, initialize attributes'''
    def __init__(self, text, date, production_time, comments, like, user_name=None, password=None, friends=None, log_in=None, email=None, phone_number=None, bio=None):
        """
        :param text: Contains post content
        :param date: Date the post was published
        :param production_time: Time the post is published
        :param number_comments: The number of comments that has each post
        """
        self.text = text
        self.date = date
        self.production_time = production_time
        self.comments = comments
        self.like = like

    '''In this function, creat your posts and add your pages '''
    @classmethod
    def creat_post(cls, name, txt):
        file_path = "post_file.csv"
        try:
            df_post = pd.read_csv(file_path)
            df_post_indexed = df_post.set_index("id_post", drop=True)
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
        except Exception:
            print("you have not this file please create a file with name post_file.csv "
                  "and set first row with this items "
                  "(user_name,id_post,txt,date,production_time,comments,like,user_log,date_comment,time_comment)")
        return post

    '''In this function, edited your post that you want '''
    def change_post(self, new_txt, id):
        try:
            post_changed = pd.read_csv('post_file.csv')
            location = 0
            with open("post_file.csv", 'r') as post_file:
                reader = csv.DictReader(post_file)
                for row in reader:
                    if row['user_name'] == self.user_name and row['id_post'] == id:
                        txt = new_txt
                        print("Your txt is changed.")
                        post_changed.loc[location, 'txt'] = txt
                        post_changed.to_csv('post_file.csv', index=False)
                    location += 1
        except Exception:
            print("you can not open this file and changed these value please check a file with name post_file.csv "
                  "is exists and what happened!! ")

    '''In this function, deleted your post that you want '''
    def delete_post(self, id):
        try:
            module_show_file.show_post_file(self.user_name)
            lines = list()
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
        except Exception:
            print("you can not open this file and deleted these value please check a file with name post_file.csv "
                  "is exists and what happened!! ")

    '''In this function, add comment for posts that you want '''
    def add_comment(self, user_name, person, id, new_comments):
        self.comments = new_comments
        d = datetime.datetime.today()
        date_comment = d.strftime('%d-%m-%Y')
        time_comment = d.strftime("%H:%M:%S")
        try:
            add_com = pd.read_csv('post_file.csv')
            location = 0
            with open("post_file.csv", 'r+') as post_file:
                reader = csv.DictReader(post_file)
                for row in reader:
                    if row['user_name'] == person and row['id_post'] == id:
                        log.info_logger.info(f'post with ID:{id} add comment by user name:{user_name}')
                        comments = self.comments
                        print("Your comment is added.")
                        add_com.loc[location, 'user_log'] = user_name
                        add_com.loc[location, 'date_comment'] = date_comment
                        add_com.loc[location, 'time_comment'] = time_comment
                        add_com.loc[location, 'comments'] = comments
                        add_com.to_csv('post_file.csv', index=False)
                    location += 1

        except Exception:
            print("you can not open this file and add comment please check a file with name post_file.csv "
                  "is exists and what happened!! ")

    '''In this function, show my post '''
    def show_my_post(self):
        try:
            with open("post_file.csv", 'r') as post_file:
                reader = csv.DictReader(post_file)
                print(f'<<<<<<<< {self.user_name} ----> logged and see my posts.')
                for row in reader:
                    if row['user_name'] == self.user_name:
                        print(f"user_name:{row['user_name']}, Id of post: {row['id_post']} , text: {row['txt']}"
                              f" ,date: {row['date']} , production_time: {row['production_time']},"
                              f" comments: {row['comments']} , like: {row['like']} ")
        except Exception:
            print("you can not open this file and show these value please check a file with name post_file.csv "
                  "is exists and what happened!! ")

    '''In this function, view each other's posts '''
    def show_post(self, person):
        try:
            with open("post_file.csv", 'r') as post_file:
                reader = csv.DictReader(post_file)
                print(f'>>>>>>>>{self.user_name} ----> logged and see your posts ----> {person}')
                for row in reader:
                    if row['user_name'] == person:
                        print(f"user_name:{row['user_name']}, Id of post: {row['id_post']} , text: {row['txt']}"
                              f" ,date: {row['date']} , production_time: {row['production_time']},"
                              f" comments: {row['comments']} , like: {row['like']} ")
        except Exception:
            print("you can not open this file and show these value please check a file with name post_file.csv "
                  "is exists and what happened!! ")

    '''In this function, liked your post that you want '''
    def like(self, user_name, person, id):
        count_like = 0
        try:
            add_like = pd.read_csv('post_file.csv')
            location = 0
            with open("post_file.csv", 'r') as post_file:
                reader = csv.DictReader(post_file)
                for row in reader:
                    if row['user_name'] == person and row['id_post'] == id:
                        count_like += 1
                        likes = count_like
                        print("You liked post.")
                        add_like.loc[location, 'user_log'] = user_name
                        add_like.loc[location, 'like'] = likes
                        add_like.to_csv('post_file.csv', index=False)
                    location += 1
        except Exception:
            print("you can not open this file and add like please check a file with name post_file.csv "
                  "is exists and what happened!! ")

    '''In this function, manage to you want add comment or like'''
    def access_post(self, user_name, person, select, id, new_comments=None):
        if select == '1':
            print(">>>> add comment")
            self.add_comment(user_name, person, id, new_comments)
        elif select == '2':
            print(">>>> add like")
            Post.like(self, user_name, person, id)
        else:
            print('you dont add comment or liked the post!')

    '''In this function, creat obj of post class'''
    @staticmethod
    def obj_post(person, id):
        with open("post_file.csv", 'r') as post_file:
            reader = csv.DictReader(post_file)
            for row in reader:
                if row['user_name'] == person and row['id_post'] == id:
                    pst = Post(row['txt'], row['date'], row['production_time'], row['comments'], row['like'])
        return pst








