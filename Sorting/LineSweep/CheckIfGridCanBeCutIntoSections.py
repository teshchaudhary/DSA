"""
You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

Each of the three resulting sections formed by the cuts contains at least one rectangle.
Every rectangle belongs to exactly one section.
Return true if such cuts can be made; otherwise, return false.

"""

# Idea is line sweep algorithm

class Solution:
    def countLineIntersections(self, coordinates):
        overlap = 0
        lines = 0
        
        for _, event in coordinates:
            if event == -1:  # End of an interval
                overlap -= 1
            else:  # Start of an interval
                overlap += 1
            
            if overlap == 0:  # A valid cut
                lines += 1

        return lines >= 3  # Check if at least 3 sections are possible

    def checkValidCuts(self, n: int, rectangles):
        x_coordinates, y_coordinates = [], []

        for rect in rectangles:
            x_coordinates.append((rect[0], 1))  # Start of x-interval
            x_coordinates.append((rect[2], -1))  # End of x-interval
            y_coordinates.append((rect[1], 1))  # Start of y-interval
            y_coordinates.append((rect[3], -1))  # End of y-interval

        # Sorting coordinates (Primary: position, Secondary: event type)
        x_coordinates.sort()
        y_coordinates.sort()

        # Apply line sweep on both x and y coordinates
        return self.countLineIntersections(x_coordinates) or self.countLineIntersections(y_coordinates)
