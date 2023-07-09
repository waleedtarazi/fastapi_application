from typing import Union, Dict
#   
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

sentiment_labels = {
    'LABEL_0': "حزين وواعي",
    'LABEL_1': "مبسوووط",
    'LABEL_2' : "حيادي"
}

tokenizer = AutoTokenizer.from_pretrained("D:/University/5th_year/Graduation/AraBERT")
model = AutoModelForSequenceClassification.from_pretrained("D:/University/5th_year/Graduation/AraBERT")
sentiment = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

def make_prediction(text: str) -> Dict[str, Union[str, int]]:
    result = sentiment(text)[0]
    label_id = result['label']
    label = sentiment_labels[label_id]
    score = result['score']
    return {"text": text ,"label": label, "score": score}