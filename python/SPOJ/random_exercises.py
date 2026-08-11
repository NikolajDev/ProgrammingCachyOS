def mix_paint(bucket1, bucket2):
    color, fullness = bucket1["color"], bucket1["fullness"]
    color2, fullness2 = bucket2["color"], bucket2["fullness"]
    output = []
    for i in range(3):
        val = fullness / 100 * color[i]
        val += fullness2 / 100 * color2[i]
        val //= 1
        output.append(int(val))
    return output

print(mix_paint({"color": [143, 143, 101], "fullness": 45}, {"color": [100, 204, 204], "fullness": 90}))