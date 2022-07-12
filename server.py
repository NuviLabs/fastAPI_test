import random
import time
import json

import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class BaseBody(BaseModel):
    data: int


@app.get('/get')
def get(param: int):
    print('request #%s start'%param)
    t = random.random()
    time.sleep(t)
    print('request #%s end'%param)


@app.get('/async_get')
async def async_get(param: int):
    print('request #%s start'%param)
    t = random.random()
    time.sleep(t)
    print('request #%s end'%param)


@app.post('/post')
def post(body: BaseBody):
    data = body.data
    print('request #%s start'%data)
    t = random.random()
    time.sleep(t)
    print('request #%s end'%data)


@app.post('/async_post')
async def async_post(body: BaseBody):
    data = body.data
    print('request #%s start'%data)
    t = random.random()
    time.sleep(t)
    print('request #%s end'%data)


@app.post('/async_post_request')
async def async_post_request(body: Request):
    body = await body.body()
    body = json.loads(body)
    data = body.get('data')
    print('request #%s start'%data)
    t = random.random()
    time.sleep(t)
    print('request #%s end'%data)


if __name__ == '__main__':
    uvicorn.run('server:app', host='0.0.0.0', port=8888, reload=True)
