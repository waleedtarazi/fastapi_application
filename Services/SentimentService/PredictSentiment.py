from typing import Union, Dict
from decouple import config
from transformers import pipeline

# model_path = config('MODEL_PATH')
# tokenizer_path = config('TOKENIZER_PATH')

sentiment_labels = {
    'negative': "حزين ",
    'positive': "مبسوووط",
    'neutral' : "حيادي"
}

sentiment_model = pipeline('text-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment')

async def make_prediction(text: str) -> Dict[str, Union[str, int]]:
    result = sentiment_model(text)[0]
    label = result['label']
    score = result['score']
    return {"text": text ,"label": label, "score": score}