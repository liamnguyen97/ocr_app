from typing import Union

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from loguru import logger
import uvicorn
import requests

app = FastAPI()


class OCREvent(BaseModel):
    done: bool


class OCREventReceived(BaseModel):
    ok: bool


ocr_callback_router = APIRouter()


@ocr_callback_router.post(
    "{$callback_url}/ocr/{$invoice_id}", response_model=OCREventReceived
)
def ocr_notification(notification: OCREvent):
    pass


@app.post("/ocr", callbacks=ocr_callback_router.routes)
def ocr(invoice_id: str, callback_url: Union[str, None] = None):
    """
    Process the invoice and notify the callback
    """
    logger.info(f"Pseudo OCR processing {invoice_id}!")

    # Send a nice notification to the callback
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'done': True
    }
    callback_response = requests.post(f'{callback_url}/ocr/{invoice_id}', headers=headers, json=json_data)
    logger.info(f"Call back response: {callback_response.json()}!")

    return {"msg": "Completed processing!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)