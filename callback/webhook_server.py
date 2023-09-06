from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger
import uvicorn


app = FastAPI()


class OCREvent(BaseModel):
    done: bool


class OCREventReceived(BaseModel):
    ok: bool


@app.post("/ocr/{invoice_id}", response_model=OCREventReceived)
async def ocr_notitifcation(invoice_id: str, notification: OCREvent):
    """
    Process the invoice and notify the callback
    """
    if notification.done:
        logger.info(f"Received completed notification for image_id: {invoice_id}!")
    else:
        logger.info(f"Received incomplete notification for image_id: {invoice_id}!")
        
    return {"ok": True}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)