"""MIT License

Copyright (c) 2020 Björn Plüster

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
from typing import Tuple

from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import date, timedelta
from transactions import Transaction


def clean_date(date_string: str) -> date:
    """
    'Cleans' the date found in PayPal html. Instead of using a date,
    they use 'today' and 'yesterday' or 'heute' and 'gestern' in
    german respectively.

    :param date_string: The date string found in the html
    :return: a date corresponding to the input
    """
    if date_string in ["gestern", "yesterday"]:
        return date.today() - timedelta(days=1)
    elif date_string in ["heute", "today"]:
        return date.today()
    else:
        return parse(date_string).date()


def get_transaction_data(transaction: BeautifulSoup) -> Transaction:
    """
    Gets the valuable data from a single transaction.

    :param transaction: the BeautifulSoup of a transaction found in
    paypal transactions html
    :return: a tuple of (name of other party, transaction amount, date)
    """
    name = transaction.find("strong", {"class": "counterparty-text"}).string.strip()

    amount_soup = transaction.find("span", {"class": "netAmount"})
    # html is different for receiving and sending transactions
    if not amount_soup:
        amount_soup = transaction.find_all("span", {"class": "isPositive"})[1]
        amount = float(amount_soup.string.replace(",", "."))
    else:
        amount = -float(amount_soup.string.replace(",", "."))

    time_soup = transaction.find("span", {"class": "relative-time"})
    date_string = time_soup.next

    category = time_soup.findChild("div")

    return Transaction(name, amount, clean_date(date_string), category.next)
