def fibonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    elif length == 1:
        return [start_sequence[0]]
    else:
        while len(start_sequence) != length:
            start_sequence.append(start_sequence[-1] + start_sequence[-2])
        return start_sequence


print(fibonacci_sequence([21, 32], 1))
