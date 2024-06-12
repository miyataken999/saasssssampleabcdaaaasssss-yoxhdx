from fastapi import APIRouter, HTTPException
from api.schemas.user import UserSchema
from api.models.user import User
from sqlalchemy.orm import sessionmaker

router = APIRouter()

@router.post("/users/")
async def create_user(user: UserSchema):
    session = sessionmaker(bind=engine)()
    existing_user = session.query(User).filter_by(username=user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=user.username, password=user.password, profile=user.profile, team_id=user.team_id)
    session.add(new_user)
    session.commit()
    return {"message": "User created successfully"}

@router.get("/users/")
async def read_users():
    session = sessionmaker(bind=engine)()
    users = session.query(User).all()
    return [{"username": user.username, "profile": user.profile} for user in users]