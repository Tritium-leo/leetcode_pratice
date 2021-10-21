from typing import *
from pydantic import BaseModel


class BaseTest(BaseModel):
    param: List
    result: Any
