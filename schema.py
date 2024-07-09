from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime

# post model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    create_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: Optional[bool] = False
