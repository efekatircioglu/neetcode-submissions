class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # new interval is completely before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # return early with the rest of intervals
                return res + intervals[i:]

            # new interval is completely after
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # merged intervals
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
