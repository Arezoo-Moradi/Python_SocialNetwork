import csv
import pandas as pd
from User import User
from Profile import Profile
import datetime
import csv
import pandas as pd
from pathlib import Path
'''writer = csv.DictWriter(fp_to_write)
reader = csv.DictReader(fp_to_read)
index = 0
for row in reader:
    row['id'] = index
    writer.write(row)
    index += 1'''
'''df = pandas.read_csv('User_Information.csv')
df.index = [x for x in range(1, len(df.values)+1)]
print('df:', df)'''

'''import pandas as pd

df = pd.read_csv('User_Information.csv')
print(df)
df.index = [x for x in range(1, len(df.values)+1)]
df.index.name = 'id'
print(df)
print(df.index.values)'''

'''def update_csv(file_path, value_to_update, update_value):
    df = pd.read_csv(file_path)
    df_updated = df.replace(to_replace=value_to_update, value=update_value)
    print(df_updated)

update_csv('User_Information.csv' ,'vahid', 'nazi')'''
def creat_post():
    name = 'arezoo'
    # id_post = input('Enter id of the post:')
    txt = input('Enter text of the post:')
    #Post.post_id.append(id_post)
    d = datetime.datetime.today()
    date = d.strftime('%d-%m-%Y')
    production_time = d.strftime("%H:%M:%S")
    comments = None
    like = None

    with open('post_file.csv', 'a', newline='') as file_post:
        fields_name = ['user name','txt', 'date', 'production_time', 'comments', 'like']
        csv_writer = csv.DictWriter(file_post, fieldnames=fields_name)
        if Path('post_file.csv').stat().st_size == 0:
            csv_writer.writeheader()
        # 'id_post': id_post,
        csv_writer.writerow({'user name': name, 'txt': txt, 'date': date,
                             'production_time': production_time, 'comments': comments, 'like': like})
        df = pd.read_csv('post_file.csv')
        df.index.name = 'id_post'
        df.to_csv('post_file.csv', index=True)

creat_post()
