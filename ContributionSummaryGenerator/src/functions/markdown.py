from src.Models.ContributorActivity import UserActivitySummary, ActivitySummary

MD_PATH = "./Docs/Contributions"

def generate_overall_md_file(data: list[UserActivitySummary]):
    data = sorted(data, key=lambda x: x.commits, reverse=True)
    data_to_write = []
    data_to_write.append("# Overall Contributions to THD(c) app per User\n")
    data_to_write.append("```diff\n")
    for item in data:
        data_to_write.append(f"@@ {item.login} @@ \n! {item.commits:_} commits\n# {item.repository_count} repositories\n++ {item.additions:_}\n-- {item.deletions:_}\n\n")
    
    data_to_write.append("```\n")
    
    with open(f"{MD_PATH}/Contributions_Overall.md", "w") as f:
        f.writelines(data_to_write)
        
def get_user_contributions(data: ActivitySummary) -> str:
    return f"@@ {data.author.login} @@\n++ {data.additions:_}\n-- {data.deletions:_}\n! {data.commits:_} commits\n\n"


def write_contributions_per_repo_to_file(data: list[str]):
    with open(f"{MD_PATH}/Contributions_per_Repository.md", "w") as f:
        f.writelines(data)