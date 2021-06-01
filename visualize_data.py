import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_no_emergency = pd.read_csv('trip_info_no_emergency.csv')
file_emergency = pd.read_csv('trip_info_emergency.csv')

file_emergency = file_emergency.drop(['departLane', 'departPos', 'departSpeed',
                                     'arrivalLane', 'arrivalSpeed', 'rerouteNo',  'devices', 'vaporized', 'arrivalPos'], axis=1)
file_no_emergency = file_no_emergency.drop(
    ['departLane', 'departPos', 'departSpeed', 'arrivalLane', 'arrivalSpeed', 'rerouteNo',  'devices', 'vaporized', 'arrivalPos'], axis=1)


file_emergency['avg_speed'] = file_emergency['routeLength'] / \
    file_emergency['duration']

file_no_emergency['avg_speed'] = file_no_emergency['routeLength'] / \
    file_no_emergency['duration']

file_emergency = file_emergency.replace(
    {'vType': {'DEFAULT_VEHTYPE': 'Normal Vehicles', 'bus': 'Emergency Vehicles'}})
file_no_emergency = file_no_emergency.replace(
    {'vType': {'DEFAULT_VEHTYPE': 'Normal Vehicles', 'bus': 'Emergency Vehicles'}})

avg_duration_emergency_in_emergency = (file_emergency.query('vType == "Emergency Vehicles"')['duration'].sum())/file_emergency.query('vType == "Emergency Vehicles"').shape[0]
avg_duration_no_emergency_in_emergency = (file_emergency.query('vType == "Normal Vehicles"')['duration'].sum())/file_emergency.query('vType == "Normal Vehicles"').shape[0]

avg_duration_emergency_in_no_emergency = (file_no_emergency.query('vType == "Emergency Vehicles"')['duration'].sum())/file_no_emergency.query('vType == "Emergency Vehicles"').shape[0]
avg_duration_no_emergency_in_no_emergency = (file_no_emergency.query('vType == "Normal Vehicles"')['duration'].sum())/file_no_emergency.query('vType == "Normal Vehicles"').shape[0]

print(avg_duration_emergency_in_emergency)
print(avg_duration_no_emergency_in_emergency)

print(avg_duration_emergency_in_no_emergency)
print(avg_duration_no_emergency_in_no_emergency)



sns.set(font_scale=1.5)
sns.lmplot(x='timeLoss', y='avg_speed', data=file_emergency,
           hue='vType').set(title='Priority to Emergency Vehicles')
plt.gcf().set_size_inches(12, 8)
plt.ylabel("Average Speed")
plt.xlabel("Loss of Time")
plt.show()

sns.set(font_scale=1.5)
sns.lmplot(x='timeLoss', y='avg_speed', data=file_no_emergency,
           hue='vType').set(title='No Priority to Emergency Vehicles')
plt.gcf().set_size_inches(12, 8)
plt.ylabel("Average Speed")
plt.xlabel("Loss of Time")
plt.show()

sns.set(font_scale=1.5)
sns.jointplot(x='depart', y='timeLoss', data=file_emergency,
           hue='vType')
plt.gcf().set_size_inches(12, 8)
plt.ylabel("Time of Departure")
plt.xlabel("Loss of Time")
plt.show()

sns.set(font_scale=1.5)
sns.jointplot(x='depart', y='timeLoss', data=file_no_emergency,
           hue='vType')
plt.gcf().set_size_inches(12, 8)
plt.ylabel("Time of Departure")
plt.xlabel("Loss of Time")
plt.show()