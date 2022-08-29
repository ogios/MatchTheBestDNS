import concurrent.futures as futures
from ping3 import ping
import pandas as pd
import numpy as np
import os, sys, click, keyboard, signal, json
os.system('')

def _exit(key):
    os.kill(os.getpid(),signal.SIGABRT)


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


def url_get():
    global urls
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


def pi(num):
    global pings
    global fatals
    while True:
        try:
            url=url_get()
            if not url:
                break
            l=[]
            print(num,'-',url)
            for i in range(10):
                ms=ping(url,unit='ms')
                if not ms:
                    print(url,'timeout')
                    break
                l+=[ms]
            l0=list(filter(None,l))
            if not l0:
                raise 'ping fatal'
            a=tuple([url]+[np.mean(l0),np.std(l0,ddof=1)]+l)
            pings+=[a]
        except Exception as e:
            print(e)
            fatals+=[tuple([url]+['None']*12)]


@click.command()
@click.option('--thread', default=4, help='Thread counts')
def main(thread):

    print(color('Press ESC to exit at anytime','green'))
    keyboard.on_press_key('esc',_exit)

    '''preparations'''
    global path
    global ok
    global fatal
    global pings
    global fatals
    global urls
    path=os.getcwd()
    ok=color('[ OK ]','green')
    fatal=color('[ FATAL ]','red')
    pings=[]
    fatals=[]
    _urls=open('./dns.json','r',encoding='utf8').read()
    urls=json.loads(_urls)
    '''preparations'''


    pool=futures.ThreadPoolExecutor(thread)
    tid=[i for i in range(1,thread+1)]
    threads=[pool.submit(pi,i) for i in tid]
    futures.wait(threads)

    print(urls)
    print(ok,pings)
    print(color('[ NoResponse ]','red'),fatals)
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
    df.to_excel(path+'\\ping_test.xlsx')



if __name__=="__main__":
    try:
        main()
    except Exception as e:
        with open('Error log.txt','w') as f:
            f.write(str(e))
        input(fatal+' '+str(e))

