from faker import Faker
import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split

fake = Faker()

compiled = []

for i in range(1,3):
    print(fake.words(1,ext_word_list=['100MB','500MB','1GB','3GB','5GB']))

    fake.name()


for i in range(1,1001):
    customer = {
        'name': fake.name(),
        'service_id': fake.msisdn(),
        'voice_usage': np.random.randint(1320),
        'data_usage': np.random.randint(69895),
        'sms_usage': np.random.randint(1320),
        'plan': fake.words(1,ext_word_list=['Smart Especial 1','Smart Especial 2','Smart Especial 3','Smart Especial 4','Smart Especial 5',
                                      'Smart Premium 1','Smart Premium 2','Smart Premium 3','Smart Premium 4','Smart Premium 5'])[0],
        'quantity': np.random.randint(30),
        'packages': fake.words(1,ext_word_list=['100MB','500MB','1GB','3GB','5GB'])[0],
        'upsale': ''
    }
    
    # print (customer)
    compiled.append(customer)

if(
    
):

print(compiled[0].keys())

customers = pd.DataFrame(compiled,columns=compiled[0].keys())

print(customers)

customers.to_csv('sample.csv')