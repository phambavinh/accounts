import json
import random

with open("username.txt") as fo:
    users = [line.strip() for line in fo]

with open("accounts.txt") as fo:
    accs = [line.strip() for line in fo]
random.shuffle(accs)

with open("Phambavinh.json") as f:
    d = json.load(f)

    new_accs = {}
    for a, k in zip(accs, d["Accounts"]):
        new_accs[a] = d["Accounts"][k]

        for i, k1 in enumerate(new_accs[a], start=1):
            new_accs[a][k1]["Character"] = f"{a}00{i}"

    d["Accounts"] = new_accs

    for key in d["Accounts"]:
        idx = 0
        for k2 in d["Accounts"][key]:
            d["Accounts"][key][k2]["Username"] = users[idx]
            idx += 1

with open("ans.json", mode='w') as f1:
    json.dump(d, f1, indent=4)
