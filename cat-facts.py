import http.client
import json
from collections import Counter
import re

conn = http.client.HTTPSConnection("cat-fact.herokuapp.com")
conn.request("GET", "/facts/random?animal_type=cat&amount=10")
response = conn.getresponse()
data = response.read().decode("utf-8")
facts = json.loads(data)

cat_facts = [fact['text'] for fact in facts]
all_text = " ".join(cat_facts)

#wanted to make it all the case the same so the same word but different capitalization will not count as different strings
words = re.findall(r'\b\w+\b', all_text.lower())
word_counts = Counter(words)

top_5_words = word_counts.most_common(5)

# Display the cat facts and top 5 words
print("Cat Facts:")
for i, fact in enumerate(cat_facts, 1):
    print(f"{i}. {fact}")

print("\nTop 5 Most Used Words:")
for word, count in top_5_words:
    print(f"{word}: {count} times")

conn.close()
