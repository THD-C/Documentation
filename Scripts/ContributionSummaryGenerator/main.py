from src.functions.GitHub import get_contributors_stats, get_repository_list
from src.functions.calculate import get_contribution_per_username
from src.functions.markdown import generate_overall_md_file, get_user_contributions, write_contributions_per_repo_to_file


def main():
    repo_list = get_repository_list("THD-C")
    
    result_per_repo = []
    contributions_per_repo_md = []
    
    contributions_per_repo_md.append("# Contributions to THD(c) app per Repository\n")
    for repo in repo_list:
        if repo.name == "Documentation":
            continue
        result = get_contributors_stats(repo.name)
        contributions_per_repo_md.append(f"## {repo.name}\n")
        contributions_per_repo_md.append("```diff\n")
        
        repo_authors = []
        for author in result.activity:
            author_summary = author.get_summary(repo.name)
            repo_authors.append(author_summary)
        
        repo_authors = sorted(repo_authors, key=lambda x: x.commits, reverse=True)  
        [result_per_repo.append(author) for author in repo_authors]
        [contributions_per_repo_md.append(get_user_contributions(author)) for author in repo_authors]
        contributions_per_repo_md.append("```\n")
        
    generate_overall_md_file(get_contribution_per_username(result_per_repo))  
    write_contributions_per_repo_to_file(contributions_per_repo_md)  

if __name__ == "__main__":
    main()
