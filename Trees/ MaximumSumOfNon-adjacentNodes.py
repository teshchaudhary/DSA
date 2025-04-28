"""
Given a binary tree with a value associated with each node. Your task is to select a subset of nodes such that the sum of their values is maximized, with the condition that no two selected nodes are directly connected that is, if a node is included in the subset, neither its parent nor its children can be included.
"""

class Solution:
    def helper(self, root):
        if root is None:
            return (0, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        include = root.data + left[1] + right[1]

        exclude = max(left) + max(right)

        return (include, exclude)

    def getMaxSum(self, root):
        include, exclude = self.helper(root)
        return max(include, exclude)
    
"""       
       10
      /  \
     1    2
    / \  / \
   3  4 5   6

---

At leaves (3, 4, 5, 6):

- `helper(3)` returns `(3, 0)`  
  - Include 3 → 3
  - Exclude 3 → 0

- `helper(4)` returns `(4, 0)`
- `helper(5)` returns `(5, 0)`
- `helper(6)` returns `(6, 0)`


At node 1 (left child of 10):

- Left child (3) → `(3, 0)`
- Right child (4) → `(4, 0)`

- Include 1:
  - 1 + exclude of left (0) + exclude of right (0)  
  - `1 + 0 + 0 = 1`

- Exclude 1:
  - max(include, exclude) of left + max(include, exclude) of right  
  - `max(3,0) + max(4,0) = 3 + 4 = 7`

Result for `helper(1)` = `(1, 7)`


At node 2 (right child of 10):

- Left child (5) → `(5, 0)`
- Right child (6) → `(6, 0)`

- Include 2:
  - 2 + 0 + 0 = 2

- Exclude 2:
  - max(5,0) + max(6,0) = 5 + 6 = 11

Result for `helper(2)` = `(2, 11)`


At root 10:

- Left child (1) → `(1, 7)`
- Right child (2) → `(2, 11)`

- Include 10: 
  - 10 + exclude of left (7) + exclude of right (11)  
  - `10 + 7 + 11 = 28`

- Exclude 10:
  - max(1,7) + max(2,11)  
  - `7 + 11 = 18`

Result for `helper(10)` = `(28, 18)`

### Finally:

| Node | Include | Exclude |
|:----:|:-------:|:-------:|
| 3 | 3 | 0 |
| 4 | 4 | 0 |
| 5 | 5 | 0 |
| 6 | 6 | 0 |
| 1 | 1 | 7 |
| 2 | 2 | 11 |
| 10 | 28 | 18 |

"""