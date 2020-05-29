#Solving the 1st challenge
#http://www.pythonchallenge.com/pc/def/0.html

def first_challenge():
    num: int = 2
    return f'{num ** 38}'

def new_url():
    url = "http://www.pythonchallenge.com/pc/def/0.html"
    url = url.replace("0", first_challenge())
    print(f'paste this result as http url browser:\n{url}')

if __name__ == "__main__":
    new_url()