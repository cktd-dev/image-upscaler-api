from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageEnhance
import io

app = FastAPI(title="Image Upscaler API")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Upscaler API Live!", "docs": "/docs", "upload": "/upscale"}

@app.post("/upscale")
async def upscale_image(file: UploadFile = File(...)):
    # Read uploaded file
    contents
