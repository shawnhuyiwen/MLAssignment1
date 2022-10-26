import pandas as pd

data = pd.read_table('diagnosis.data', encoding="utf-16", header=None) 
data.columns = ['Temperature of patient',  'Occurrence of nausea', 'Lumbar pain', 'Urine pushing', 'Micturition pains', 'Burning of urethra, itch, swelling of urethra outlet', 'Decision: Inflammation of urinary bladder', 'Decision: Nephritis of renal pelvis origin']

for i in range(len(data['Temperature of patient'])):
    num = float(data['Temperature of patient'][i].replace(',','.'))
    data['Temperature of patient'][i] = num

data.replace('yes', 1, inplace=True)
data.replace('no', 0, inplace=True)
data.to_csv('diagnosis.csv',sep=',',index=False)

