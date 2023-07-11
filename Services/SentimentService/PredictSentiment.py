from typing import Union, Dict
from decouple import config
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_path = config('MODEL_PATH')
tokenizer_path = config('TOKENIZER_PATH')

sentiment_labels = {
    'negative': "حزين ",
    'positive': "مبسوووط",
    'neutral' : "حيادي"
}

tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
sentiment_model = pipeline('text-classification', model=model, tokenizer=tokenizer)

async def make_prediction(text: str) -> Dict[str, Union[str, int]]:
    result = sentiment_model(text)[0]
    label_id = result['label']
    label = sentiment_labels[label_id]
    score = result['score']
    return {"text": text ,"label": label, "score": score}