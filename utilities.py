import os

def get_reformatted_headers(filepath):
    header_dict = {}
    with open(filepath, 'r') as f:
        for row in f:
            header_dict[row.split(':')[0]] = row.split(':')[-1]
    return header_dict

def make_dirs(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


if __name__ == '__main__':
    x = get_reformatted_headers(os.path.join('espn_golf', 'headers.txt'))
    print()
