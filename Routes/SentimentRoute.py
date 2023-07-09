from fastapi import APIRouter, HTTPException
from Models.SentimentModel import SentimentInput
from Services.SentimentService.PredictSentiment import make_prediction 

# Router
SentimentRouter = APIRouter(prefix="/sentiment", tags=["Sentiment"])

# Index
@SentimentRouter.get("/")
def index():
    raise HTTPException(status_code=404, detail= "no root for this directory for now, please visit us again")

@SentimentRouter.post('/predict_sentiment', status_code= 200)
async def predict(input_text: SentimentInput):
    return  make_prediction(input_text.text)
