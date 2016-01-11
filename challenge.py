import pandas as pd

mta = pd.read_csv('MTA/turnstile_160109.txt')

mta['key'] = zip(mta['C/A'], mta['UNIT'], mta['SCP'], mta['STATION'])


mta_dict = dict()

for index, row in mta.iterrows():
	value = row[3:10].tolist()
	key = row['key']
	print key, value
	
	if key in mta_dict:
		mta_dict[key].append(value)
	else:
		mta_dict[key] = value




