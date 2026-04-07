gif = Image.open('vtak.gif')
for i in range(gif.n_frames):
    gif.seek(i)
    gif.save(f'vtak/vtak{i}.png')