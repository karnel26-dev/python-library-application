from datetime import datetime
from .crud import crud


MIN_YEAR = 1377
CURRENT_YEAR = datetime.today().year
STATUS_LIST = ('в наличии', 'на выдаче')

def validate_book_id(session, book_id: str):
    """
    Validating id of a book
    :param session: active session for db
    :param book_id: id of a book
    :return: id of a book or Exception
    """
    if not book_id.isdigit():
        raise ValueError('ID книги должен быть цифрой')
    if not crud.get_book_by_id(session, book_id):
        raise ValueError('Нет книги с таким ID')
    return book_id

def validate_year(year: str):
    """
    Validating year of publication of a book
    :param year: year of publication of a book
    :return: year of publication of a book or Exception
    """
    if isinstance(year, int):
        raise ValueError("Год издания должен быть строковым представлением года")
    if not year.isdigit():
        raise ValueError("Год издания должен быть цифрой")
    if not (MIN_YEAR < int(year) < CURRENT_YEAR):
        raise ValueError(f"Год издания должен быть c {MIN_YEAR} по {CURRENT_YEAR}")
    return year

def validate_status(status: str):
    """
    Validating status of a book
    :param status: status of a book
    :return: status of a book or Exception
    """

    if status.lower() not in STATUS_LIST:
        raise ValueError(f"Статус книги может быть {STATUS_LIST[0]} или {STATUS_LIST[1]}")
    return status


