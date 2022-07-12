import requests
import threading
import time
import json

API_URL = 'http://localhost:8888'

def call_get(i):
    SUB_PATH = '/get'
    params = {'param': i}
    response = requests.get(API_URL + SUB_PATH, params=params)
    print(SUB_PATH, i)

def call_async_get(i):
    SUB_PATH = '/async_get'
    params = {'param': i}
    response = requests.get(API_URL + SUB_PATH, params=params)
    print(SUB_PATH, i)

def call_post(i):
    SUB_PATH = '/post'
    body = {'data': i}
    response = requests.post(API_URL + SUB_PATH, data=json.dumps(body))
    print(SUB_PATH, i)

def call_async_post(i):
    SUB_PATH = '/async_post'
    body = {'data': i}
    response = requests.post(API_URL + SUB_PATH, data=json.dumps(body))
    print(SUB_PATH, i)

def call_async_post_request(i):
    SUB_PATH = '/async_post_request'
    body = {'data': i}
    response = requests.post(API_URL + SUB_PATH, data=json.dumps(body))
    print(SUB_PATH, i)

def call_thread(func, *args):
    t = threading.Thread(target=func, args=(*args,))
    t.start()


if __name__ == '__main__':

    # to check how async & non-async endpoint work for many client's request in short time
    print('Function list')
    print('0. call_get')
    print('1. call_async_get')
    print('2. call_post')
    print('3. call_async_post')
    print('4. call_async_post_request')
    idx = int(input('Select function : '))
    selected_func = [call_get, call_async_get, call_post, call_async_post, call_async_post_request][idx]
    for i in range(5):
        call_thread(selected_func, i)
        time.sleep(0.1) #to make sure previous thread function call finished.

    # time.sleep(1)
    # # to check whether async endpoint affect to other endpoint
    # #call async_get
    # for i in range(5):
    #     call_thread(call_async_get, i)
    #     time.sleep(0.1)

    # #call async_post
    # for i in range(5):
    #     call_thread(call_async_post, i)
    #     time.sleep(0.1)
        

    # #call get
    # for i in range(5):
    #     call_thread(call_get, i)
    #     time.sleep(0.1)

    #call async_get
    for i in range(5):
        call_thread(call_async_get, i)
        time.sleep(0.1)

    #call post
    for i in range(5):
        call_thread(call_post, i)
        time.sleep(0.1)

    # #call async_post
    # for i in range(5):
    #     call_thread(call_async_post, i)
    #     time.sleep(0.1)

    # #call async_post_request
    # for i in range(5):
    #     call_thread(call_async_post_request, i)
    #     time.sleep(0.1)