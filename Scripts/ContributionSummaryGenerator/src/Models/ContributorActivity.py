from pydantic import BaseModel, Field

    
class Author(BaseModel):
    login: str
    html_url: str
    
class Contributions(BaseModel):
    week: int = Field(alias='w')
    additions: int = Field(alias='a')
    deletions: int = Field(alias='d')
    commits: int = Field(alias='c')

class ActivitySummary(BaseModel):
    repository: str
    author: Author
    additions: int
    deletions: int
    commits: int

class UserActivitySummary(BaseModel):
    repository_count: int = Field(default=1)
    login: str
    additions: int
    deletions: int
    commits: int

class Activity(BaseModel):
    author: Author
    total: int
    weeks: list[Contributions]
    
    def get_summary(self, repo_name: str) -> ActivitySummary:
        summary = ActivitySummary(
            repository=repo_name,
            author=self.author,
            additions=0,
            deletions=0,
            commits=0,
        )
        
        for week in self.weeks:
            summary.additions += week.additions
            summary.deletions += week.deletions
            summary.commits += week.commits
            
        return summary
    

class Repository(BaseModel):
    name: str
    activity: list[Activity]
    
    