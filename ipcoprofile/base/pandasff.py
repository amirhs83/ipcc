from .models import Date
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def find_index(id_value):
    dfbook = pd.read_csv('Book1.csv')
    dfbook = pd.DataFrame(dfbook)

    if id_value in dfbook['id'].values:
      return dfbook['id'].values.tolist().index(id_value)
    else:
      return None
def eskelet(id_search,listf):
    int = find_index(id_search)
    dfbom = pd.read_csv('bom.csv')
    dfbom = pd.DataFrame(dfbom)

    dfdaycreate = pd.read_csv('daycreate.csv')
    dfdaycreate = pd.DataFrame(dfdaycreate)
    dfbook = pd.read_csv('Book1.csv')
    dfbook = pd.DataFrame(dfbook)

    tolid = pd.read_csv('tolidrozaneh.csv')
    tolid = pd.DataFrame(tolid)

    tolid.fillna(0, inplace=True)
    dfdaycreate.fillna(0, inplace=True)
    dfbook.fillna(0, inplace=True)
    dfdaycreate = dfdaycreate.mul(dfbom.iloc[0])

    dfdaycreate["sumcreate"] = dfdaycreate.sum(axis=1)


    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    for i in range(0, 50):
        sum_row = tolid.iloc[i - 1, [0, 1, 2]].sum()
        new_row = [dfdaycreate["sumcreate"].loc[int], 0, sum_row]
        tolid.loc[i] = new_row

    days = Date.objects.all()
    daysoff = []
    for i in days:
        daysoff.append(i.name)

    dates = [datetime.today() + timedelta(days=i) for i in range(500)]
    dates_str = [date.strftime('%Y-%m-%d') for date in dates]
    for i in dates_str:
        if i in daysoff:
            dates_str.remove(i)

    tolid["datetolid"] = pd.DataFrame({'dates': dates_str})
    llist = []
    for i in range(0, len(tolid) - 1):
        for j in listf:
            if j == 'g1':

                if tolid.loc[i, 'datetolid'] in dfbook.loc[0, 'g1d']:
                    tolid.loc[i, 'gomrock'] = dfbook.loc[int, 'g1']
            if j == 'g2':
                if tolid.loc[i, 'datetolid'] in dfbook.loc[0, 'g2d']:
                    tolid.loc[i, 'gomrock'] = dfbook.loc[int, 'g2']
            if j == 'g3':

                if tolid.loc[i, 'datetolid'] in dfbook.loc[0, 'g3d']:
                    tolid.loc[i, 'gomrock'] = dfbook.loc[int, 'g3']
            if j == 'g4':

                if tolid.loc[i,'datetolid'] in dfbook.loc[0, 'g4d']:
                    tolid.loc[i, 'gomrock'] = dfbook.loc[int, 'g4']

        if tolid.loc[i, 'result'] <= 0:
            llist.append(tolid.loc[i, 'datetolid'])

    for i in range(0, len(tolid) - 1):
        tolid.loc[i + 1, 'result'] = tolid.loc[i, 'gomrock'] + tolid.loc[i, 'result'] + tolid.loc[i, 'tolid']

    labels_2=[]
    data_2=[]
    gomrock=[]
    tolidd=[]
    for i in range(0,len(tolid)):
        labels_2.append(tolid["datetolid"][i])
    for j in range(0,len(tolid)):
        data_2.append(tolid["result"][j])
    for i in range(0,len(tolid)):
        gomrock.append(tolid["gomrock"][i])
    for j in range(0,len(tolid)):
        tolidd.append(tolid["tolid"][j])
    return tolid,llist,labels_2,data_2,gomrock,tolidd

def en(list):
    labels=[]
    data=[]

    dfbook = pd.read_csv('Book1.csv')
    dfbook = pd.DataFrame(dfbook)
    dfbook.fillna(0, inplace=True)
    s = {}
    for i in range(0,len(dfbook)):
        sum=0
        for j in list:
            sum = dfbook[j][i]+sum



        s[i]=sum

    for i in s:
        labels.append(i)
        data.append(s[i])



    return labels,data














