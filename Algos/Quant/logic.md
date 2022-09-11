# Wight out

```py
def weight(number):
    if -0.1 < number < 0.1:
        return 0
    if number > 0.1:
        return 1
    if number < -0.1:
        return 2
```

vars that change weight

change in hash rate

Before weight shifting
24805

34654

At
0.1 = 24370
0.2 = 22545
0.3 = 29236
0.4 = 36912
0.5 = 32654
0.6 = 31979
0.7 = 35757
0.8 = 36704
0.9 = 41927
1.0 = 41375

dif avg
trade: -18514.93252201425
trans: -746.1249763132469 ~25x Trade
harshrate: 32.05882406901156

<hr>
Price-Trade Volume R
Pearson's r =      0.0056
<hr>
Price-Trans Volume R
Pearson's r =      0.057
<hr>
Price-HashRate R
Pearson's r =      0.233
