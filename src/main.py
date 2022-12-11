import uvicorn
import asyncio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from baseStation import scan, send

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return RedirectResponse("/static/index.html")


@app.get("/api/basestation/on")
async def basestation_on():
    lhb_devices = await scan()
    await asyncio.gather(*[send(device, b'\x01') for device in lhb_devices])
    return "on"


@app.get("/api/basestation/off")
async def basestation_off():
    lhb_devices = await scan()
    await asyncio.gather(*[send(device, b'\x00') for device in lhb_devices])
    return "off"


if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.112", port=8000)
