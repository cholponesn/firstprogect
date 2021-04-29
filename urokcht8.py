

# dict1 = {'a':1,'b':2}
# dict2 = {'a':33,'z':3}
#                                        #способ обьеденить 2 словаря
# dict1.update(dict2)
# print(dict1)


users = [{'id':1,'user': 'digital', },
         {'id':2,'user': 'maksim', },
         {'id':3,'user': 'vova', },
         {'id':4,'user': 'begimai', },
         {'id':5,'user': 'aliya', },
         {'id':6,'user': 'bakyt',},
         {'id':7,'user': 'chingiz', },
         {'id':8,'user': 'jamilya',},
         {'id':9,'user': 'cholpon', },
         {'id':10,'user': 'erbol', }
         ]
posts = [{'id':1,'text':'hiring','status':'sponsored','keyword':'nic1'},
         {'id':2,'text':'text1','status':'pub'},
         {'id':3,'text':'text2','status':'pub'},
         {'id':4,'text':'text3','status':'pub'},
         {'id':5,'text':'text4','status':'pub'},
         {'id':6,'text':'text5','status':'pub'},
         {'id':7,'text':'Canada immigration','status':'sponsored','keyword':'interested!'}]
comments = [{'id':1,'user_id':1,'post_id':1,'comment':'This is not nic1'},
            {'id':2,'user_id':2,'post_id':1,'comment':'Hello this is nic1'},
            {'id':3,'user_id':3,'post_id':2,'comment':'looking good!'},
            {'id':4,'user_id':4,'post_id':2,'comment':'awesome!'},
            {'id':5,'user_id':5,'post_id':2,'comment':'LGTM'},
            {'id':6,'user_id':6,'post_id':3,'comment':'here we go!'},
            {'id':7,'user_id':6,'post_id':4,'comment':'not ok'},
            {'id':8,'user_id':6,'post_id':7,'comment':'interested!'},
            {'id':9,'user_id':6,'post_id':7,'comment':'woohoo!'},
            {'id':10,'user_id':6,'post_id':7,'comment':'interested!'}]
"""
1. Нужно найти все posts со статусом sponsored!
2. Найти комментарии к posts sponsored
3. Среди найденных комментариев найти те что содержат keyword из posts
"""

def search_posts_status_sponsored(posts):
    list = []
    for post in posts:

        if post['status'] == 'sponsored':
            list.append(post)                        #первая задача
    return list
posts = search_posts_status_sponsored(posts)

def comment_to_post(posts):

    for post in posts:
        post['comments'] = []
        for comment in comments:                   #задача 2
            if post['id'] == comment['post_id']:
                post['comments'].append(comment['comment'])
    return posts
posts = comment_to_post(posts)
print(posts)

def clean_data(posts):
    for post in posts:
        key = post['keyword']
        for comment in post['comments']:
            if key not in comment:                    #задача 3
                post['comments'].remove(comment)
    return posts
posts = clean_data(posts)
print(posts)




























