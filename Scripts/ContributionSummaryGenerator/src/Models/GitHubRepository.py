from pydantic import BaseModel

class GitHubRepository(BaseModel):
    name: str
    full_name: str
    html_url: str
    visibility: str
    pushed_at: str
    created_at: str
    updated_at: str
    