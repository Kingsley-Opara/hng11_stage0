from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

@app.get('/', status_code=200)
def home():
    current_datetime = datetime.now(timezone.utc)
    formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
    data = {
        "email": "oparaudochukwu277@gmail.com",
        "current_datetime": formatted_datetime,
        "github_url": "https://github.com/Kingsley-Opara/hng11_stage0"
    }
    return data