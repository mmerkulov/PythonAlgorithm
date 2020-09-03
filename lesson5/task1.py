import collections

# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего

amount_company = int(input('Entry amount company: '))
i = 0
company_data = {}
# Вводим именование компании
while i < amount_company:
    company_name = input('Entry company name: ')
    m = 1
    profit_array = []
    while m < 5:
        profit = int(input(f'Введите прибыль за {m} квартал: '))
        profit_array.append(profit)
        m += 1
    company_line = {company_name: profit_array}
    company_data.update(company_line)
    i += 1

print(company_data)
company_data_1 = {}
avg_sum = 0
for key, value in company_data.items():
    total_sum = sum(value)
    avg_sum = avg_sum + total_sum
    company_data_line = {key: total_sum}
    company_data_1.update(company_data_line)

avg_sum = avg_sum / len(company_data_1.keys())

print(f'Средяя сумма по всем компаниям = {avg_sum}')
for key, value in company_data_1.items():
    print(f'+ {key}') if value >= avg_sum else print(f'- {key}')
