import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_no_emergency = pd.read_csv('trip_info_no_emergency.csv')
file_emergency = pd.read_csv('trip_info_emergency.csv')

print(file_no_emergency.shape)
print(file_emergency.shape)

file_emergency = file_emergency.drop(['departLane', 'departPos', 'departSpeed',
                                     'arrivalLane', 'arrivalSpeed', 'rerouteNo',  'devices', 'vaporized', 'arrivalPos'], axis=1)
file_no_emergency = file_no_emergency.drop(
    ['departLane', 'departPos', 'departSpeed', 'arrivalLane', 'arrivalSpeed', 'rerouteNo',  'devices', 'vaporized', 'arrivalPos'], axis=1)


file_emergency['avg_speed'] = file_emergency['routeLength']/ file_emergency['duration']

file_no_emergency['avg_speed'] = file_no_emergency['routeLength']/ file_no_emergency['duration']


for val in  file_emergency['avg_speed']:
    if(val<0):
        print(val)


sns.set(font_scale=1.5)
sns.lmplot(x='timeLoss', y='avg_speed', data = file_no_emergency, 
           hue='vType')
plt.gcf().set_size_inches(12, 8)
plt.ylabel("Average Speed")
plt.xlabel("Loss of Time")
plt.show()


print(file_no_emergency.head)
print(file_emergency.head)
