"""
1) Реалізувати функцію, яка порахує прибуток по таблиці invoice_items.
Сума по замовленню = UnitPrice * Quantity.
Прибуток = сумма замовлень. Якщо вирішуєте через sql,
то необхідно для суми викрористати агрегатну функцію sum.
2) Реалізувати функцію, которая виведе повторювані FirstName з таблиці customers
і кількість їх входжень в таблицю. Результат має виглядати як:

Марія 2

Микола 3.

Тобто виводимо тільки ті імена, які повторюються більше одного разу.
Якщо вирішуєте через sql, то використовуємо count та group by.

Приймаються рішення як з допомогою python, так і з sql.
"""

import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    for record in records:
        print(*record)


def get_profit() -> None:
    query_sql = '''
        SELECT SUM(UnitPrice * Quantity) 
            FROM invoice_items;
            '''
    result = execute_query(query_sql)
    unwrapper(result)


get_profit()


def get_double() -> None:
    query_sql = '''
        SELECT FirstName, COUNT(FirstName) AS Chosen
            FROM customers
        GROUP BY FirstName
        HAVING Chosen > 1;
    '''
    result = execute_query(query_sql)
    unwrapper(result)


get_double()

