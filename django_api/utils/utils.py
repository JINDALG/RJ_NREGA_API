from api.models import District, Employee
import json
import random

genders = ['FEMALE', 'MALE', 'FEMALE']


def upload_data():
    file = "/home/shivji/Downloads/2704.json"
    file = open(file, 'r')
    data = json.loads(file.read())
    # print type(data.get('nregaDetailsList'))
    # print data.get('nregaDetailsList')[0].keys()
    for a in data.get('nregaDetailsList')[:100]:
        if a.get('AADHAR_ID') and a['NAME'] and a['BDH_DISTRICT']:
            print a.get('AADHAR_ID')
            di = District.objects.get(district_id=a['BDH_DISTRICT'])
            Employee.objects.create(
                emp_aadhar=a.get('AADHAR_ID'), name=a['NAME'], district=di, gender=random.choice(genders))


def get_name(obj):
    if 'name' in obj:
        return obj['name']
    return obj['district__name']


def analysis():
    import pandas as pd, pprint, matplotlib.pyplot as plt, numpy as np
    districs = {'district': District.objects.all().values('district_id', 'name')}
    ds = districs['district']
    names = map(get_name, ds)
    emps = map(get_name,Employee.objects.all().values('district__name'))
    #print emps
    numarr = np.array(emps)
    df = pd.DataFrame(data=numarr)
    print df.head()
    df.columns = ['districts']
    print df
    #plt.hist(, len(numarr))
    #plt.hist(df['districts'])
    #df.districts.value_counts().plot(kind='bar')
    df.groupby('districts').size().plot(kind='bar')
    #plt.hist(df['districts'])
    plt.xlabel('Districts')
    plt.ylabel('Number of employees')
    plt.show()
    print "ned"
    #df.districts.value_counts().plot(kind='bar')