import crypt
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--hash', help='Hash to crack', required=True)
    return parser.parse_args()

def retreive_salt(full_hash):
    #TODO - Complete Me

def crack_pass(hash_to_crack, salt):
    #TODO - Complete Me
        processed_hash = crypt.crypt(str(i), salt)
        print("Hash: %s\n pass: %s" % (processed_hash, i))
        if hash_to_crack == processed_hash:
            print("Found match! \n Password in cleartext: %s" % str(i))
            break

def main():
    args = parse_args()
    salt = retreive_salt(args.hash)
    crack_pass(args.hash, salt)

if __name__ == "__main__":
    main()

