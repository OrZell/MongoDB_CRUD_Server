from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/get')
def get_data():
    return 'data'

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)