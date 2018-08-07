import os

import os.path

import sys

import subprocess



OUTPUT_DIR = '/home/intern/check_eat_out/app/uploaded_files/'



def main():

    path = '/home/intern/check_eat_out/app/uploaded_files/'
    filenames = [

        filename

        for filename

        in os.listdir(path)

        if filename.endswith('.m4a')

        ]



    for filename in filenames:

        subprocess.call([

            "ffmpeg", "-i",

            os.path.join(path, filename),

            "-acodec", "libmp3lame", "-ab", "256k",

            os.path.join(OUTPUT_DIR, '%s.mp3' % filename[:-4])

            ])

    return 0


# function_namef(parameter)

main()
#
# if __name__ == '__main__':
#
#     status = main()
#
#     sys.exit(status)
#
#


# import audiosegment
# at = audiosegment.AudioSegment()
# at.('C:\\Users\\LS-COM-00025\\Downloads\\testt.m4a','C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\CheckEatOut\\app\\output.mp3')


# from pydub import AudioSegment
# AudioSegment.converter = "C:\\Users\\LS-COM-00025\\Downloads\\testt.m4a"
# song = AudioSegment.from_mp3("song.mp3")


# import subprocess
#
# m4a = 'C:\\Users\\LS-COM-00025\\Downloads\\testt.m4a'
# cmd = 'lame --preset insane %s' % m4a
# subprocess.call(cmd, shell=True)




# from pydub import AudioSegment
# filepath = 'C:\\Users\\LS-COM-00025\\Downloads\\testt.m4a'
#
# m4a_audio = AudioSegment.from_file(filepath, format="m4a")
# m4a_audio.export(filepath.replace((filepath).split('.')[-1], 'mp3'), format="mp3")

# import subprocess
# command = "ffmpeg -i C:\\Users\\LS-COM-00025\\Downloads\\testt.m4a -ab 160k -ac 2 -ar 44100 -vn audio.wav"
# subprocess.call(command, shell=True)
#
#
#
# for i, m4a_buffer in enumerate(m4a_buffers):
#     f = tempfile.NamedTemporaryFile(dir=voice_datadir, suffix="."+input_audio_extension, prefix="%s_%d"%(username,i), delete=True)
#     f.write(m4a_buffers[i])
#     f.seek(0, os.SEEK_END)
#     chunk = AudioSegment.from_file(f.name, "mp4")
#     chunk.export("%s_%d.wav"%(username,i), format="wav")