#!/usr/bin/env python3

from ..games.engine import engine
from ..games import progression

import sys
sys.path.append("../games")


def main():
    engine(progression)


if __name__ == "__main__":
    main()
