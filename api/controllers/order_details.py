from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import models, schemas

def create(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if not db_order_detail.first():
        raise HTTPException(status_code=404, detail="Order detail not found")
    db_order_detail.update(order_detail.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return db_order_detail.first()

def delete(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if not db_order_detail:
        raise HTTPException(status_code=404, detail="Order detail not found")
    db.delete(db_order_detail)
    db.commit()
    return {"message": "Order detail deleted successfully"}
