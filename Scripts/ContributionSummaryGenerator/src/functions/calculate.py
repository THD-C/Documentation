from src.Models.ContributorActivity import ActivitySummary,UserActivitySummary



def get_contribution_per_username(data: list[ActivitySummary]) -> list[UserActivitySummary]:
    temp: dict[str, UserActivitySummary] = {}
    
    for item in data:
        if item.author.login in temp:
            temp[item.author.login].additions += item.additions
            temp[item.author.login].deletions += item.deletions
            temp[item.author.login].commits += item.commits
            temp[item.author.login].repository_count += 1
        else:
            temp[item.author.login] = UserActivitySummary(additions=item.additions, deletions=item.deletions, commits=item.commits, login=item.author.login)
            
    return list(temp.values())