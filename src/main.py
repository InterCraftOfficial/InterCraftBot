import sys
from client import *

from utils.jsonreader import *


def main(argv):

    client = InterCraftBot()

    jsonLoaderKey = JsonReader()

    client.run(jsonLoaderKey.getServerKey())
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
