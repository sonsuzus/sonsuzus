d = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
for d[0] in range(1,16):
    for d[1] in range(1,16):
        for d[2] in range(1, 16):
            for d[3] in range(1, 16):
                for d[4] in range(1, 16):
                    d[5],d[6],d[7],d[8]=abs(d[0]-d[1]),abs(d[2] - d[1]),abs(d[3] - d[2]),abs(d[3] - d[4])
                    d[9],d[10],d[11] = abs(d[6] - d[5]),abs(d[7] - d[6]),abs(d[8] - d[7])
                    d[12],d[13] = abs(d[10] - d[9]),abs(d[10] - d[11])
                    d[14] = abs(d[13] - d[12])
                    #cd = d.copy()
                    kume = set(d)
                    if len(kume)==15:
                        print(d[0:5])
                        print(d[5:9])
                        print(d[9:12])
                        print(d[12:14])
                        print(d[14])