import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse (html):
    soup = BeautifulSoup(html)
    table = soup.find("table", class_="auctions w100")
    rows = table.find_all("td")
    #print(rows)
    projects = []
    c=1
    for row in rows:#table.find_all("td"):

        if c==1:
            projects.append({
            "PRODUCT":row.text})
            c=c+1

        elif c==2:
             projects.append({
            "COMPANY":row.text})
             c=c+1
        elif c==3:
             c=c+1
        elif c==4:
             c=c+1
        elif c==5:
             c=c+1

        elif c==6:
             projects.append({
            "DEAD LINE":row.text})
             c=c-5





    #print(c)

    projects=str(projects)
    print(projects)


def main():
    parse(get_html("http://www.icetrade.by/search/auctions?search_text=%D0%BC%D0%B5%D1%82%D0%B8%D0%B7%D1%8B&zakup_type%5B1%5D=1&zakup_type%5B2%5D=1&auc_num=&okrb=&company_title=&establishment=0&industries=&period=&created_from=&created_to=&request_end_from=&request_end_to=&t%5BTrade%5D=1&t%5BeTrade%5D=1&t%5BsocialOrder%5D=1&t%5BsingleSource%5D=1&t%5BAuction%5D=1&t%5BRequest%5D=1&t%5BcontractingTrades%5D=1&t%5Bnegotiations%5D=1&t%5BOther%5D=1&r%5B1%5D=1&r%5B2%5D=2&r%5B7%5D=7&r%5B3%5D=3&r%5B4%5D=4&r%5B6%5D=6&r%5B5%5D=5&sort=num%3Adesc&sbm=1&onPage=20"))

if __name__ == '__main__':
    main()





