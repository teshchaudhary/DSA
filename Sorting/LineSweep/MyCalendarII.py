class MyCalendarTwo:
    def __init__(self):
        self.check = dict()

    def book(self, startTime: int, endTime: int) -> bool:
        if startTime in self.check:
            self.check[startTime] += 1
        else:
            self.check[startTime] = 1
        
        if endTime in self.check:
            self.check[endTime] -= 1
        else:
            self.check[endTime] = -1

        sorted_check = sorted(self.check.items())

        overlap = 0
        for _, value in sorted_check:
            overlap += value
            if overlap > 2:
                self.check[startTime] -= 1
                if self.check[startTime] == 0:
                    del self.check[startTime]
                
                self.check[endTime] += 1
                if self.check[endTime] == 0:
                    del self.check[endTime]
                
                return False
        
        return True