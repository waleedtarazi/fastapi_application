from sqlalchemy.orm import Session
from Schemas.RequestSchema import Request as SchemaRequest
# from Models.RequestModel import UserAddRequst


def get_request_db(db: Session, request_id: int) -> SchemaRequest:
    return db.query(SchemaRequest).\
        filter(SchemaRequest.id == request_id).first()
        
def create_request_db(request: SchemaRequest, db: Session):
    """ Add request to the DB """
    db.add(request)
    db.commit()
    db.refresh(request)
    return request  

def update_request_db(request: SchemaRequest, db: Session):
    """ update the current request into DB """
    db.commit()
    db.refresh(request)
    return request
