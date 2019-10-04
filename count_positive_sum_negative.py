# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.


def count_positives_sum_negatives(arr):
    if arr == []
    return []
    output = [0, 0]
    for i in arr:
        if i > 0:
            output[0] += 1
        elif i < 0:
            output[1] = output[1]+(i)
    return output


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    print(count_positives_sum_negatives(array))
