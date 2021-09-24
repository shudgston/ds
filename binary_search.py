import unittest


def bin_search(arr, x, left, right):
    if left > right:
        return False

    mid = (left + right) // 2

    if arr[mid] == x:
        return True
    elif x < arr[mid]:
        return bin_search(arr, x, left, mid - 1)
    else:
        return bin_search(arr, x, mid + 1, right)


class TestBinSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [1, 2, 3, 4, 5, 6, 7, 8,9, 10]

    def test_found(self):
        bin_search(self.values, x=5, left=0, right=len(self.values) - 1)
        bin_search(self.values, x=1, left=0, right=len(self.values) - 1)
        bin_search(self.values, x=8, left=0, right=len(self.values) - 1)

    def test_not_found(self):
        bin_search(self.values, x=-999, left=0, right=len(self.values) - 1)
        bin_search(self.values, x=999, left=0, right=len(self.values) - 1)


if __name__ == '__main__':
    unittest.main()