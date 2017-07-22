# coding=utf-8

from multiprocessing.pool import ThreadPool


def worker(name, **kwargs):
    print "do sth, func: {}, kwargs: {}".format(name, kwargs)
    # TODO: analysis `raise Exception` result
    # raise Exception("worker exited...")


def main():
    # the processes set the process count for this pool.
    # default is the cpu num.
    # TODO: How about the thread stdout\stderr? what will happen? why?
    pool = ThreadPool(processes=3)

    # like built-in map, worker will yield the iterator.
    # TODO: chunksize?
    # TODO: callback?
    # pool.map(worker, [("test_worker_{}".format(x), ) for x in range(100)])

    # apply_async task
    # name = "test_worker"
    # pool.apply_async(worker, args=(name, ), kwds={}, callback=None)

    # map async
    pool.map_async(
        worker,
        [("test_worker_{}".format(x), ) for x in range(100)]
    )

    # TODO: what happened?
    # _worker_handler\_task_handler\_result_handler?
    # the pool class?
    # the _multiprocessing C lib?
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
