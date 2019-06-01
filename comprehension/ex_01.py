rows = range(1, 4)
cols = range(2, 4)

cells = [(r, c) for r in rows for c in cols]
print(cells)

word = "hottest"
dic = {w: word.count(w) for w in word}

dic1 = {w: word.count(w) for w in set(word)}  # use set
