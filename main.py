from datetime import datetime
from application.db.people import print_people
from application.salary import print_salary

if __name__ == '__main__':
    print(f'Текущая дата/время: {datetime.now()}')
    print(f'Функция из модуля: {print_people()}')
    print(f'Функция из модуля: {print_salary()}')