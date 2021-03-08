from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.infomoney.com.br/onde-investir/os-fundos-imobiliarios-preferidos-dos-analistas-para"
                   "-comprar-em-marco/?ifm=IM-INVL-MTR-IM-X-20210305-OP-X-X-X&utm_source=infomoney&utm_campaign"
                   "=IM20210305&utm_source=infomoney&utm_medium=email&utm_campaign=20210305/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(), "html5lib")

    if res.title is None:
        print("T&iacute;tulo n&atilde;o encontrado")
    else:
        print("Infomoney - " + res.title.getText() + "\n")

    tags = res.findAll("td", {"style": "width: 25%;height: 22px;text-align: center"})
    cods = res.findAll("td", {"style": "width: 25%;text-align: center;height: 22px"})

    numFii = len(tags)
    numCod = len(cods)

    x = 0
    y = 0

    while x < numFii:
        while y < numCod:
            print(tags[y].getText() + " " + cods[y].getText())
            y += 1
        x += 1


