import uuid
fname = "./coin_purse.staticum"
n_staticums = (1000000)
staticums = [uuid.uuid4().hex for _ in range(n_staticums)]
with open(fname, 'w') as f:
    f.write("\n".join(staticums))
