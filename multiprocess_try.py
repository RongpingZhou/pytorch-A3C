# from multiprocessing import Pool

# def f(x):
#     return x*x

# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))

# from torch.multiprocessing import Process
# import os

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def f(name):
#     info('function f')
#     print('hello', name)

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()


import torch.multiprocessing as mp


class Worker(mp.Process):
    def __init__(self, res_queue, name):
        super(Worker, self).__init__()
        self.name = 'w%i' % name
        self.res_queue = res_queue

    def run(self):
        ABC = True
        total_step = 1
        while total_step < 2:
            if (ABC):
                self.res_queue.put("Hello")

            total_step += 1

        self.res_queue.put(None)


if __name__ == "__main__":
    res_queue = mp.Queue()

    print("1st place")

    # parallel training
    # workers = [Worker(gnet, opt, global_ep, global_ep_r, res_queue, i) for i in range(mp.cpu_count())]
    workers = [Worker(res_queue, i) for i in range(1)]
    # workers = [Worker(res_queue, i) for i in range(mp.cpu_count())]
    [w.start() for w in workers]
    print(f"{len(workers)}")
    print("2nd place")
    res = []                    # record episode reward to plot
    time = 0
    while True:
        if(time==0):
            print("3rd place")
        # print(f"process {w.name}")
        r = res_queue.get()
        print(f"r: {r}")
        if(time==0):
            print("4th place")
            time = time + 1
        if r is not None:
            res.append(r)
        else:
            break
    [w.join() for w in workers]
