import sys

if len(sys.argv) < 2:
    print("python %s 127.0.0.1" % sys.argv[0])
    sys.exit(0)

try:
    st = sys.argv[1].split(".")
    a = int(st[0]) * 256 * 256 * 256
    b = int(st[1]) * 256 * 256
    c = int(st[2]) * 256
    d = int(st[3])
    ip = a + b + c + d
    print("Your ip is %s" % ip)
except:
    print("Enter a valid IP please.")
