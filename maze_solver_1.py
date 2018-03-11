import time

grid = [[0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 2, 1],
        [0, 0, 0, 0, 0, 0, 0, 0]]#Bu matrisimiz bu matriste: 0 Yol ,1 Duvar ,2 Varış Noktamız

def search(x, y):
    #time.sleep(0.5)
    print("Hareket ediliyor...")
    if grid[x][y] == 2:# 2 Bizim Varış Noktamız.
        print("Ulastiniz tebrikler! [%d, %d]" % (x, y))
        return True
#    elif grid[x][y] == 0:
#        print("[%d, %d] konumuna gidiliyor..." % (x, y))
#        return False
    elif grid[x][y] == 1:
        print("[%d, %d] konumunda duvar var!" % (x, y))
        return False
    elif grid[x][y] == 3:
        print("[%d, %d] konumu daha once ziyaret edildi." % (x, y))
        return False
        
    grid[x][y] = 3
    
    if((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True
    return False

search(0, 0)