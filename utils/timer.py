import time


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        print(f'耗时:{int(time.time() - t1)}s')
        return res

    return wrapper

if __name__=='__main__':
    @timer
    def func():
        time.sleep(1)
        return 1


    print(func())
