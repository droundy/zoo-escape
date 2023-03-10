import glob

for gif in glob.glob("*-cards/*.gif"):
    base = gif[:-4]
    print(f"| convert {gif}[0] -gravity center -extent 600x825 {base}.png")
    print(f"> {base}.png")


for gif in glob.glob("pieces/*.gif"):
    base = gif[:-4]
    print(f"| convert {gif}[0] -gravity center -extent 375x375 {base}.png")
    print(f"> {base}.png")
