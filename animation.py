import glob
import moviepy.editor as mpy

class Animate:
        def make_movie(self):
                gif_name = 'outputName'
                file_list = glob.glob('snapshots/*.png') # Get all the pngs in the current directory
                list.sort(file_list, key=lambda x: int(x.split('/')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
                fps = 30
                clip = mpy.ImageSequenceClip(file_list, fps=fps)
                clip.write_gif('{}.gif'.format(gif_name), fps=fps)

