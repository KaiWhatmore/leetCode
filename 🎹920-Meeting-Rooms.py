class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda i: i.start)

        i = 1
        while i < len(intervals):
            beforeMeeting = intervals[i - 1]
            afterMeeting = intervals[i]

            if afterMeeting.start < beforeMeeting.end:
                return False

            i += 1

        return True
