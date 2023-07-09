from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

sentiment_labels = {
    'LABEL_0': "حزين وواعي",
    'LABEL_1': "مبسوووط"
}

tokenizer = AutoTokenizer.from_pretrained("D:/University/5th_year/Graduation/AraBERT")
model = AutoModelForSequenceClassification.from_pretrained("D:/University/5th_year/Graduation/AraBERT")
sentiment = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)