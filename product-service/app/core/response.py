from typing import List

from pydantic import BaseModel


class Response(BaseModel):
    status_code: int = None
    messages: str = None
    result: BaseModel = None
    results: List = None
