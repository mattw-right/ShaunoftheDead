import glob
import moviepy.editor as mpy
from PIL import Image

turns = 2349

frames = []
for i in range(turns):
        new_frame = Image.open('snapshots/{}.png'.format(i))
        frames.append(new_frame)


# Save into a GIF file that loops forever
frames[0].save('output.gif', format='GIF',
           append_images=frames[:],
           save_all=True,
           duration=30, loop=1)

