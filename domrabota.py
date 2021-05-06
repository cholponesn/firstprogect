# a, b, c = int(input()), int(input()), int(input())
# if (a + b) % 2 != 0:
#     print('YES')
# elif (b + c) % 2 != 0:
#     print('YES')                      # задача 2 которую сначала я не поняла
#
# elif (a + c) % 2 != 0:
#     print('YES')
# else:
#     print('NO')


# a = 5
# if a % 2 == 0:
#     print('Четное число')       #чтобы узнать четность числа , присваеваем переменной а число четность которого хотим
# else:                                   #проверить. пишем условие: если остаток деления переменной ф на 2 равно 0
#     print('Нечентное число'                 #вывести на экран "четное число" если нет то "нечетное число'


# b = 6
# if b % 2 == 0:
#     print('четное число')               #те же условия, вывели четно число
# else:
#     print('нечетное число')


# a = [1,1,2,3,5,8,13,21,34,55,89]
# for elem in a:
#     if elem < 5:
#         print(elem)

a = [1,1,2,3,5,8,13,21,34,55,89]
b =[1,2,3,4,5,6,7,8,9,10,11,12,13]
result = [elem for elem in a if elem in b]


"""
1. Вывести все коммиты (сообщения) и подсчитать все.
    1.1 Вывести сообщения длина которых больше 10 и их кол-во
    1.2 Вывести пользователей кто сделал коммит
    1.3 Вывести по каждому пользователю его кол-во коммитов
    ДЗ Запуск программы через терминала с указом имени пользователя и репозитория
"""

import sys
import datetime
import time
token = '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'
import requests


start_time = time.time()



def fetch_url(url:str):
    r = requests.get(url)
    return r


def get_commits(url:str):
    responses = fetch_url(url).json()
    for response in responses:
        commit_msg = response['commit']['message']
        if len(commit_msg) > 10:
            print(commit_msg)


def get_users(url:str):
    responses = fetch_url(url).json()
    author_list = []
    for response in responses:
        author = response['commit']['author']['name']
        if author not in author_list:
            author_list.append(author)
    return author_list,responses


def get_commits_by_user(url:str):
    authors,responses = get_users(url)
    for author in authors:
        commits_count = 0
        for response in responses:
            commit = response['commit']
            if commit['author']['name'] == author:
                commits_count += 1
        print(commits_count)


def main():
    github_username = sys.argv[1]
    github_repository = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits?page1&per_page=100'.format(github_username,github_repository)
    get_commits_by_user(url)


# main()
# print(time.time() - start_time)

