from django.db import models
class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.title

  import requests
  from bs4 import BeautifulSoup

  r = requests.get("https://timesofindia.indiatimes.com/briefs")
  soup = BeautifulSoup(r.content, 'html5lib')

  headings = soup.find_all('h2')

  headings = headings[0:-13]  # removing footer links