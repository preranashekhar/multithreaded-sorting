import random
import time
import threading


def merge_sort(input_array, result):
    print("{} is sorting {} numbers".format(threading.current_thread().getName(), len(input_array)))
    result.append(merge_sort_helper(input_array))


def merge_sort_helper(input_array):
    time.sleep(0.001)
    if len(input_array) > 1:
        mid = len(input_array) // 2
        left_arr = input_array[:mid]
        right_arr = input_array[mid:]

        return merge_sorted_arrays(
            merge_sort_helper(left_arr),
            merge_sort_helper(right_arr)
        )
    return input_array


def merge_sorted_arrays(left_arr, right_arr, result=[]):
    i, j = 0, 0
    merge_arr = []

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merge_arr.append(left_arr[i])
            i = i + 1
        else:
            merge_arr.append(right_arr[j])
            j = j + 1

    merge_arr += left_arr[i:] or right_arr[j:]
    result.append(merge_arr)
    return merge_arr


def single_threaded_merge_sort(data):
    print("Sorting for {} numbers".format(len(data)))
    start = time.time()
    result = []
    merge_sort(data, result)
    end = time.time()
    print("Time to execute {} secs ".format(end - start))
    print("Sorted array: ", result[0])
    print("===================================")


def multi_threaded_merge_sort(data):
    # threaded merge sort
    print("Sorting for {} numbers".format(len(data)))
    mid = len(data) // 2
    result = []
    start = time.time()
    sorting_thread_1 = threading.Thread(name="sorting_thread_1",
                                        target=merge_sort,
                                        args=(data[:mid], result,))
    sorting_thread_2 = threading.Thread(name="sorting_thread_2",
                                        target=merge_sort,
                                        args=(data[mid:], result,))

    sorting_thread_1.start()
    sorting_thread_2.start()

    # print("Active thread count after starting sorting threads:", threading.active_count())

    # wait until both sorting threads are complete
    sorting_thread_1.join()
    sorting_thread_2.join()

    final_sorted_array = []
    merging_thread = threading.Thread(name="merging_thread",
                                      target=merge_sorted_arrays,
                                      args=(result[0], result[1], final_sorted_array,))
    merging_thread.start()

    end = time.time()
    merging_thread.join()

    print("Time to execute {} secs ".format(end - start))
    print("Sorted array: ", final_sorted_array[0])
    print("===================================")


if __name__ == "__main__":
    arr_length = 1000
    data_set = [random.randint(0, 50000) for _ in range(arr_length)]

    print("Input array: ", data_set)
    single_threaded_merge_sort(data_set)
    multi_threaded_merge_sort(data_set)






