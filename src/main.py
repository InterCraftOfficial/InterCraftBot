import sys
from intercraftbot import *


def main(argv):

	# Create the InterCraftBot instance
    icBot = InterCraftBot()

    # Execute until finished
    return icBot.run()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
