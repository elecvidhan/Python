import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    return re.fullmatch(r"[0-255]\.[0-255]\.[0-255]\.[0-255]", ip)


if __name__ == "__main__":
    main()
