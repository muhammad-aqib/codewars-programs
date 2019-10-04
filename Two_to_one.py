# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,
# each taken only once - coming from s1 or s2.


def longest(s1, s2):
    joint = s1+s2
    unsorted = list(set(joint))
    sort_unique_list = sorted(unsorted)
    final = "".join(sort_unique_list)
    return final


if __name__ == "__main__":
    print(longest("ashdgajhksd", "ahjsdjhasd"))
