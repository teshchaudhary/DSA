class PascalTriangle:
    
    # Calculate nCr using integer arithmetic
    def nCr(self, n, r):
        if r > n:
            return 0
        res = 1
        for i in range(1, r + 1):
            res = res * (n - r + i) // i
        return res

    # Get element at position (n, r)
    def get_element(self, n, r):
        return self.nCr(n, r)

    # Get the nth row (0-based)
    def get_nth_row(self, n):
        row = []
        val = 1
        for r in range(n + 1):
            row.append(val)
            val = val * (n - r) // (r + 1)
        return row

    # Get the rth column (0-based), up to total_rows
    def get_rth_column(self, r, total_rows):
        col = []
        for n in range(r, total_rows):
            col.append(self.get_element(n, r))
        return col

    # Print the nth row
    def print_row(self, n):
        print(f"Row {n}:", self.get_nth_row(n))

    # Print Pascal's Triangle up to n rows
    def print_triangle(self, n):
        for i in range(n):
            row = self.get_nth_row(i)
            print(" " * (n - i), *row)


# Example usage
if __name__ == "__main__":
    pt = PascalTriangle()

    n = 5
    r = 2

    print("Element at (n={}, r={}):".format(n, r), pt.get_element(n, r))
    print("Nth Row:", pt.get_nth_row(n))
    print("Rth Column:", pt.get_rth_column(r, n + 1))
    pt.print_row(n)
    print("Full Pascal Triangle:")
    pt.print_triangle(n + 1)
