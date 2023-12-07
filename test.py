from multiprocessing import Process
import time

def f(name):
    print(name)
    time.sleep(1)
    print('hello', name)

def test(bb,aa):
    sol = 0
    # print(bb)
    # print(aa)
    for a in aa:
        sol+= bb[a]

    return sol


if __name__ == '__main__':
    a = [1,2,3]
    b = {1:1,2:1,3:1}
    # for i in range(10):
    #     p = Process(target=f, args=(i,))
    #     p.start()
    from multiprocessing import Pool
    from functools import partial

    with Pool(8) as p:
        b = p.map(partial(test,b),[[1],[2],[3]])
    
    print(b)
    print(min([1,2,3,4]))

    import re

    print(list(re.findall('\d+','234 34 2   3 ')))