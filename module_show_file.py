import csv

'''This function, show following list'''
def following_list():
    with open('following_list.csv', 'r') as following_data:
        reader = csv.DictReader(following_data)
        for row in reader:
            print(row['user_name'])


'''This function, show contains of post_file.csv'''
def show_post_file(name):
    with open("post_file.csv", 'r') as post_file:
        reader = csv.DictReader(post_file)
        for row in reader:
            if row['user_name'] == name:
                print(f"user_name:{row['user_name']}, Id of post: {row['id_post']} , text: {row['txt']} .")


'''This function, show contains of User_Information.csv'''
def show_userInfo():
    with open("User_Information.csv", 'r') as user_file:
        reader = csv.DictReader(user_file)
        for row in reader:
            print(f"user name:{row['user_name']}")


'''This function, show contains of profile_file.csv'''
def show_profInfo(user_log):
    with open("profile_file.csv", 'r') as profile_file:
        reader = csv.DictReader(profile_file)
        for row in reader:
            if row['user_name'] == user_log:
                print(f"user_name: {row['user_name']}"
                      f" email: {row['email']} , phone_number: {row['phone_number']}"
                      f" 'bio': {row['bio']}.")
