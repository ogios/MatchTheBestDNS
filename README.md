# MatchTheBestDNS

> Mainly Python

## Packages required
|Package|
|----|
|Pandas|
|Numpy|
|ping3|

if not installed: ``` pip install <package> ```

## Details
default 10 time pings:
``` 
for i in range(10):
    l+=[ping(url,unit='ms')]
```
And 2 indicators
|平均时长|离散度(方差)|
|--|--|
|Average time|Statistical Dispersion(std)|

the smaller, the better
## Preview
![preview](https://user-images.githubusercontent.com/96933655/187014508-61cd1f3b-aab6-482f-b4d8-bb2696f8651e.png)
