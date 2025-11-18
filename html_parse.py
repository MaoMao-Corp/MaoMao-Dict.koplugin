from bs4 import BeautifulSoup
from WSD import stardict


word = input("word: ")

html = stardict[word]

soup = BeautifulSoup(html, "html.parser")

count = 0
for p in soup.find_all("p"):
    b = p.find("b", recursive=False)
    if b and (b.get_text(strip=True) == word.capitalize() or b.get_text(strip=True).endswith(".")):
        print("________\n", p.get_text())
        count+=1

print()
print(count)
