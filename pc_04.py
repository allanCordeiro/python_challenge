import urllib.request
import re

# solving the 5th challenge
# http://www.pythonchallenge.com/pc/def/linkedlist.html


def main():
    uri: str = "http://www.pythonchallenge.com/pc/def/"
    link: str = "linkedlist.php"

    first_execution_url = execute(uri, link)
    print(first_execution_url)
    execute(uri, first_execution_url[0], first_execution_url[1], 400)


def execute(uri, link, querystring="", no_execution=0):
    if no_execution == 0:
        with urllib.request.urlopen(f"{uri}{link}") as response:
            html = response.read().decode('utf-8')
            new_url = scrapper(html)
            return url_dehydrate(new_url)

    # recursive
    counter = 1
    while True:
        with urllib.request.urlopen(f"{uri}{link}={querystring}") as response:
            html = response.read().decode('utf-8')
            next_nothing = text_split(html)
            if next_nothing:
                querystring = next_nothing
            elif "Divide by two" in html:
                querystring = str(int(querystring) // 2)
            else:
                print(f"This is the the URL you should follow: {uri}{html}")
                print("Challenge completed.")
                break

            print(f"{counter} :: {html} :: next :: {querystring}")
            counter += 1


def text_split(sentence):
    return "".join(re.findall('the next nothing is ([0-9]*)', sentence))


def scrapper(html):
    tags = html.split("\n")
    return tags


def url_dehydrate(tags):
    url_found = []
    for tag in tags:
        if "nothing" in tag:
            url_found = tag.split('"')

    for url in url_found:
        if "nothing" in url:
            return url.split("=")


if __name__ == "__main__":
    main()

