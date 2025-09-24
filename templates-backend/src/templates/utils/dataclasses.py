from dataclasses import dataclass

from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext

from templates.settings import Settings


@dataclass
class AppContext(BaseContext):
    settings: Settings
    session: Session
