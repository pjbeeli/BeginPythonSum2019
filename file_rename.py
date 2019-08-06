"""
Rename files from a folder
"""
import os


def rename_files():
    """
    Rename files in a folder
    :return: nothing
    """
    folder_dir = r"C:\Users\piederbeeli\prankOrig"  # raw text
    saved_path = os.getcwd() # save current working directory
    files = os.listdir(folder_dir)
    os.chdir(folder_dir)
    print(files)
    for file in files:
        new_file = file.lstrip('0123456789')
        print("old name", file, "new name", new_file,  type(file))
        os.rename(file, new_file)
    # return to original directory
    os.chdir(saved_path)

def main():
    """
    test function
    :return:
    """
    rename_files()


if __name__ == '__main__':
    main()
    exit(0)