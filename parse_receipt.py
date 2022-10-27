from bs4 import BeautifulSoup


def parse_receipt(path_to_receipt):
    with open(path_to_receipt, "r", encoding="utf8") as file:
        body = file.read()
    soup = BeautifulSoup(body, features="lxml")

    items = soup.select('td.receipt-body div.item')
    header = soup.select_one('td.receipt-header2')

    receipt_num = header.select_one("td.receipt-col1 span.value").get_text()
    receipt_date = header.select_one("td.receipt-col2 span.value").get_text()

    print('Кассовый чек №', receipt_num, '\n'
          'Дата и время покупки:', receipt_date)
    print('\n')

    for item in items:

        title = item.select_one("table.receipt-row-1 span.value").get_text().split()
        amount, price = list(map(lambda x: " ".join(x.get_text().split()), item.select('table.receipt-row-2 td.receipt-col1 span.value')))
        total_price = item.select('table.receipt-row-2 td.receipt-col2 span.value')

        if "[М" in total_price[0].get_text():
            total_price = total_price[1:]

        total_price = total_price[0].get_text()

        print('Название:', ' '.join(title))
        print('Количество:', amount)
        print('Цена за один товар', price)
        print('Итоговая цена:', total_price)
        print('\n')


if __name__ == "__main__":
    parse_receipt("receipt_examples/receipt2.html")
