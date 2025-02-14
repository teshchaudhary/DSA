# Cold State: The player whose turn it is will LOSE the game
# Hot State: The player whose turn it is will WIN the game

import math
# Wythoff's Game


def func(A, B):

    # B should always be greater
    if (A > B):
        A, B = B, A

    k = (B-A)

    goldenRatio = (1+math.sqrt(5))//2

    # To determine if the given state is a cold state or a hot state
    checkBy = goldenRatio * k

    if checkBy == A:  # Hot Place
        return False

    else:  # Cold Place
        return True