from pydantic import BaseModel, Field
from typing import Annotated
from fastapi import Body, FastAPI

class AnonymizeRequest(BaseModel):
    user_question: str = Field(..., example="What is my IP address?", description="The user's question containing potential PII.")
    user_id: str = Field(None, description="An optional user identifier that might be used for logging or tracking anonymization requests.")


# from typing import Annotated

# from fastapi import Body, FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()


# class AnonymizeRequest(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300
#     )
