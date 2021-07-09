import sys
from random import randint
from functools import reduce
from pyparsing import (
    infixNotation,
    oneOf,
    opAssoc,
    pyparsing_common as ppc,
    ParserElement
)


def dice_action(toks):
    toks = toks[0]
    tot = 0
    for i in range(toks[0]):
        tot += randint(1, toks[2])
    return tot


def plus_minus_action(toks):
    toks = toks[0]
    ret = toks[0]
    for op, val in zip(toks[1::2], toks[2::2]):
        if op == "+":
            ret += val
        elif op == "-":
            ret -= val
        else:
            raise Exception
    return ret


def mult_action(toks):
    toks = toks[0]
    return reduce(lambda acc, y: acc*y, toks[::2], 1)


def sign_action(toks):
    toks = toks[0]
    print(toks)
    if toks[0] == "+":
        return toks[1]
    else:
        return -toks[1]


class DiceParser:
    def __init__(self):
        ParserElement.enablePackrat()
        sys.setrecursionlimit(100)
        integer = ppc.integer

        plusop = oneOf("+ -")
        signop = oneOf("+ -")

        self.expr = infixNotation(
            integer,
            [
                ("d", 2, opAssoc.LEFT, dice_action),
                (signop, 1, opAssoc.RIGHT, sign_action),
                ("*", 2, opAssoc.LEFT, mult_action),
                (plusop, 2, opAssoc.LEFT, plus_minus_action),

            ],
        )

    def parse_expr(self, string: str):
        return self.expr.parseString(string)


if __name__ == '__main__':
    roller = DiceParser()
    print(roller.parse_expr("1"))
