from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Upscaler API Live!"}

@app.post("/upscale")
async def upscale_image(file: UploadFile = File(...)):
    contents
