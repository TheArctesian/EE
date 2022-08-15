from coalas import csvReader as c
datePriceDict = {
"2019-06-26":11766,
"2019-06-27":12933,
"2019-06-28":11133,
"2019-06-29":12374,
"2019-06-30":11890,
"2019-07-01":10738,
"2019-07-02":10579,
"2019-07-03":10805,
"2019-07-04":11985,
"2019-07-05":11160,
"2019-07-06":10955,
"2019-07-07":11232,
"2019-07-08":11477,
"2019-07-09":12313,
"2019-07-10":12587,
"2019-07-11":12100,
"2019-07-12":11353,
"2019-07-13":11804,
"2019-07-14":11389,
"2019-07-15":10187,
"2019-07-16":10874,
"2019-07-17":9398 ,
"2019-07-18":9674 ,
"2019-07-19":10639,
"2019-07-20":10536,
"2019-07-21":10765,
"2019-07-22":10587,
"2019-07-23":10324,
"2019-07-24":9844 ,
"2019-07-25":9772 ,
"2019-07-26":9875 ,
"2019-07-27":9849 ,
"2019-07-28":9474 ,
"2019-07-29":9530 ,
"2019-07-30":9501 ,
"2019-07-31":9589 ,
"2019-08-01":10085,
"2019-08-02":10407,
"2019-08-03":10530,
"2019-08-04":10815,
"2019-08-05":10980,
"2019-08-06":11788,
"2019-08-07":11466,
"2019-08-08":11961,
"2019-08-09":11996,
"2019-08-10":11857,
"2019-08-11":11282,
"2019-08-12":11567,
"2019-08-13":11386,
"2019-08-14":10858,
"2019-08-15":10017,
"2019-08-16":10302,
"2019-08-17":10359,
"2019-08-18":10215,
"2019-08-19":10318,
"2019-08-20":10917,
"2019-08-21":10761,
"2019-08-22":10129,
"2019-08-23":10112,
"2019-08-24":10406,
"2019-08-25":10144,
"2019-08-26":10135,
"2019-08-27":10360,
"2019-08-28":10172,
"2019-08-29":9718 ,
"2019-08-30":9485 ,
"2019-08-31":9578 ,
"2019-09-01":9601 ,
"2019-09-02":9770 ,
"2019-09-03":10387,
"2019-09-04":10621,
"2019-09-05":10584,
"2019-09-06":10578,
"2019-09-07":10317,
"2019-09-08":10487,
"2019-09-09":10406,
"2019-09-10":10314,
"2019-09-11":10101,
"2019-09-12":10159,
"2019-09-13":10420,
"2019-09-14":10364,
"2019-09-15":10361,
"2019-09-16":10310,
"2019-09-17":10266,
"2019-09-18":10190,
"2019-09-19":10158,
"2019-09-20":10276,
"2019-09-21":10173,
"2019-09-22":9979 ,
"2019-09-23":10033,
"2019-09-24":9683 ,
"2019-09-25":8554 ,
"2019-09-26":8432 ,
"2019-09-27":8056 ,
"2019-09-28":8194 ,
"2019-09-29":8225 ,
"2019-09-30":8057 ,
"2019-10-01":8308 ,
"2019-10-02":8323 ,
"2019-10-03":8382 ,
"2019-10-04":8236 ,
"2019-10-05":8155 ,
"2019-10-06":8148 ,
"2019-10-07":7870 ,
"2019-10-08":8212 ,
"2019-10-09":8190 ,
"2019-10-10":8588 ,
"2019-10-11":8587 ,
"2019-10-12":8270 ,
"2019-10-13":8308 ,
"2019-10-14":8284 ,
"2019-10-15":8354 ,
"2019-10-16":8162 ,
"2019-10-17":8003 ,
"2019-10-18":8077 ,
"2019-10-19":7954 ,
"2019-10-20":7960 ,
"2019-10-21":8231 ,
"2019-10-22":8223 ,
"2019-10-23":8027 ,
"2019-10-24":7470 ,
"2019-10-25":7432 ,
"2019-10-26":8667 ,
"2019-10-27":9260 ,
"2019-10-28":9552 ,
"2019-10-29":9219 ,
"2019-10-30":9433 ,
"2019-10-31":9165 ,
"2019-11-01":9148 ,
"2019-11-02":9253 ,
"2019-11-03":9301 ,
"2019-11-03":9206 ,
"2019-11-04":9418 ,
"2019-11-05":9310 ,
"2019-11-06":9343 ,
"2019-11-07":9204 ,
"2019-11-08":8766 ,
"2019-11-09":8809 ,
"2019-11-10":9037 ,
"2019-11-11":8718 ,
"2019-11-12":8802 ,
"2019-11-13":8762 ,
"2019-11-14":8632 ,
"2019-11-15":8458 ,
"2019-11-16":8483 ,
"2019-11-17":8504 ,
"2019-11-18":8176 ,
"2019-11-19":8121 ,
"2019-11-20":8082 ,
"2019-11-21":7617 ,
"2019-11-22":7286 ,
"2019-11-23":7324 ,
"2019-11-24":6907 ,
"2019-11-25":7130 ,
"2019-11-26":7164 ,
"2019-11-27":7524 ,
"2019-11-28":7431 ,
"2019-11-29":7757 ,
"2019-11-30":7558 ,
"2019-12-01":7403 ,
"2019-12-02":7310 ,
"2019-12-03":7297 ,
"2019-12-04":7193 ,
"2019-12-05":7396 ,
"2019-12-06":7547 ,
"2019-12-07":7505 ,
"2019-12-08":7522 ,
"2019-12-09":7337 ,
"2019-12-10":7221 ,
"2019-12-11":7202,
"2019-12-12":7189 ,
"2019-12-13":7252 ,
"2019-12-14":7068 ,
"2019-12-15":7111 ,
"2019-12-16":6880 ,
"2019-12-17":6612 ,
"2019-12-18":7284 ,
"2019-12-19":7151 ,
"2019-12-20":7190 ,
"2019-12-21":7143 ,
"2019-12-22":7514 ,
"2019-12-23":7322 ,
"2019-12-24":7251 ,
"2019-12-25":7193 ,
"2019-12-26":7194 ,
"2019-12-27":7244 ,
"2019-12-28":7301 ,
"2019-12-29":7385 ,
"2019-12-30":7220 ,
"2019-12-31":7168 ,
"2020-01-01":7176 ,
"2020-01-02":6944 ,
"2020-01-03":7326 ,
"2020-01-04":7348 ,
"2020-01-05":7352 ,
"2020-01-06":7759 ,
"2020-01-07":8165 ,
"2020-01-08":8043 ,
"2020-01-09":7818 ,
"2020-01-10":8185 ,
"2020-01-11":8021 ,
"2020-01-12":8174 ,
"2020-01-13":8105 ,
"2020-01-14":8842 ,
"2020-01-15":8814 ,
"2020-01-16":8722 ,
"2020-01-17":8900 ,
"2020-01-18":8911 ,
"2020-01-19":8703 ,
"2020-01-20":8626 ,
"2020-01-21":8722 ,
"2020-01-22":8659 ,
"2020-01-23":8388 ,
"2020-01-24":8428 ,
"2020-01-25":8327 ,
"2020-01-26":8588 ,
"2020-01-27":8896 ,
"2020-01-28":9386 ,
"2020-01-29":9280 ,
"2020-01-30":9502 ,
"2020-01-31":9334 ,
"2020-02-01":9378 ,
"2020-02-02":9315 ,
"2020-02-03":9285 ,
"2020-02-04":9162 ,
"2020-02-05":9615 ,
"2020-02-06":9756 ,
"2020-02-07":9808 ,
"2020-02-08":9907 ,
"2020-02-09":10162,
"2020-02-10":9855 ,
"2020-02-11":10275,
"2020-02-12":10354,
"2020-02-13":10242,
"2020-02-14":10369,
"2020-02-15":9904 ,
"2020-02-16":9938 ,
"2020-02-17":9704 ,
"2020-02-18":10181,
"2020-02-19":9605 ,
"2020-02-20":9607 ,
"2020-02-21":9697 ,
"2020-02-22":9670 ,
"2020-02-23":9989 ,
"2020-02-24":9664 ,
"2020-02-25":9309 ,
"2020-02-26":8786 ,
"2020-02-27":8805 ,
"2020-02-28":8712 ,
"2020-02-29":8531 ,
"2020-03-01":8534 ,
"2020-03-02":8913 ,
"2020-03-03":8754 ,
"2020-03-04":8759 ,
"2020-03-05":9067 ,
"2020-03-06":9156 ,
"2020-03-07":8899 ,
"2020-03-09":8039 ,
"2020-03-10":7932 ,
"2020-03-11":7885 ,
"2020-03-12":7937 ,
"2020-03-13":4830 ,
"2020-03-14":5609 ,
"2020-03-15":5166 ,
"2020-03-16":5348 ,
"2020-03-17":5026 ,
"2020-03-18":5358 ,
"2020-03-19":5410 ,
"2020-03-20":6195 ,
"2020-03-21":6226 ,
"2020-03-22":6190 ,
"2020-03-23":5823 ,
"2020-03-24":6502 ,
"2020-03-25":6768 ,
"2020-03-26":6698 ,
"2020-03-27":6764 ,
"2020-03-28":6369 ,
"2020-03-29":6261 ,
"2020-03-30":5885 ,
"2020-03-31":6405 ,
"2020-04-01":6428 ,
"2020-04-02":6653 ,
"2020-04-03":6809 ,
"2020-04-04":6742 ,
"2020-04-05":6872 ,
"2020-04-06":6777 ,
"2020-04-07":7343 ,
"2020-04-08":7206 ,
"2020-04-09":7365 ,
"2020-04-10":7294 ,
"2020-04-11":6873 ,
"2020-04-12":6892 ,
"2020-04-13":6915 ,
"2020-04-14":6858 ,
"2020-04-15":6872 ,
"2020-04-16":6624 ,
"2020-04-17":7112 ,
"2020-04-18":7035 ,
"2020-04-19":7259 ,
"2020-04-20":7130 ,
"2020-04-21":6840 ,
"2020-04-22":6853 ,
"2020-04-23":7131 ,
"2020-04-24":7478 ,
"2020-04-25":7507 ,
"2020-04-26":7550 ,
"2020-04-27":7699 ,
"2020-04-28":7791 ,
"2020-04-29":7765 ,
"2020-04-30":8778 ,
"2020-05-01":8629 ,
"2020-05-02":8825 ,
"2020-05-03":8974 ,
"2020-05-04":8904 ,
"2020-05-05":8886 ,
"2020-05-06":9031 ,
"2020-05-07":9171 ,
"2020-05-08":10002,
"2020-05-09":9822 ,
"2020-05-10":9527 ,
"2020-05-11":8754 ,
"2020-05-12":8617 ,
"2020-05-13":8815 ,
"2020-05-14":9306 ,
"2020-05-15":9790 ,
"2020-05-16":9304 ,
"2020-05-17":9386 ,
"2020-05-18":9669 ,
"2020-05-19":9719 ,
"2020-05-20":9786 ,
"2020-05-21":9511 ,
"2020-05-22":9058 ,
"2020-05-23":9167 ,
"2020-05-24":9178 ,
"2020-05-25":8731 ,
"2020-05-26":8900 ,
"2020-05-27":8843 ,
"2020-05-28":9198 ,
"2020-05-29":9569 ,
"2020-05-30":9426 ,
"2020-05-31":9698 ,
"2020-06-01":9451 ,
"2020-06-02":10204,
"2020-06-03":9526 ,
"2020-06-04":9658 ,
"2020-06-05":9795 ,
"2020-06-06":9624 ,
"2020-06-07":9670 ,
"2020-06-08":9754 ,
"2020-06-09":9783 ,
"2020-06-10":9775 ,
"2020-06-11":9892 ,
"2020-06-12":9286 ,
"2020-06-13":9460 ,
"2020-06-14":9474 ,
"2020-06-15":9330 ,
"2020-06-16":9427 ,
"2020-06-17":9526 ,
"2020-06-18":9455 ,
"2020-06-19":9380 ,
"2020-06-20":9300 ,
"2020-06-21":9357 ,
"2020-06-22":9285 ,
"2020-06-23":9692 ,
"2020-06-24":9621 ,
"2020-06-25":9277 ,
"2020-06-26":9241 ,
"2020-06-27":9154 ,
"2020-06-28":9004 ,
"2020-06-29":9127 ,
"2020-06-30":9185 ,
"2020-07-01":9134 ,
"2020-07-02":9236 ,
"2020-07-03":9088 ,
"2020-07-04":9072 ,
"2020-07-05":9131 ,
"2020-07-06":9089 ,
"2020-07-07":9349 ,
"2020-07-08":9256 ,
"2020-07-09":9440 ,
"2020-07-10":9238 ,
"2020-07-11":9287 ,
"2020-07-12":9236 ,
"2020-07-13":9296 ,
"2020-07-14":9238 ,
"2020-07-15":9255 ,
"2020-07-16":9194 ,
"2020-07-17":9131 ,
"2020-07-18":9154 ,
"2020-07-19":9175 ,
"2020-07-20":9215 ,
"2020-07-21":9164 ,
"2020-07-22":9393 ,
"2020-07-23":9537 ,
"2020-07-24":9613 ,
"2020-07-25":9551 ,
"2020-07-26":9708 ,
"2020-07-27":9939 ,
"2020-07-28":11042,
"2020-07-29":10935,
"2020-07-30":11103,
"2020-07-31":11115,
"2020-08-01":11344,
"2020-08-02":11824,
"2020-08-03":11078,
"2020-08-04":11243,
"2020-08-05":11194,
"2020-08-06":11750,
"2020-08-07":11773,
"2020-08-08":11606,
"2020-08-09":11768,
"2020-08-10":11684,
"2020-08-11":11893,
"2020-08-12":11392,
"2020-08-13":11573,
"2020-08-14":11777,
"2020-08-15":11774,
"2020-08-16":11874,
"2020-08-17":11914,
"2020-08-18":12294,
"2020-08-19":11970,
"2020-08-20":11734,
"2020-08-21":11866,
"2020-08-22":11523,
"2020-08-23":11683,
"2020-08-24":11653,
"2020-08-25":11764,
"2020-08-26":11337,
"2020-08-27":11467,
"2020-08-28":11302,
"2020-08-29":11535,
"2020-08-30":11482,
"2020-08-31":11708,
"2020-09-01":11660,
"2020-09-02":11923,
"2020-09-03":11397,
"2020-09-04":10188,
"2020-09-05":10468,
"2020-09-06":10160,
"2020-09-07":10255,
"2020-09-08":10368,
"2020-09-09":10122,
"2020-09-10":10228,
"2020-09-11":10353,
"2020-09-12":10395,
"2020-09-13":10446,
"2020-09-14":10331,
"2020-09-15":10675,
"2020-09-16":10786,
"2020-09-17":10948,
"2020-09-18":10944,
"2020-09-19":10932,
"2020-09-20":11081,
"2020-09-21":10920,
"2020-09-22":10430,
"2020-09-23":10532,
"2020-09-24":10234,
"2020-09-25":10732,
"2020-09-26":10693,
"2020-09-27":10732,
"2020-09-28":10774,
"2020-09-29":10692,
"2020-09-30":10841,
"2020-10-01":10778,
"2020-10-02":10619,
"2020-10-03":10575,
"2020-10-04":10552,
"2020-10-05":10673,
"2020-10-06":10789,
"2020-10-07":10604,
"2020-10-08":10671,
"2020-10-09":10923,
"2020-10-10":11063,
"2020-10-11":11303,
"2020-10-12":11377,
"2020-10-13":11540,
"2020-10-14":11428,
"2020-10-15":11431,
"2020-10-16":11504,
"2020-10-17":11328,
"2020-10-18":11367,
"2020-10-19":11508,
"2020-10-20":11758,
"2020-10-21":11925,
"2020-10-22":12832,
"2020-10-23":12990,
"2020-10-24":12945,
"2020-10-25":13128,
"2020-10-26":13037,
"2020-10-27":13076,
"2020-10-28":13651,
"2020-10-29":13289,
"2020-10-30":13459,
"2020-10-31":13565,
"2020-11-01":13810,
"2020-11-01":13759,
"2020-11-02":13575,
"2020-11-03":14023,
"2020-11-04":14156,
"2020-11-05":15591,
"2020-11-06":15596,
"2020-11-07":14840,
"2020-11-08":15491,
"2020-11-09":15329,
"2020-11-10":15317,
"2020-11-11":15709,
"2020-11-12":16296,
"2020-11-13":16339,
"2020-11-14":16091,
"2020-11-15":15968,
"2020-11-16":16725,
"2020-11-17":17680,
"2020-11-18":17798,
"2020-11-19":17821,
"2020-11-20":18687,
"2020-11-21":18700,
"2020-11-22":18422,
"2020-11-23":18399,
"2020-11-24":19173,
"2020-11-25":18740,
"2020-11-26":17151,
"2020-11-27":17139,
"2020-11-28":17732,
"2020-11-29":18192,
"2020-11-30":19710,
"2020-12-01":18793,
"2020-12-02":19227,
"2020-12-03":19455,
"2020-12-04":18670,
"2020-12-05":19155,
"2020-12-06":19378,
"2020-12-07":19181,
"2020-12-08":18319,
"2020-12-09":18554,
"2020-12-10":18248,
"2020-12-11":18029,
"2020-12-12":18803,
"2020-12-13":19164,
"2020-12-14":19277,
"2020-12-15":19440,
"2020-12-16":21379,
"2020-12-17":22847,
"2020-12-18":23151,
"2020-12-19":23870,
"2020-12-20":23491,
"2020-12-21":22745,
"2020-12-22":23825,
"2020-12-23":23253,
"2020-12-24":23716,
"2020-12-25":24694,
"2020-12-26":26443,
"2020-12-27":26247,
"2020-12-28":27037,
"2020-12-29":27376,
"2020-12-30":28857,
"2020-12-31":28983,
"2021-01-01":29394,
"2021-01-02":32195,
"2021-01-03":33001,
"2021-01-04":32035,
"2021-01-05":34047,
"2021-01-06":36860,
"2021-01-07":39486,
"2021-01-08":40670,
"2021-01-09":40241,
"2021-01-10":38240,
"2021-01-11":35545,
"2021-01-12":34012,
"2021-01-13":37393,
"2021-01-14":39158,
"2021-01-15":36829,
"2021-01-16":36065,
"2021-01-17":35793,
"2021-01-18":36632,
"2021-01-19":36020,
"2021-01-20":35539,
"2021-01-21":30798,
"2021-01-22":33002,
"2021-01-23":32100,
"2021-01-24":32277,
"2021-01-25":32243,
"2021-01-26":32542,
"2021-01-27":30419,
"2021-01-28":33403,
"2021-01-29":34314,
"2021-01-30":34318,
"2021-01-31":33136,
"2021-02-01":33523,
"2021-02-02":35530,
"2021-02-03":37676,
"2021-02-04":37002,
"2021-02-05":38279,
"2021-02-06":39323,
"2021-02-07":38928,
"2021-02-08":46364,
"2021-02-09":46590,
"2021-02-10":44878,
"2021-02-11":48013,
"2021-02-12":47471,
"2021-02-13":47185,
"2021-02-14":48720,
"2021-02-15":47952,
"2021-02-16":49160,
"2021-02-17":52118,
"2021-02-18":51608,
"2021-02-19":55917,
"2021-02-20":56001,
"2021-02-21":57488,
"2021-02-22":54123,
"2021-02-23":48880,
"2021-02-24":50625,
"2021-02-25":46800,
"2021-02-26":46340,
"2021-02-27":46156,
"2021-02-28":45114,
"2021-03-01":49618,
"2021-03-02":48356,
"2021-03-03":50478,
"2021-03-04":48449,
"2021-03-05":48861,
"2021-03-06":48882,
"2021-03-07":51170,
"2021-03-08":52299,
"2021-03-09":54882,
"2021-03-10":55997,
"2021-03-11":57764,
"2021-03-12":57253,
"2021-03-13":61259,
"2021-03-15":59133,
"2021-03-16":55755,
"2021-03-17":56872,
"2021-03-18":58913,
"2021-03-19":57666,
"2021-03-20":58075,
"2021-03-21":58086,
"2021-03-22":57411,
"2021-03-23":54205,
"2021-03-24":54477,
"2021-03-25":52508,
"2021-03-26":51416,
"2021-03-27":55074,
"2021-03-28":55864,
"2021-03-29":55784,
"2021-03-30":57628,
"2021-03-31":58730,
"2021-04-01":58735,
"2021-04-02":58737,
"2021-04-03":59031,
"2021-04-04":57076,
"2021-04-05":58207,
"2021-04-06":59054,
"2021-04-07":58020,
"2021-04-08":55947,
"2021-04-09":58049,
"2021-04-10":58103,
"2021-04-11":59774,
"2021-04-12":59965,
"2021-04-13":59835,
"2021-04-14":63554,
"2021-04-15":62969,
"2021-04-16":63253,
"2021-04-17":61456,
"2021-04-18":60087,
"2021-04-19":56251,
"2021-04-20":55703,
"2021-04-21":56508,
"2021-04-22":53809,
"2021-04-23":51732,
"2021-04-24":51153,
"2021-04-25":50111,
"2021-04-26":49076,
"2021-04-27":54057,
"2021-04-28":55071,
"2021-04-29":54884,
"2021-04-30":53584,
"2021-05-01":57797,
"2021-05-02":57858,
"2021-05-03":56610,
"2021-05-04":57213,
"2021-05-05":53242,
"2021-05-06":57473,
"2021-05-07":56428,
"2021-05-08":57380,
"2021-05-09":58929,
"2021-05-10":58281,
"2021-05-11":55884,
"2021-05-12":56750,
"2021-05-13":49007,
"2021-05-14":49702,
"2021-05-15":49923,
"2021-05-16":46737,
"2021-05-17":46442,
"2021-05-18":43596,
"2021-05-19":42912,
"2021-05-20":36964,
"2021-05-21":40784,
"2021-05-22":37280,
"2021-05-23":37528,
"2021-05-24":34755,
"2021-05-25":38729,
"2021-05-26":38411,
"2021-05-27":39266,
"2021-05-28":38445,
"2021-05-29":35690,
"2021-05-30":34648,
"2021-05-31":35685,
"2021-06-01":37311,
"2021-06-02":36663,
"2021-06-03":37585,
"2021-06-04":39189,
"2021-06-05":36886,
"2021-06-06":35530,
"2021-06-07":35816,
"2021-06-08":33515,
"2021-06-09":33450,
"2021-06-10":37338,
"2021-06-11":36705,
"2021-06-12":37313,
"2021-06-13":35495,
"2021-06-14":39067,
"2021-06-15":40526,
"2021-06-16":40189,
"2021-06-17":38325,
"2021-06-18":38068,
"2021-06-19":35730,
"2021-06-20":35524,
"2021-06-21":35592,
"2021-06-22":31687,
"2021-06-23":32448,
"2021-06-24":33675,
"2021-06-25":34639,
"2021-06-26":31641,
"2021-06-27":32161,
"2021-06-28":34644,
"2021-06-29":34457,
"2021-06-30":35848,
"2021-07-01":35047,
"2021-07-02":33537,
"2021-07-03":33857,
"2021-07-04":34689,
"2021-07-05":35309,
"2021-07-06":33748,
"2021-07-07":34211,
"2021-07-08":33839,
"2021-07-09":32877,
"2021-07-10":33819,
"2021-07-11":33516,
"2021-07-12":34228,
"2021-07-13":33158,
"2021-07-14":32687,
"2021-07-15":32815,
"2021-07-16":31739,
"2021-07-17":31421,
"2021-07-18":31521,
"2021-07-19":31783,
"2021-07-20":30816,
"2021-07-21":29790,
"2021-07-22":32118,
"2021-07-23":32298,
"2021-07-24":33582,
"2021-07-25":34279,
"2021-07-26":35365,
"2021-07-27":37318,
"2021-07-28":39406,
"2021-07-29":40003,
"2021-07-30":40006,
"2021-07-31":42214,
"2021-08-01":41659,
"2021-08-02":40000,
"2021-08-03":39194,
"2021-08-04":38138,
"2021-08-05":39750,
"2021-08-06":40882,
"2021-08-07":42826,
"2021-08-08":44634,
"2021-08-09":43816,
"2021-08-10":46333,
"2021-08-11":45608,
"2021-08-12":45611,
"2021-08-13":44418,
"2021-08-14":47834,
"2021-08-15":47112,
"2021-08-16":47056,
"2021-08-17":45983,
"2021-08-18":44649,
"2021-08-19":44778,
"2021-08-20":46735,
"2021-08-21":49328,
"2021-08-22":48932,
"2021-08-23":49336,
"2021-08-24":49524,
"2021-08-25":47745,
"2021-08-26":48972,
"2021-08-27":46963,
"2021-08-28":49057,
"2021-08-29":48898,
"2021-08-30":48807,
"2021-08-31":47075,
"2021-09-01":47156,
"2021-09-02":48863,
"2021-09-03":49329,
"2021-09-04":50035,
"2021-09-05":49947,
"2021-09-06":51769,
"2021-09-07":52677,
"2021-09-08":46809,
"2021-09-09":46078,
"2021-09-10":46369,
"2021-09-11":44847,
"2021-09-12":45145,
"2021-09-13":46059,
"2021-09-14":44969,
"2021-09-15":47072,
"2021-09-16":48168,
"2021-09-17":47785,
"2021-09-18":47264,
"2021-09-19":48259,
"2021-09-20":47249,
"2021-09-21":42902,
"2021-09-22":40619,
"2021-09-23":43605,
"2021-09-24":44889,
"2021-09-25":42816,
"2021-09-26":42742,
"2021-09-27":43183,
"2021-09-28":42238,
"2021-09-29":41011,
"2021-09-30":41522,
"2021-10-01":43758,
"2021-10-02":48140,
"2021-10-03":47727,
"2021-10-04":48206,
"2021-10-05":49144,
"2021-10-06":51506,
"2021-10-07":55344,
"2021-10-08":53801,
"2021-10-09":53867,
"2021-10-10":55123,
"2021-10-11":54626,
"2021-10-12":57452,
"2021-10-13":56243,
"2021-10-14":57407,
"2021-10-15":57398,
"2021-10-16":61641,
"2021-10-17":60949,
"2021-10-18":61546,
"2021-10-19":61972,
"2021-10-20":64288,
"2021-10-21":66064,
"2021-10-22":62355,
"2021-10-23":60697,
"2021-10-24":61277,
"2021-10-25":60884,
"2021-10-26":63071,
"2021-10-27":60345,
"2021-10-28":58538,
"2021-10-29":60587,
"2021-10-30":62249,
"2021-10-31":61731,
"2021-11-01":61373,
"2021-11-02":61030,
"2021-11-03":63241,
"2021-11-04":62955,
"2021-11-05":61442,
"2021-11-06":61072,
"2021-11-07":61516,
"2021-11-07":63293,
"2021-11-08":67562,
"2021-11-09":66954,
"2021-11-10":64977,
"2021-11-11":64839,
"2021-11-12":64255,
"2021-11-13":64421,
"2021-11-14":65469,
"2021-11-15":63584,
"2021-11-16":60172,
"2021-11-17":60381,
"2021-11-18":56921,
"2021-11-19":58133,
"2021-11-20":59778,
"2021-11-21":58756,
"2021-11-22":56302,
"2021-11-23":57578,
"2021-11-24":57188,
"2021-11-25":58935,
"2021-11-26":53588,
"2021-11-27":54801,
"2021-11-28":57292,
"2021-11-29":57828,
"2021-11-30":57026,
"2021-12-01":57230,
"2021-12-02":56508,
"2021-12-03":53714,
"2021-12-04":49254,
"2021-12-05":49380,
"2021-12-06":50565,
"2021-12-07":50645,
"2021-12-08":50511,
"2021-12-09":47660,
"2021-12-10":47137,
"2021-12-11":49380,
"2021-12-12":50117,
"2021-12-13":46757,
"2021-12-14":48393,
"2021-12-15":48885,
"2021-12-16":47658,
"2021-12-17":46174,
"2021-12-18":46864,
"2021-12-19":46689,
"2021-12-20":46910,
"2021-12-21":48935,
"2021-12-22":48628,
"2021-12-23":50786,
"2021-12-24":50815,
"2021-12-25":50471,
"2021-12-26":50801,
"2021-12-27":50692,
"2021-12-28":47601,
"2021-12-29":46409,
"2021-12-30":47133,
"2021-12-31":46250,
"2022-01-01":47763,
"2022-01-02":47328,
"2022-01-03":46442,
"2022-01-04":45863,
"2022-01-05":43436,
"2022-01-06":43121,
"2022-01-07":41528,
"2022-01-08":41691,
"2022-01-09":41864,
"2022-01-10":41849,
"2022-01-11":42723,
"2022-01-12":43926,
"2022-01-13":42546,
"2022-01-14":43099,
"2022-01-15":43147,
"2022-01-16":43102,
"2022-01-17":42248,
"2022-01-18":42381,
"2022-01-19":41708,
"2022-01-20":40684,
"2022-01-21":36481,
"2022-01-22":35071,
"2022-01-23":36281,
"2022-01-24":36679,
"2022-01-25":36949,
"2022-01-26":36824,
"2022-01-27":37147,
"2022-01-28":37770,
"2022-01-29":38186,
"2022-01-30":37919,
"2022-01-31":38522,
"2022-02-01":38740,
"2022-02-02":36913,
"2022-02-03":37092,
"2022-02-04":41584,
"2022-02-05":41435,
"2022-02-06":42451,
"2022-02-07":43834,
"2022-02-08":44133,
"2022-02-09":44397,
"2022-02-10":43531,
"2022-02-11":42401,
"2022-02-12":42246,
"2022-02-13":42105,
"2022-02-14":42581,
"2022-02-15":44536,
"2022-02-16":43949,
"2022-02-17":40566,
"2022-02-18":40015,
"2022-02-19":40115,
"2022-02-20":38382,
"2022-02-21":37031,
"2022-02-22":38262,
"2022-02-23":37291,
"2022-02-24":38345,
"2022-02-25":39223,
"2022-02-26":39104,
"2022-02-27":37705,
"2022-02-28":43226,
"2022-03-01":44419,
"2022-03-02":43935,
"2022-03-03":42464,
"2022-03-04":39141,
"2022-03-05":39400,
"2022-03-06":38408,
"2022-03-07":38033,
"2022-03-08":38753,
"2022-03-09":41957,
"2022-03-10":39438,
"2022-03-11":38741,
"2022-03-12":38809,
"2022-03-14":37820,
"2022-03-15":39681,
"2022-03-16":39321,
"2022-03-17":41133,
"2022-03-18":40947,
"2022-03-19":41796,
"2022-03-20":42222,
"2022-03-21":41251,
"2022-03-22":41071,
"2022-03-23":42373,
"2022-03-24":42905,
"2022-03-25":44004,
"2022-03-26":44334,
"2022-03-27":44542,
"2022-03-28":46859,
"2022-03-29":47116,
"2022-03-30":47448,
"2022-03-31":47064,
"2022-04-01":45539,
"2022-04-02":46283,
"2022-04-03":45825,
"2022-04-04":46426,
"2022-04-05":46611,
"2022-04-06":45508,
"2022-04-07":43190,
"2022-04-08":43464,
"2022-04-09":42279,
"2022-04-10":42788,
"2022-04-11":42144,
"2022-04-12":39489,
"2022-04-13":40102,
"2022-04-14":41148,
"2022-04-15":39940,
"2022-04-16":40566,
"2022-04-17":40389,
"2022-04-18":39711,
"2022-04-19":40806,
"2022-04-20":41507,
"2022-04-21":41376,
"2022-04-22":40514,
"2022-04-23":39728,
"2022-04-24":39429,
"2022-04-25":39466,
"2022-04-26":40473,
"2022-04-27":38115,
"2022-04-28":39249,
"2022-04-29":39770,
"2022-04-30":38596,
"2022-05-01":37661,
"2022-05-02":38475,
"2022-05-03":38511,
"2022-05-04":37727,
"2022-05-05":39675,
"2022-05-06":36550,
"2022-05-07":36013,
"2022-05-08":35471,
"2022-05-09":34082,
"2022-05-10":30176,
"2022-05-11":31004,
"2022-05-12":28907,
"2022-05-13":28931,
"2022-05-14":29234,
"2022-05-15":30075,
"2022-05-16":31277,
"2022-05-17":29834,
"2022-05-18":30407,
"2022-05-19":28681,
"2022-05-20":30290,
"2022-05-21":29160,
"2022-05-22":29410,
"2022-05-23":30279,
"2022-05-24":29074,
"2022-05-25":29635,
"2022-05-26":29519,
"2022-05-27":29194,
"2022-05-28":28579,
"2022-05-29":29014,
"2022-05-30":29449,
"2022-05-31":31716,
"2022-06-01":31776,
"2022-06-02":29781,
"2022-06-03":30430,
"2022-06-04":29682,
"2022-06-05":29845,
"2022-06-06":29901,
"2022-06-07":31350,
"2022-06-08":31118,
"2022-06-09":30189,
"2022-06-10":30083,
"2022-06-11":29059,
"2022-06-12":28345,
"2022-06-13":26593,
"2022-06-14":22431,
"2022-06-15":22189,
"2022-06-16":22551,
"2022-06-17":20350,
"2022-06-18":20435,
"2022-06-19":18978,
"2022-06-20":20540,
"2022-06-21":20582,
"2022-06-22":20704,
"2022-06-23":19954,
}

c.importData('news.csv')
c.printHeaders()
for x in range(len(c.date)):
    p = datePriceDict[c.date[x]]
    c.price[x] = p
c.writeCSV("new.csv")