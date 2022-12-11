import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from baseStation import scan

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return RedirectResponse("/static/index.html")


@app.get("/api/basestation/on")
async def basestation_on():
    await scan(b'\x01')
    return "on"


@app.get("/api/basestation/off")
async def basestation_off():
    await scan(b'\x00')
    return "off"


async def send(status):
    print('SEND :    ', status)

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.112", port=8000)
