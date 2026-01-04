from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Upscaler API Ready!", "endpoint": "/upscale"}

@app.post("/upscale")
async def upscale_image(file: UploadFile = File(...)):
    # Read file
    contents = await file.read()
    
    # Open image
    image = Image.open(io.BytesIO(contents)).convert('RGB')
    
    # 4x upscale
    width
