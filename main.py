from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile
from loguru import logger
import easyocr
from io import BytesIO
from PIL import Image
import numpy as np
import imagehash
from time import perf_counter
# Save all files and result to cached
# by a dictionary with key is image hash
cache = {}

# Initialize the model to None
# Load the ML model
reader = easyocr.Reader(
    ['vi', 'en'],
    gpu=True,
    detect_network="craft",
    model_storage_directory="./model_storage/model",
    download_enabled=False
)

app = FastAPI()

def measure_execution_time(fn):
    def inner(*args, **kwargs):
        start_time = perf_counter()
        result = fn(*args, **kwargs)       
        end_time = perf_counter()
        execution_time = end_time - start_time
        logger.info('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return result  
    return inner
@measure_execution_time
def readtext(pil_image):
    return reader.readtext(pil_image)

@app.get("/")
async def root():
    return {"message": "Hello World v5"}

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    # Read image from route
    request_object_content = await file.read()
    pil_image = Image.open(BytesIO(request_object_content))
    pil_hash = imagehash.average_hash(pil_image)
    logger.info("HELLO FROM OCR APP v5")
    if pil_hash in cache:
        logger.info("Getting result from cache!")
        return cache[pil_hash]
    else:
        logger.info("Predicting. Please wait...")
        # Get the detection from EasyOCR
        detection = readtext(pil_image)

        # Create the final result
        result = {"bboxes": [], "texts": [], "probs": []}
        for (bbox, text, prob) in detection:
            # Convert a list of NumPy int elements to premitive numbers
            bbox = np.array(bbox).tolist()
            result["bboxes"].append(bbox)
            result["texts"].append(text)
            result["probs"].append(prob)

        # Save the result to cache
        cache[pil_hash] = result
        
        return result