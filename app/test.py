import subprocess, os


OUTPUT_DIR = "/home/intern/check_eat_out/app/uploaded_files/"

def main():
    path = OUTPUT_DIR

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


main()