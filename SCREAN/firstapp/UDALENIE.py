import os


def all_img_delete():
    os.system(f"del {os.path.abspath('./static/img/')} /q")
