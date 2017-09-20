import requests, os
from time import sleep
from bs4 import BeautifulSoup


def replace_dollar_signs(name):
    return "".join([x if x != "$" else "\$" for x in name])


def execute(command, output):
    inc = 0
    while 1:
        out = os.popen(command)
        if ("Error" not in out and "Incorrect solution" not in out) or inc > 10:
            break
        else:
            inc += 1
    print(output)


def main():
    while 1:
        try:
            golf = requests.get("http://codegolf.hostbin.org/")
            bs = BeautifulSoup(golf.text, "html5lib")
            for e, x in enumerate(bs.findAll("tr")):
                try:
                    fa = x.findAll("td")
                    if(fa[1].text == "RileyJ" and fa[2].text != "185"):
                        execute("bash rjautosub.sh 2less_kramer.c", "Reseting you")
                    elif "tom" in fa[1].text.lower() and "800" not in fa[2].text:
                        execute("bash tomautosub.sh " + fa[1].text, "Setting Tom")
                    elif "tom" not in fa[1].text.lower() and fa[1].text != "RileyJ" and "799" not in fa[2].text:
                        execute("bash otherautosub.sh " + fa[1].text, fa[1].text)
                except Exception as exx:
                    print(exx)
        except Exception as err:
            print(err)
        sleep(1)

if __name__ == "__main__":
    main()

