import http.client as client
import xml.etree.ElementTree as etree
import sys


class ExchangeRate:

    _response = None
    _tree = None
    _date = None

    def __init__(self, source, path):
        try:
            conn = client.HTTPConnection(source)
            conn.request("GET", path)
            self._response = conn.getresponse().read()
            conn.close()
        except Exception:
            print("Error:", sys.exc_info()[0])
            print("Может стоит проверить подключение к интернету?")
            exit()

    def _get_tree(self):
        if self._tree:
            return self._tree

        try:
            self._tree = etree.fromstring(self._response)
        except Exception:
            print("Error:", sys.exc_info()[0])
            return None

        return self._tree

    def get_date(self):
        if not self._tree:
            self._get_tree()

        self._date = self._tree.attrib['Date']
        return self._date

    def get_currency(self, currency):
        if not self._tree:
            self._get_tree()

        for valute in self._tree:
            if valute.findall("CharCode")[0].text == currency:
                return "%s\n%s: %s" % (self.get_date(), valute.findall("Name")[0].text, valute.findall("Value")[0].text)
        return "%s\nВалюта не найдена" % self.get_date()

source = "www.cbr.ru"
path = "/scripts/XML_daily.asp"

ex = ExchangeRate(source, path)

new_currency = input("Введите код валюты: ")
print(ex.get_currency(new_currency))
