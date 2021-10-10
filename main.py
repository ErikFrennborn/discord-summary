import subprocess
import glob
import os
import sys
from parser import print_data

def msgHandler(args):
    (message, _) = subprocess.Popen(args,stdout=subprocess.PIPE).communicate()
    return message.decode('utf-8')


def main(argv):
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("DISCORD_TOKEN needs to be set")
        exit()
    if len(argv) != 1:
        print("Needs a channel id/name, must be a dm")
        print(msgHandler(["discord-chat-exporter-cli", "dm", "-t", token]))
        exit()

    if argv[0].isdigit():
        channel = argv[0]
    else:
        channels = msgHandler(["discord-chat-exporter-cli", "dm", "-t", token])
        channel = list(filter(lambda x: argv[0] in x and "Private" in x, channels.split('\n')))
        if len(channel) == 0:
            print("No Such channel exist")
            exit()
        channel = channel[0].split()[0]

    if os.path.exists("data.json"):
        os.remove("data.json")
    try:
        msgHandler(["discord-chat-exporter-cli", "export", "-c", channel, "-f", "json", "-t", token])
    except:
        print("Invalid argument")
        exit()
    os.rename(glob.glob("*.json")[0],"data.json")
    print_data()


if __name__ == "__main__":
    main(sys.argv[1:])
