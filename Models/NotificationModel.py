from pydantic import BaseModel

class Notificatoin(BaseModel):
    fcm: str
    title: str
    body: str
    class Config:
        json_schema_extra = {
            'example': {
                'fcm': 'cBpWspdpRY2ywHr8whZMuA:APA91bG1_874mgSkvcxVm8x0KSpzAIXNSc7GSJo3An_pVRBBRdNirKjn3_HD5rWmnqZL1x8PszK2lqj92cQKsbOrVAquFDlujT0EER-9IMAmh0LJ6M60182AwRXTxmTvtv8Wm78wxodw',
                'title' : 'Notification from the EndPoint',
                'body': 'Some Random Body'
            }
        }
        
    
    