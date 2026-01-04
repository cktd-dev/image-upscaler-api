from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

app = FastAPI(title="FREE Image Upscaler API")

# CORS so frontend can call
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Image Upscaler API Live!",
        "docs": "/docs",
        "upload": "/upscale",
    }

@app.post("/upscale")
async def upscale_image(
    file: UploadFile = File(...),
    scale: int = Form(4),
):
    # 1. Read uploaded file
    contents = await file.read()

    # 2. Open image
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # 3. Clamp scale
    if scale < 1:
        scale = 1
    if scale > 4:
        scale = 4

    # 4. Calculate new size
    width, height = image.size
    new_size = (width * scale, height * scale)

    # 5. Resize (high quality)
    upscaled = image.resize(new_size, Image.Resampling.LANCZOS)

    # 6. Save to bytes buffer
    buf = io.BytesIO()
    upscaled.save(buf, format="JPEG", quality=95)
    buf.seek(0)

    # 7. Return image stream
    return StreamingResponse(
        buf,
        media_type="image/jpeg",
        headers={
            "Content-Disposition": 'inline; filename="upscaled.jpg"'
        },
    )
