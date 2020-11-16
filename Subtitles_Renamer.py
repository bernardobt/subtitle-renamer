import os
import re

file_path = os.getcwd()
vid_ext = "mkv"
sub_ext = "srt"


def get_file_list(path, v_format, s_format):
    print(f'Getting lists for "{vid_ext}" and "{sub_ext}" files in "{file_path}"...')
    vid_arr = []
    subs_arr = []
    arr = os.listdir(path)
    for i, name in enumerate(arr):
        if name.endswith('.' + v_format):
            vid_arr.append(name)
        elif name.endswith('.' + s_format):
            subs_arr.append(name)
    return vid_arr, subs_arr


def print_lists(lists):
    print("Printing lists...")
    for l1, list in enumerate(lists, start=1):
        print(f"List {l1}")
        for l2, item in enumerate(list,start=1):
            print(f"\t{l2}.{item}")


def rename_files(lists):
    for counter, item in enumerate(lists[0]):
        new = re.sub(f"{vid_ext}", f"{sub_ext}", item)
        os.rename((file_path + '\\' + lists[1][counter]), (file_path + '\\' +new))
        print(f"Renamed: {lists[1][counter]} --> {new}")

lists = get_file_list(file_path, vid_ext, sub_ext)
print_lists(lists)
rename_files(lists)

print('Press Enter key to exit')
input()
