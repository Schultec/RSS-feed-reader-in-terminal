import feedparser
import bs4

if __name__ == '__main__':
    # take in url
    url = input("please enter a rss feed url: ")
    # parse feed
    feed = feedparser.parse(url)
    for entry in feed['entries']:
        print("--------------------")
        print(entry['title'])
        # parse and display description
        desc = entry['description']
        desc = bs4.BeautifulSoup(desc, features="html.parser")
        desc = desc.get_text()
        print(desc)
        # display link
        print(entry['link'])