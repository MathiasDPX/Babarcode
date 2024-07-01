codes = {
    1: "Drop",
    2: "Forward",
    3: "Inventory",
    4: "Jump",
    5: "LMB",
    6: "RMB",
    7: "Left",
    8: "Backward",
    9: "Right",
    10: "Sneak",
    11: "Sprint",
    12: "Long LMB",
    13: "Escape",
    14: "Eat",
    15: "Long RMB"
}

for i in range(0, 30):
    with open(f"tools/barcodes/{i+1:02d}.svg", "r") as f:
        content = f.read()
        f.close()

    try:
        newText = codes[i+1]
    except:
        newText = f"{i+1:02d}"

    content = content.replace(f">{i+1:02d}</text>", f">{newText}</text>")
    print(f"{i+1:02d} modified to {newText}")

    with open(f"tools/barcodes/{i+1:02d}.svg", "w+") as f:
        f.write(content)
        f.close()