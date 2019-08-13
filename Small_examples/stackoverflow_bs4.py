# Simple reader by bs4

import requests
from bs4 import BeautifulSoup
import json

# Target
response_from_www = requests.get('https://stackoverflow.com/questions')

# Logic
soup_reader = BeautifulSoup(response_from_www.text, 'html.parser')

questions_from_www = {
    'questions': []
}

questions = soup_reader.select('.question-summary')

# Iterate between result
for existing_question in questions:
    ask_question = existing_question.select_one('.question-hyperlink').getText()
    vote_count = existing_question.select_one('.vote-count-post').getText()
    views = existing_question.select_one('.views').attrs['title']
    questions_from_www['questions'].append({
        'questions':ask_question,
        'views': views,
        'vote_count': vote_count
    })

json_data_list = json.dumps(questions_from_www)
print(json_data_list)