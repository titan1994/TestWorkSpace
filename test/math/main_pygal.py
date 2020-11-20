try:
    import pygal
except ModuleNotFoundError:
    import os
    os.system('pip install pygal')

from RandomCube import Die

result_list = []
diecub = Die()

for roll_num in range(1000):
    res = diecub.roll()
    result_list.append(res)

frequencies = []
for value in range(1, diecub.num_sides+1):
    frequency = result_list.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6_1', frequencies)
hist.add('D6_2', frequencies)
hist.render_to_file('die_visual.svg')
