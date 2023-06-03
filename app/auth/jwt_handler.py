import time
import jwt
from decouple import config

JWT_SECRET = config('SECRET_KEY')
JWT_ALGORITHM = config('ALGORITHM')

# return generated tokens(JWT)
def token_response(token: str):
    return{
        'access_token': token
    }
    
def signJWT(userID: str):
    payload = {'userId' : userID, 
        'exp': time.time() + 3600}
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)


def decode_JWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM,verify_exp=False)
        return decoded_token
    except:
        return {'problem with the token'}
    
def get_JWT_ID(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM,verify_exp=False)
        return decoded_token['userId']
    except:
        return {'problem with the token'}