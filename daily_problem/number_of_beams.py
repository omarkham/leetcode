class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        new_arr = []
        beams = 0

        for string in bank:
            beams = string.count("1")
            if beams > 0: new_arr.append(beams)

        print(new_arr)

        sum = 0

        for i in range(len(new_arr) - 1):
            print(i)
            print(sum)
            sum += new_arr[i] * new_arr[i + 1]

        return sum
