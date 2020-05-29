#solving the 2nd challenge
#http://www.pythonchallenge.com/pc/def/map.html

'''
hint
K -> M
O -> Q
E -> G

everybody thinks twice before solving this.
'''


def get_translation(challenge: str, unlock: str):

    new_string: str = ""

    for letter in challenge:
        if letter in unlock:
            index: int = unlock.find(letter) + 2
            if index >= len(unlock):
                length: int = index - len(unlock)
                index = length
            new_string += unlock[index]
        else:
            new_string += letter
    return new_string


def challenge():
    challenge: str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagcl" \
                     "r ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    current_url: str = 'http://www.pythonchallenge.com/pc/def/map.html'
    phrase: str = get_translation(challenge, alphabet)
    print(f'This sould be the sentence: {phrase}\n')

    # so we need to use the same method do get the new URL
    answser: str = get_translation('map', alphabet)
    print(f"And the next challenge is in: {current_url.replace('map', answser)}")


if __name__ == "__main__":
    challenge()
