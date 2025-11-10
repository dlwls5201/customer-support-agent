from pydantic import BaseModel
from typing import Optional


class UserAccountContext(BaseModel):
    customer_id: int
    name: str
    email: Optional[str] = None
    tier: str = "basic"  # premium entreprise


class InputGuardRailOutput(BaseModel):
    is_off_topic: bool
    reason: str
