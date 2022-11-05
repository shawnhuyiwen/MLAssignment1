import pandas as pd

data = pd.read_table('breast-cancer.data', encoding="utf-8", header=None, sep=',') 
data.columns = ['Class', 'Age', 'Menopause', 'Tumor-size', 'Inv-nodes', 'Node-caps', 'Deg-malig', 'breast', 'breast-quad', 'Irradiant']

for i in range(len(data['Age'])):
    num = int(data['Age'][i][0:2])/10
    data['Age'][i] = num

data.insert(3, 'lt40', 0)
data.insert(4, 'ge40', 0)
data.insert(5, 'premeno', 0)

for i in range(len(data['Menopause'])):
    temp = data['Menopause'][i]
    if temp == 'lt40':
        data['lt40'][i] = 1
    elif temp == 'ge40':
        data['ge40'][i] = 1
    elif temp == 'premeno':
        data['premeno'][i] = 1

data.drop(columns=['Menopause'], inplace=True)

for i in range(len(data['Tumor-size'])):
    num = int(data['Tumor-size'][i].split('-')[0])/5 + 1
    data['Tumor-size'][i] = num

for i in range(len(data['Inv-nodes'])):
    num = int(data['Inv-nodes'][i].split('-')[0])/3 + 1
    data['Inv-nodes'][i] = num
    
print(type(data['Deg-malig'][0]))

data.replace({'no-recurrence-events': 0, 'recurrence-events': 1}, inplace=True)
data.replace({'yes': 1, 'no': 0, '?': 2}, inplace=True)
data.replace({'left': 1, 'right': 0}, inplace=True)
data.replace({'left_up': 1, 'left_low': 2, 'right_up': 3, 'right_low': 4, 'central': 5}, inplace=True)
data.to_csv('breast-cancer.csv',sep=',',index=False)
