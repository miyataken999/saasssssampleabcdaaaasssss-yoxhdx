from fastapi import APIRouter
from api.schemas.team import TeamSchema
from api.models.team import Team
from sqlalchemy.orm import sessionmaker

router = APIRouter()

@router.post("/teams/")
async def create_team(team: TeamSchema):
    session = sessionmaker(bind=engine)()
    new_team = Team(name=team.name)
    session.add(new_team)
    session.commit()
    return {"message": "Team created successfully"}

@router.get("/teams/")
async def read_teams():
    session = sessionmaker(bind=engine)()
    teams = session.query(Team).all()
    return [{"name": team.name} for team in teams]