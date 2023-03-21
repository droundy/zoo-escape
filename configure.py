import glob
import subprocess

for json in glob.glob("*-cards/*.json"):
    base = json[:-5]
    print(f"| color-splotch --mini-deck --gif --path {base}.json")
    print(f"< {base}.json")
    print(f"> {base}.gif")
    print(
        f"| convert {base}.gif[0] -gravity center -extent 600x825 {base}.png")
    print(f"< {base}.gif")
    print(f"> {base}.png")

for json in glob.glob("board/*.json"):
    base = json[:-5]
    print(f"| color-splotch --mini-deck --gif --path {base}.json")
    print(f"< {base}.json")
    print(f"> {base}.gif")
    print(
        f"| convert {base}.gif[0] -gravity center -extent 800x800 {base}.png")
    print(f"< {base}.gif")
    print(f"> {base}.png")

for json in glob.glob("pieces/*.json"):
    base = json[:-5]
    print(f"| color-splotch --large-circle-chit --gif --path {base}.json")
    print(f"< {base}.json")
    print(f"> {base}.gif")
    print(
        f"| convert {base}.gif[0] -gravity center -extent 375x375 {base}.png")
    print(f"< {base}.gif")
    print(f"> {base}.png")

inkscape_version = subprocess.check_output(['inkscape', '--version'])
if b'0.92' in inkscape_version:
    print('| inkscape -e board/board6x6.png -C -w 4875 board/board6x6.svg')
else:
    print('''
| inkscape -o board/board.png -C -w 4875 board/board.svg

| inkscape -o board/board6x6.png -C -w 4875 board/board6x6.svg

| inkscape -o box.png -C -w 5850 board/box.svg
''')
