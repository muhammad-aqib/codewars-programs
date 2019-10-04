# Test.describe("Basic tests")
# Test.assert_equals(beggars([1,2,3,4,5],1),[15])
# Test.assert_equals(beggars([1,2,3,4,5],2),[9,6])
# Test.assert_equals(beggars([1,2,3,4,5],3),[5,7,3])
# Test.assert_equals(beggars([1,2,3,4,5],6),[1,2,3,4,5,0])
# Test.assert_equals(beggars([1,2,3,4,5],0),[])


def beggars(values, n):
    if len(values) == 0 or n == 0:
        return []
        
    final_list = []

    for i in range(n):
        final_list.append(0)

    count = 0

    for i in values:
        final_list[count] = final_list[count] + i
        count += 1
        if count >= len(final_list):
            count = 0
    return final_list


if __name__ == "__main__":
    print(beggars([1, 2, 3, 4, 5], 2))
