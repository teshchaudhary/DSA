class MyCalendarThree:
    def __init__(self):
        self.timeline = {}
        self.max_overlap = 0

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] = self.timeline.get(startTime, 0) + 1
        self.timeline[endTime] = self.timeline.get(endTime, 0) - 1

        overlap = 0
        for _, value in sorted(self.timeline.items()):
            overlap += value
            self.max_overlap = max(self.max_overlap, overlap)

        return self.max_overlap