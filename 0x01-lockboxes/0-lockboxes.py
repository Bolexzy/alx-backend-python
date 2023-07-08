#!/usr/bin/python3
"""Defines a dunction canUnlockAll();
Determines if all the boxes can be opened in a
number of locked boxes in front of you.
"""


def unlock(idx, key=[]):
    """Unlocks a box with key

    Args:
        idx: The index/key of the box
        Key: A list of positive integers of keys to unlock boxes.

    Returns:
        bool: True if the box can be unlocked, False otherwise
    """
    if not key:
        return False

    for i in range(len(key)):
        if key[i] == idx:
            del key[i]
            return True
    return False


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes
        and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    keys = []  # Store all keys in each box.

    keys.extend(boxes[0])
    unlockedAll = False

    # Iterate through the boxes
    for i in range(1, len(boxes)):
        # Attempt to unlock each box with keys
        unlockedAll = unlock(i, boxes[i], keys)
        # If unlocked add new box keys to keys[]
        key.extend(boxes[i])

    return unlockedAll
