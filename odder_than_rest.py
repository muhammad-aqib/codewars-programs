
def odd_one(arr):
    for i in arr:
        if i % 2 != 0:
            return arr.index(i)
    return -1

if __name__ == "__main__":
    print(odd_one([2,4,6,7,10]))