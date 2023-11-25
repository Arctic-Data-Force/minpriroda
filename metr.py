import pandas as pd

df1 = pd.read_csv('result.csv')
df2 = pd.read_csv('predict.csv')


def check_row(row1, row2):
    def check_quantity(qty1, qty2):
        if qty1 == 0:
            return 0 if qty2 == 0 else 1
        return abs(qty2 - qty1) / qty1

    def check_speed(speed1, speed2):
        return abs(speed2 - speed1)

    car_quantity = check_quantity(row1['quantity_car'], row2['quantity_car'])
    van_quantity = check_quantity(row1['quantity_van'], row2['quantity_van'])
    bus_quantity = check_quantity(row1['quantity_bus'], row2['quantity_bus'])

    car_speed = check_speed(row1['average_speed_car'], row2['average_speed_car'])
    van_speed = check_speed(row1['average_speed_van'], row2['average_speed_van'])
    bus_speed = check_speed(row1['average_speed_bus'], row2['average_speed_bus'])

    car_condition = car_quantity <= 0.1 and car_speed <= 10
    van_condition = van_quantity <= 0.2 and van_speed <= 10
    bus_condition = bus_quantity <= 0.2 and bus_speed <= 10
    
    return car_condition and van_condition and bus_condition

correct_count = 0
incorrect_count = 0

for index, row1 in df1.iterrows():
    file_name = row1['file_name']
    corresponding_row_df2 = df2[df2['file_name'] == file_name]

    if not corresponding_row_df2.empty:
        row2 = corresponding_row_df2.iloc[0] 
        if check_row(row1, row2):
            correct_count += 1
        else:
            incorrect_count += 1

print(f"Ок: {correct_count}\nНе ок: {incorrect_count}")
