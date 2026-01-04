from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
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
    return {"message": "Image Upscaler API Live!", "endpoint": "/enhance"}

@app.post("/enhance")
async def enhance_image(file: UploadFile = File(...), scale: int = Form(4)):
    # Read image
    contents = await file.read()
    image = Image
