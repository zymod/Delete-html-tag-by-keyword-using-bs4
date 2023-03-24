from bs4 import BeautifulSoup


html = '''
<h1>Green turtle</h1>
<p>the turtle is patient</p>
'''

keyword = 'green'

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all():
	if tag.string and keyword.lower() in tag.string.lower():
		tag.decompose()
		html = str(soup)
