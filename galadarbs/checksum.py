#!/usr/bin/env python3
import argparse 
import hashlib

def is_checksum(user_checksum, file_checksum):
    return user_checksum == file_checksum

def get_checksum(filename, hash_type='md5'):
    hash_type = hash_type.lower()

    with open(filename, "rb") as f:
        bytes = f.read()
        if hash_type == "md5":
            checksum = hashlib.md5(bytes).hexdigest()
        elif hash_type == "sha256":
            checksum = hashlib.sha256(bytes).hexdigest()
        else:
            raise Exception("Invalid hash type...")
    return checksum



def main():
    parser = argparse.ArgumentParser(
        prog='Checksum',
        description='Checks if a files checksum matches the vendors checksum.',
        epilog='Usage: checksum.py -f [filename] -t [checksum type] -u [checksum]')
    parser.add_argument('-f', '--filename', required=True)
    parser.add_argument('-t', '--type')
    parser.add_argument('-u', '--user_checksum')
    args = parser.parse_args()
    
    if (args.type == None):
        print("No type specified using MD5 hash by default")
        file_checksum = get_checksum(args.filename)
        if (args.user_checksum == None):
            print(f"No checksum provided: \n\tThe MD5 Cheksum for {args.filename} is {file_checksum}")
        else:
            if is_checksum(args.user_checksum, file_checksum):
                print(f"MD5 file: {file_checksum}")
                print(f"MD5 user: {args.user_checksum}")
                print("Match")
            else:
                print(f"MD5 file: {file_checksum}")
                print(f"MD5 user: {args.user_checksum}")
                print("Dont Match")
    else:
        file_checksum = get_checksum(args.filename, args.type)
        if (args.user_checksum == None):
            print(f"No checksum provided: \n\tThe {args.type} Cheksum for {args.filename} is {file_checksum}")
        else:
            if is_checksum(args.user_checksum, file_checksum):
                print(f"{args.type} file: {file_checksum}")
                print(f"{args.type} user: {args.user_checksum}")
                print("Match")
            else:
                print(f"{args.type} file: {file_checksum}")
                print(f"{args.type} user: {args.user_checksum}")
                print("Dont Match") 




if __name__ == "__main__":
    main()