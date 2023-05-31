from pydantic import BaseModel

class SentimentInput(BaseModel):
    text: str
    
# adding the seconed commit that i don't want to UNDO it