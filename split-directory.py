
import argparse
import os
import shutil


def split_dir(abs_dirname, N):
    """Move files into subdirectories."""

    files = [os.path.join(abs_dirname, f) for  f in os.listdir(abs_dirname)]    
    i = 0   

    for f in files:
        while(os.path.isfile(f)):
            # create new subdir if necessary
            if i % N == 0:            
                subdir_name = os.path.join(abs_dirname, '{0:03d}'.format(int(i / N + 1)))
                os.mkdir(subdir_name)
                print("Created sub directories "+ subdir_name)

            # move file to current dir
            f_base = os.path.basename(f)
            shutil.move(f, os.path.join(subdir_name, f_base))
            print("Moved File "+ f_base + " into sub directory "+ subdir_name)
            i += 1

def split_fixed_dir(abs_dirname, dir_count):
    """Move files into subdirectories."""

    files = [os.path.join(abs_dirname, f) for  f in os.listdir(abs_dirname)]  

    # create new fixed subdir if necessary
    i = 1

    while (i <= dir_count):
        subdir_name = os.path.join(abs_dirname + '{0:03d}'.format(i))
        os.mkdir(subdir_name)
        print("Created sub directories "+ subdir_name)
        i = i+1
    j = 1

    for f in files:
        while(os.path.isfile(f)):
            if j <= dir_count:
                curr_subdir = os.path.join(abs_dirname + '{0:03d}'.format(j))
            else:
                j = 1
                curr_subdir = os.path.join(abs_dirname + '{0:03d}'.format(j))

            # move file to current dir
            shutil.move(f, curr_subdir)
            j += 1
            print("Moved File "+ os.path.basename(f) + " into sub directory "+ curr_subdir)


def parse_args():
    """Parse command line arguments passed to script invocation."""
    parser = argparse.ArgumentParser(
        description='Split files into multiple subfolders.')

    parser.add_argument('src_dir', help='source directory')
    parser.add_argument('split_opt', help='split options')
    parser.add_argument('fix_val', help='fixed value')

    return parser.parse_args()


def main():
    """Module's main entry point """
    args = parse_args()
    src_dir = args.src_dir
    split_opt = args.split_opt
    fix_val = args.fix_val

    if not os.path.exists(src_dir):
        raise Exception('Directory does not exist ({0}).'.format(src_dir))

    if (int(split_opt) == 2):
        split_fixed_dir(os.path.abspath(src_dir), int(fix_val))
    elif (int(split_opt) == 1):
        split_dir(os.path.abspath(src_dir), int(fix_val))
    else:
        print("Invalid Option")

if __name__ == '__main__':
    main()
