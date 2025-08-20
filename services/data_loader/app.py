from DAL import DAL
from fastapi import FastAPI
import uvicorn

app = FastAPI()
dal = DAL()
dal.open_connection()
dal.create_index()

@app.get('/get')
def get_data():
    data = dal.get_data()
    return data

@app.post('/post')
def post_data(ID=None, first_name=None, last_name=None, phone_number=None, rank=None):
    if None in [ID, first_name, last_name, phone_number, rank]:
        return 'please enter whole data'
    return dal.post_data(ID, first_name, last_name, phone_number, rank)

@app.put('/put')
def put_data_by_id(ID=None):
    if ID == None:
        return 'Please Insert ID'
    return dal.put_data_by_id(ID)

@app.get('/close')
def close():
    return dal.close_connection()

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)