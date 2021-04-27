



data = [
    {'user': 'digital', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'sam', 'email': 'digital', 'age': 23, 'salary': 200000, 'department': 'manager'},
    {'user': 'john', 'email': 'john@google.com', 'age': 23, 'salary': 200000, 'department': 'CEO'},
    {'user': 'sparrow', 'email': 'digital@go.com', 'age': 23, 'salary': 200000, 'department': 'SEO'},
    {'user': 'orlando', 'email': 'digital@gmail.com', 'age': 23, 'salary': 200000, 'department': 'food'},
    {'user': 'ben', 'email': 'digi', 'age': 23, 'salary': 200000, 'department': 'worker'},
    {'user': 'stiller', 'email': 'digital@apple.com', 'age': 23, 'salary': 200000, 'department': 'loan'},
    {'user': 'adam', 'email': 'email@email.com', 'age': 23, 'salary': 200000, 'department': 'credit'},
    {'user': 'eva', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'buying'},
    {'user': 'frodo', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'harry', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'ron', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'germiona', 'email': 'digit', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'gannibal', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'food'},
    {'user': 'lector', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'food'}
]
worker_of_month = {'IT': ['adam', 'sparrow', 'ben', 'frodo', 'gannibal'],
                   'credit': [],
                   'loan': ['stiller'],
                   'food': ['gannibal', 'lector']}
"""
1.Всем работникам месяца увеличить зарплату на 10%
2.Отделу где больше одного работников месяца увеличить зарплату на 5% дополнительно
3.Отдел где нет работников месяца - уменьшить всем зарплату на 3%
4.Работники чьи email-не принадлежат гуглу все кроме [@google.com,@gmail.com] - уволить
"""
#


def worker_of_month_increase_salary(data,worker_of_month):
    for worker_key,worker_value in worker_of_month.items():
        for worker in worker_value:                               #1 пункт
            for user in data:
                if user['user'] == worker:
                    user['salary'] = user['salary'] + (user['salary'] * 0.1)
    return data

data = worker_of_month_increase_salary(data,worker_of_month)

def best_departments(data,worker_of_month):
    pass
print(data)

def remove_worker(data=data):
    data_copy = data.copy()
    for user in data_copy:
        email = user['email']
        if '@google.com' in email or '@gmail.com' in email:     # 4 пункт
            pass
        else:
            data.remove(user)
    return data
data = remove_worker(data=data)
print(data)










