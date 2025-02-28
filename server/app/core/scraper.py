from bs4 import BeautifulSoup
from leetscrape import GetQuestion

class LeetCodeScraper:
    def __init__(self):
        pass

    def clean_html_description(self, html_content: str) -> str:
        # Parse the HTML using BeautifulSoup and extract the text
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.get_text()

    def get_question(self, url: str) -> str:
        # Get the problem details using the GetQuestion class
        title = url.split("/")[4]
        problem = GetQuestion(titleSlug=title).scrape()

        # Clean the HTML description
        clean_description = self.clean_html_description(problem.Body)

        # Format the problem information into a string
        problem_info = f"**Title:** {problem.title}\n"
        problem_info += f"**Description:** {clean_description}\n"
        problem_info += f"**Difficulty:** {problem.difficulty}\n"
        problem_info += f"**Tags:** {', '.join(problem.topics)}"

        return problem_info


