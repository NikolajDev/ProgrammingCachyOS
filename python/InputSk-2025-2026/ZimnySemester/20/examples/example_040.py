gif = Image.open('vtak.gif')
i = 0
while True:
    gif.save(f'vtak/vtak{i}.png')
    try:
        i += 1
        gif.seek(i)
    except EOFError:
        break