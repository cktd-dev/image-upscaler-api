from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageEnhance
import io

app = FastAPI(title="FREE Image Upscaler API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Image Upscaler API Live!", "url": "/docs", "upload": "/upscale"}

@app.post("/upscale")
async def upscale_image(file: UploadFile = File(...)):
    # Read uploaded image
    contents
