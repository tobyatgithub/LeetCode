from collections import Counter


def robotWithString(s: str) -> str:
    res = ""
    remain = ""
    candidates = list(s)
    while len(candidates) > 0:
        print(candidates)
        minVal = min(candidates)
        while remain and remain[-1] <= minVal:
            res += remain[-1]
            remain = remain[:-1]
        last = len(candidates) - 1 - candidates[::-1].index(minVal)
        count = Counter(candidates)[minVal]
        res += minVal * count
        remain += "".join(candidates[:last]).replace(minVal, "")
        candidates = candidates[last + 1 :]
        # remain = "".join(candidates[first:]).replace(minVal, "")
        # candidates = candidates[:first]
        # if remain:
        #     candidates = [remain] + candidates

    # res += "".join(candidates)
    res += remain[::-1]
    print(res)


# robotWithString("zza")
robotWithString("vzhofnpo")
# robotWithString("bac")
