#pip install requests
#pip install html5lib
#pip install bs4


url = "https://codewithharry.com"
r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content	# r returns response so if we want the code we write r.content
print(htmlContent)		# printing the code



import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify())	# to print html in tree structure


soup = BeautifulSoup(htmlContent, 'html.parser')

####idhar pe ham soup se refine kar rahe hai data ko

#baki chize dekhne ke liye inspect element kholo aur uske class ya id ko use karo
#soup.find('p')	# to find first paragraph
#soup.find('p')['class']	# to find class of first paragraph
#soup.find_all('p')	# to find all paragraphs


#rest all you can find it in documentation of beautifulsoup
#https://beautiful-soup-4.readthedocs.io/en/latest/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
