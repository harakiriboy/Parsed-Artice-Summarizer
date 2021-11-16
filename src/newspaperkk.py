import newspaper
from newspaper import Article


def getarticle(url):
    articleurl = url
    article = Article(articleurl)
    try:
        article.download()
        article.parse()
        alltext = article.text
        return alltext
    except:
        return "this website is not available"


