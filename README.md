# MatchTheBestDNS

> Based on Python3

## Packages required

|Package(2.0)|Package(2.1)|
|----|---|
|Pandas|Pandas|
|Numpy|Numpy|
|ping3|ping3|
|     |click|
|     |keyboard|

if not installed: ``` pip install <package> ```

## Details

- In 2.1 you can add dns in the given json file.

- In 2.1 you can configurate thread counts on your own in shell command using `--thread <num>` (default 4).    
example: ```python ping_test2.1.py --thread 10```

- If error occurs, the details will be reserved in a new generated txt file.

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
## Example
![preview](https://user-images.githubusercontent.com/96933655/187014508-61cd1f3b-aab6-482f-b4d8-bb2696f8651e.png)
