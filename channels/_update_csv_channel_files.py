import subprocess

from yt_videos_list import ListCreator


def main():
    files  = run_shell_command('for file in categories/*.txt; do echo $file; done').split('\n')
    lc     = ListCreator(txt=False, csv=True, md=False, driver='firefox', scroll_pause_time=1.0)
    for file in files:
        lc.create_list_from(path_to_channel_urls_file=file, number_of_threads=4)

def run_shell_command(command):
    return subprocess.getoutput(command)


if __name__ == '__main__':
    main()
