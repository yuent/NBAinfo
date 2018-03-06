import bs4, requests, sys, pyperclip, re


if (len(sys.argv) > 1):
    player = ' '.join(sys.argv[1:])
    player = player.title()
else:
    player = pyperclip.paste()
    player = player.title()


def getPlayerAge():


    current = re.compile(r'''
    No \. \s \d+ \s . \s \w+ \s \w+
    ''', re.VERBOSE)
    
    nums = re.compile(r'''
    \d+ \s \/
    \s Round \:
    \s \d+ \s
    \/ \s
    Pick \:
    \s \w+

    ''',re.VERBOSE)

    

    res = requests.get('https://en.wikipedia.org/wiki/' + player)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    allScores = nums.findall(soup.get_text())
    if not allScores:
        print("That's not an NBA player!")
        sys.exit()
   
    cur = current.findall(soup.get_text())
    dc = allScores[0][:4]
    r = allScores[0][13:15]
    p = allScores[0][23:]

    if not cur:
        print(player + ' is currently retired. \n')
    else:
        current = cur[0].split(' ')
        yeam = ' '.join(current[3:])
        no = ' '.join(current[:2])
        print(player + ' currently plays for ' + yeam + ' and wears ' + no + '\n')
    
    print(player + ' was a part of the ' + str(dc) + ' draft class')
    print('he was drafted in round' + r)
    print('and was the' + p + ' overall pick')

    
getPlayerAge()
