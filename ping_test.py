from threading import Thread as thread
from ping3 import ping
import pandas as pd
import numpy as np
import os
os.system('')
def color(string, color):
    dic = {
        'white': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'black': '\033[37m'
    }
    return dic[color]+string+'\033[0m'
ok=color('[ OK ]','green')
fatal=color('[ FATAL ]','red')

urls={
    'aili':[
        ('223.5.5.5',),
        ('223.6.6.6',)],
    '114':[
        ('114.114.114.114',),
        ('114.114.115.115',)],
    'tencent':[
        ('119.29.29.29',),
        ('182.254.118.118',)],
    "cnn":[
        ('1.2.4.8',),
        ('210.2.4.8',)],
    'one':[
        ('112.124.47.27',),
        ('114.215.126.16',)],
    'dnspie':[
        ('101.226.4.6',),
        ('218.30.118.6',)],
    'dnspie_liantong':[
        ('123.125.81.6',),
        ('140.207.198.6',)],
    'google':[
        ('8.8.8.8',),
        ('8.8.4.4',)],
    'opendns':[
        ('208.67.222.222',),
        ('208.67.220.220',)],
    'v2exdns':[
        ('199.91.73.222',),
        ('178.79.131.110',)],
    'openerdns':[
        ('42.120.21.30',)],
}

pings=[]
fatals=[]

def url_get(urls=urls):
    b=1
    # print(urls)
    for i in urls:
        if urls[i]:
            for a in urls[i]:
                url=a[0]
                del urls[i][0]
                # print(urls)
                b=0
                break
        else:
            url=0
        if not b:
            break
    return url


def pi():
    global pings
    global fatals
    while True:
        try:
            url=url_get()
            if not url:
                break
            l=[]
            for i in range(10):
                l+=[ping(url,unit='ms')]
            l0=list(filter(None,l))
            if not l0:
                raise 'ping fatal'
            a=tuple([url]+[np.mean(l0),np.std(l0,ddof=1)]+l)
            pings+=[a]
        except Exception as e:
            print(url)
            print(l)
            print(e)
            fatals+=[tuple([url]+['None']*12)]

if __name__=="__main__":
    p1=thread(target=pi)
    p2=thread(target=pi)
    p3=thread(target=pi)
    p4=thread(target=pi)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print(urls)
    print(ok,pings)
    print(fatal,fatals)
    pings.sort(key=lambda x:x[1])
    pings+=fatals
    print(ok,pings)
    # print(pings)
    l=[]
    for i in range(10):
        l+=[i+1]
    df=pd.DataFrame(pings,columns=['IP','平均时常','离散度(方差)']+l)
    df.fillna('None')
    # print(df)
    df.to_excel('./ping_test.xlsx')
