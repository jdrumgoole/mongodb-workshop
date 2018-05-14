import srvlookup
import dns.resolver
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--host")
    parser.add_argument("--full", default=False, action="store_true")
    parser.add_argument("--txt", default=False, action="store_true")

    args = parser.parse_args()

    if args.host:
        services = srvlookup.lookup("mongodb", domain=args.host)
        for i in services:
            if args.full:
                print(i)
            else:
                print("%s:%i" % (i.hostname, i.port))

        if args.txt:
            for txtrecord in dns.resolver.query(args.host, 'TXT'):
                print("%s=%s" % (args.host, txtrecord))
    else:
        print("No host specified")
