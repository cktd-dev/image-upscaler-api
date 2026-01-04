from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageEnhance
import io

app = FastAPI(title="Image Upscaler API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Image Upscaler API Live!", "docs": "/docs"}

@app.post("/upscale")
async def upscale_image(file: UploadFile = File(...)):
    # 1. Read file completely
    contents = await file.read()
    
    # 2. Open image
    image = Image.open(io.BytesIO(contents)).convert('
