import random

def throwThreeCoins():
    coin1 = random.randint(2, 3)
    coin2 = random.randint(2, 3)
    coin3 = random.randint(2, 3)
    results = [coin1, coin2, coin3]
    return results

def sumResults(results):
    total = 0
    for result in results:
        total += result
    return total

def classifyToss(total):
    if total == 6:
        return "changing_yin"    # Old yin (6) - broken line changing to solid
    if total == 7:
        return "static_yang"     # Young yang (7) - solid line, stable
    if total == 8:
        return "static_yin"      # Young yin (8) - broken line, stable
    if total == 9:
        return "changing_yang"   # Old yang (9) - solid line changing to broken
