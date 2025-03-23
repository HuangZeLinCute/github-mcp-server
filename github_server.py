from github import Github
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize GitHub client
g = Github(os.getenv('GITHUB_TOKEN'))

# Initialize FastMCP server
mcp = FastMCP('GitHub MCP Server')

@mcp.tool()
def general_search(keyword: str) -> dict:
    """
    Search GitHub repositories with the given keyword.

    Args:
        keyword: Search term to look for on GitHub

    Returns:
        Dictionary containing the search results from GitHub API.
    """
    result = g.search_repositories(query=keyword, sort="stars", order="desc")
    
    return {
        "total_count": result.totalCount,
        "items": [{"name": repo.name, "url": repo.html_url, "description": repo.description} for repo in result]
    }

if __name__ == '__main__':
    mcp.run(transport='stdio')
