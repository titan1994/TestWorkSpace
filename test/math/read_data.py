import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = 'example.csv'

list_max_temp, list_min_temp, list_date_time = [], [], []

with open(file_name) as fobj:
    reader = csv.reader(fobj)

    header_row = next(reader)
    print(header_row)
    #
    # next_list = enumerate(header_row)
    #
    # for index, column_header in next_list:
    #     print(index, column_header)

    for row in reader:
        # print(row)
        list_min_temp.append(int(row[2]))
        list_max_temp.append(int(row[1]))
        tt = datetime.strptime(row[0], '%Y-%m-%d')
        list_date_time.append(tt)

print(list_max_temp)
print(list_date_time)

# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(list_max_temp, c='red')
# Р¤РѕСЂРјР°С‚РёСЂРѕРІР°РЅРёРµ РґРёР°РіСЂР°РјРјС‹.
# plt.title("Daily high temperatures, July 2014", fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.show()

# РќР°РЅРµСЃРµРЅРёРµ РґР°РЅРЅС‹С… РЅР° РґРёР°РіСЂР°РјРјСѓ.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(list_date_time, list_max_temp, c='red')
plt.plot(list_date_time, list_min_temp, c='green')
plt.fill_between(list_date_time, list_max_temp, list_min_temp, facecolor='blue', alpha=0.1)
# Р¤РѕСЂРјР°С‚РёСЂРѕРІР°РЅРёРµ РґРёР°РіСЂР°РјРјС‹.
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
