import argparse
import os
import tempfile


data = {}
res = []

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
try:
    if args.key and args.val:
        with open(storage_path, 'a') as f:
            str = '{}, {}\n'.format(args.key, args.val)
            f.write(str)
    elif args.key:
        with open(storage_path, 'r+') as f:
            content = f.readlines()
        for pair in content:
            item_list = pair.replace(" ", "").strip().split(",")
            if item_list[0] == args.key:
                res.append(item_list[1])
        print(*res, sep=', ')
except FileNotFoundError:
    print()
