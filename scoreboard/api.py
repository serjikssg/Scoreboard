import requests, sys, json


b = requests.get('https://api.safisense.com/api/v1/devices/uptime?company_id=apikirkcontainers&api_key=7EeFK8fnXsecJkSOSaYvJ98kF4YVPVHY')


print('-------------------------------------')
print('-------- API Kirk Containers --------')
print('-------------------------------------\n')


ma = {}

for i in b.json()['data']:
    try:
        if i['computedLoadStates']['percentages']['online'] >= 0:
            if i['computedLoadStates']['percentages']['online'] > 0:
                ma[int(i['deviceid'].split('machine')[1])] = i['computedLoadStates']['percentages']['online']
            else:
                ma[int(i['deviceid'].split('machine')[1])] = i['computedLoadStates']['percentages']['online']
    except:
        ...


li = list(ma.keys())

ma_list = []
j = 0

for m in sorted(li):
    if ma[m] > 0:
        # print (f"\033[1;32m Machine {m:<2} is {round(ma[m]*100)}% \033[0;0m")
        ma_list.append([m, 'bg-success', 0, 0])
        j += 1
    else:
        # print (f"\033[1;31m Machine {m:<2} is {ma[m]}% \033[0;0m")
        ma_list.append([m, 'bg-danger', 1, 0])
        j += 1

print('\n-------------------------------------')
print (ma_list)
