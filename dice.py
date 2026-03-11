#!/usr/bin/env python3
"""Dice roller — parse and roll RPG dice notation (NdM+K)."""
import sys, random, re
def roll(notation):
    m = re.match(r'(\d+)?d(\d+)([+-]\d+)?', notation.lower())
    if not m: return None, f"Invalid: {notation}"
    n, sides, mod = int(m.group(1) or 1), int(m.group(2)), int(m.group(3) or 0)
    rolls = [random.randint(1, sides) for _ in range(n)]
    total = sum(rolls) + mod
    return total, rolls, mod
if __name__ == "__main__":
    exprs = sys.argv[1:] or ["2d6", "1d20", "4d6+3", "d100"]
    for expr in exprs:
        result = roll(expr)
        if result[0] is None: print(result[1])
        else:
            total, rolls, mod = result
            mod_str = f" {'+' if mod>=0 else ''}{mod}" if mod else ""
            print(f"  {expr}: {rolls}{mod_str} = {total}")
