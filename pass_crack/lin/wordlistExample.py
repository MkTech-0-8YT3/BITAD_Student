import crypt
import sys
import argparse

def get_wordlist_content(wordlist):
    #TODO - Complete Me

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--hash', help='Hash to crack', required=True)
    parser.add_argument('-w', '--wordlist', help='Wordlist', required=True)
    return parser.parse_args()

def retreive_salt(full_hash):
    #TODO - Complete Me

def crack_pass(hash_to_crack, salt, wordlist):
    #TODO - Complete Me - tip: split the result
        processed_hash = crypt.crypt(str(passwd), salt)
        print("Hash: %s\n pass: %s" % (processed_hash, passwd))
        if hash_to_crack == processed_hash:
            print("Found match! \n Password in cleartext: %s" % str(passwd))
            break

def main():
    args = parse_args()
    salt = retreive_salt(args.hash)
    crack_pass(args.hash, salt, args.wordlist)

if __name__ == "__main__":
    main()
