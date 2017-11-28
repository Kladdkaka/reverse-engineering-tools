"""Usage: htmldiff.py <url>

Arguments:
  url        URL to diff!
Options:
  -h --help
"""
from html5print import HTMLBeautifier
from docopt import docopt
import requests
import webbrowser

new = 2  # open in a new tab, if possible

arguments = docopt(__doc__)
print(arguments)

url = arguments['<url>']

s = requests.session()
authToken = None


def get_html():
    r = requests.get(url)
    html = HTMLBeautifier.beautify(r.text, 2)
    return html


def get_session():
    global authToken
    r = requests.post('https://diffchecker-api-production.herokuapp.com/sessions', data={
        'email': 'qoxudufy@cars2.club',
        'password': 'qoxudufy@cars2.club'
    })

    authToken = r.json()['authToken']


def upload(html1, html2):
    r = requests.post('https://diffchecker-api-production.herokuapp.com/diffs', data={
        'left': html1,
        'right': html2,
        'expiry': 'forever',
        'title': None
    })

    return 'https://www.diffchecker.com/' + r.json()['slug']


htmls = [get_html(), get_html()]

get_session()

result_url = upload(htmls[0], htmls[1])

webbrowser.open(result_url, new=new)
