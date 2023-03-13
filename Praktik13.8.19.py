ticket_ = int(input("введите количество билетов :"))
num_of = 0
price_ = 0
for i in range(ticket_):
    i += 1
    age = input(f'Для какого возраста билет №{i}? ')
    age = int(age)
    if age < 18:
            num_of +=1
            print("Билет бесплатный. ")
            print(f"количество билетов {num_of}, стоимость: {price_}")
    elif 25 > age >= 18:
            price_ += 990
            num_of +=1
            print("Стоимость билета: 990 руб.")
            print(f"количество билетов {num_of}, стоимость: {price_}")
    else:
            price_ += 1390
            num_of += 1
            print("Стоимость билета: 1390 руб.")
            print(f"количество билетов {num_of}, стоимость: {price_}")
if num_of > 3:
        price_ = price_ - ((price_ / 100) * 10)
        print(f'Сумма к оплате {price_} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-х человек')
else:
        print(f'Сумма к оплате {price_} руб.')
