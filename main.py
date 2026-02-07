from fastapi import FastAPI
from datetime import datetime
import uvicorn
import pytz

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Welcome to Time Server API'}

@app.get('/time')
def get_time():
    now = datetime.now(pytz.utc)
    return {'current_time': now.strftime('%Y-%m-%d %H:%M:%S %Z')}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
