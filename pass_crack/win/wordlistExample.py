import bcrypt
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

def crack_pass(pass_to_crack, wordlist, salt):
    #TODO - Complete Me - tip: split the result
        processed_hash = bcrypt.hashpw(str(passwd).encode(), salt.encode())
        print("Hash: %s\n pass: %s" % (processed_hash.decode("utf8"), passwd))
        if pass_to_crack == str(processed_hash.decode('utf8')):
            print("Found match! \n Password in cleartext: %s" % str(passwd))
            break

def main():
    args = parse_args()
    salt = retreive_salt(args.hash)
    crack_pass(args.hash, args.wordlist, salt)

if __name__ == "__main__":
	main()
