from fastapi import APIRouter
from typing import List

from backend.utils.helpers import read_json
from backend.schemas.seasons import SeasonPerformance

router = APIRouter()

@router.get("/seasons", response_model=List[SeasonPerformance])
def get_seasons():
    return read_json("seasons.json")
