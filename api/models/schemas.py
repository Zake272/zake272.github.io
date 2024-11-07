from pydantic import BaseModel
from typing import Optional

# Sandwich schemas
class SandwichBase(BaseModel):
    sandwich_name: str
    price: float

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None

class Sandwich(SandwichBase):
    id: int

    class Config:
        orm_mode = True

# Resource schemas
class ResourceBase(BaseModel):
    item: str
    amount: int

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None

class Resource(ResourceBase):
    id: int

    class Config:
        orm_mode = True

# Recipe schemas
class RecipeBase(BaseModel):
    sandwich_id: int
    resource_id: int
    amount: int

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True

# Order schemas
class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True

# OrderDetail schemas
class OrderDetailBase(BaseModel):
    order_id: int
    sandwich_id: int
    amount: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    amount: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int

    class Config:
        orm_mode = True
