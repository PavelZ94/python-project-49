#!/usr/bin/env python3


from ..games.engine import engine
from ..games import even

import sys
sys.path.append("../games")


def main():
    engine(even)


if __name__ == "__main__":
    main()
