# Test.assert_equals(likes([]), 'no one likes this')
# Test.assert_equals(likes(['Peter']), 'Peter likes this')
# Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
# Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
# Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')


def likes(names):
    empty_str = ""
    if names == []:
        return "no one likes this"
    if len(names) == 1:
        return names[0] + " likes this"
    if len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    if len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    if len(names) >= 4:
        empty_str = ", ".join(names[:2])
        empty_str = empty_str + " and " + str(len(names) - 2) + " others like this"
    else:
        empty_str = ", ".join(names) + " like this"
    return empty_str


if __name__ == "__main__":
    print(likes(["Alex", "Jacob", "Mark", "Max"]))

