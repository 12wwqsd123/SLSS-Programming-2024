for x in range(1,100):
    for y in range(1,100):
        for m in range(1,100):
            for n in range(1,100):
                if x*y==m*n and x+y==m-n:
                    print(x*y)
                    

