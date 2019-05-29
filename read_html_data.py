import lxml.html as lh
from urllib.request import urlopen


def get_text():
    # import requests
    # page = requests.get(url)
    # doc = lh.fromstring(page.content)
    html = urlopen("file:///C:\html_files\sample.html")
    html_doc = html.read()
    doc = lh.fromstring(html_doc)

    td_elements = doc.xpath('//td')

    td_data = []
    for j, d in enumerate(td_elements):
        td_data.append(d.text_content())


if __name__ == '__main__':
    get_text()
