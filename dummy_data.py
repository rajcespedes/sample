from faker import Faker
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

fake = Faker()

compiled = []


list=['Smart Especial 1','Smart Especial 2','Smart Especial 3','Smart Especial 4','Smart Especial 5',
      'Smart Premium 1','Smart Premium 2','Smart Premium 3','Smart Premium 4','Smart Premium 5']


def generate_dataset():
    for i in range(1,1001):
        customer = {
            'name': fake.name(),
            'service_id': fake.msisdn(),
            'voice_usage': np.random.randint(1,1320),
            'data_usage': np.random.randint(1,69895),
            'sms_usage': np.random.randint(1,1320),
            'plan': fake.words(1,ext_word_list=['Smart Especial 1','Smart Especial 2','Smart Especial 3','Smart Especial 4','Smart Especial 5',
                                        'Smart Premium 1','Smart Premium 2','Smart Premium 3','Smart Premium 4','Smart Premium 5'])[0],
            'quantity': np.random.randint(30),
            'packages': fake.words(1,ext_word_list=['100','500','1024','3072','5120'])[0],
            'upsale': ''
        }
   
        compiled.append(customer)
    
    
    return compiled


data = generate_dataset()


for i in data:
    if(list.index(i['plan']) == 9):
        i['upsale'] = ''
    else:
        num = list.index(i['plan'])
        i['upsale'] = list[num + 1]
    

df = pd.DataFrame(data, columns=data[0].keys())

print(df)
    
# df.to_csv('sample.csv')

# x = df.drop('upsale', axis=1)

# y = df['upsale']

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# model = LinearSVC()

# model.train()


# print(y)

