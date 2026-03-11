#!/usr/bin/env python3
"""dice - Roll dice with D&D notation (2d6+3). Zero deps."""
import sys, random, re

def roll(expr):
    expr = expr.lower().replace(" ", "")
    parts = re.findall(r'([+-]?)(\d*)d(\d+)|([+-]?\d+)', expr)
    total, rolls = 0, []
    for sign, count, sides, const in parts:
        if sides:
            n = int(count) if count else 1
            s = int(sides)
            sign_mult = -1 if sign == "-" else 1
            for _ in range(n):
                r = random.randint(1, s)
                rolls.append(r * sign_mult)
                total += r * sign_mult
        elif const:
            total += int(const)
    return total, rolls

def main():
    if len(sys.argv) < 2:
        print("Usage: dice.py <expr> [-n times]"); print("  dice.py 2d6+3"); print("  dice.py 1d20 -n 10"); sys.exit(1)
    expr = sys.argv[1]
    n = 1
    if "-n" in sys.argv: n = int(sys.argv[sys.argv.index("-n")+1])
    results = []
    for _ in range(n):
        t, r = roll(expr)
        results.append(t)
        if n <= 20: print(f"{expr} = {t}  {r}")
    if n > 1:
        print(f"\n{n} rolls: min={min(results)} max={max(results)} avg={sum(results)/len(results):.1f} sum={sum(results)}")

if __name__ == "__main__":
    main()
