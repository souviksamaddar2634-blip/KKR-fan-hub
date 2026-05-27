from fastapi import APIRouter
from typing import List

from backend.schemas.cheers import CheerCreate, CheerResponse
from backend.services import cheers_service
from backend.utils.websocket_manager import manager
from backend.services.websocket_service import format_ws_event

router = APIRouter()

@router.get("/cheers", response_model=List[CheerResponse])
def get_cheers():
    """Endpoint to retrieve list of latest cheers."""
    return cheers_service.get_cheers()

@router.post("/cheers", response_model=List[CheerResponse])
async def add_cheer(payload: CheerCreate):
    """Endpoint to submit a new cheer."""
    updated_cheers = cheers_service.add_cheer(payload.name, payload.msg)
    event_payload = format_ws_event("cheer_update", updated_cheers)
    await manager.broadcast(event_payload, "cheers")
    return updated_cheers
