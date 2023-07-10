from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from .jwt_handler import decode_JWT

class JWTBearer(HTTPBearer):
    """
    JWT Bearer class for handling JWT authentication.

    This class extends the HTTPBearer class from the fastapi.security module and provides
    additional functionality for verifying JWT tokens.
    """
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str:
        credentials = await super().__call__(request)
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        if credentials.scheme != "Bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
        if not self.verify_jwt(credentials.credentials):
            raise HTTPException(status_code=403, detail="Invalid token or expired token.")
        return credentials.credentials

    def verify_jwt(self, jwt_token: str) -> bool:
        """
        Verify the JWT token.

        This function takes a JWT token as input and returns True if the token is valid,
        or False otherwise.
        """
        try:
            payload = decode_JWT(jwt_token)
            return True
        except:
            return False