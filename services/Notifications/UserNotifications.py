from firebase_admin import  messaging

def send_notification(token, title, body):
    
    message = messaging.Message(
        notification= messaging.Notification(title= title, body= body), 
        token= token
        )
    response = messaging.send(message)
    print(f"Successfully sent message: {response}")