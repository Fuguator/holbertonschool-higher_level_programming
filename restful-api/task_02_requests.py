#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        for post in posts:
            print(post['title'])
    else:
        print('Error', response.status_code)

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        with open('posts.csv', 'w', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
    else:
        print('Error', response.status_code)
