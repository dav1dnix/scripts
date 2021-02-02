from urllib.request import urlopen
from argparse import ArgumentParser
from os import rename, getenv, access, W_OK, X_OK, getuid, remove
from os.path import isdir
from sentry_sdk import init
from pathlib import Path
env_path = Path(".")
from dotenv import load_dotenv
from datetime import datetime
from pwd import getpwuid
from database import db
from tarfile import open as taropen

load_dotenv(verbose=True, dotenv_path=env_path)

init(getenv("SENTRY_SDK_INIT"), traces_sample_rate=1.0)

database = db("database.db")
cur = database.cursor()

uname = getpwuid(getuid())[0]
date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

cur.execute("CREATE TABLE IF NOT EXISTS pdfdocs(user TEXT NOT NULL, dir TEXT NOT NULL, date TEXT NOT NULL)")

def dir_path(d):
    if isdir(d) and access(d, W_OK | X_OK):
        return d
    else:
        raise NotADirectoryError(d)

def args():
    parser = ArgumentParser(description="Specify directory to install to")
    parser.add_argument("-dir", "--dir", type=dir_path)
    return parser

def queryPdfDocsTable():
    cur.execute("SELECT * FROM pdfdocs")
    row = cur.fetchone()
    print(row)

def getPythonDocs(url):
    with urlopen("".join(url)) as resp:
        print("Sending HTTP request...")
        if resp.code == 200:
            arguments = vars(args().parse_args())

            for _, v in arguments.items():
                tarbz2 = "".join(url).split("/")[5]
                with open(tarbz2, "wb") as tar:
                    print(f"Downloading {tarbz2} to {v}")
                    tar.write(resp.read())

                    rename(tarbz2, f"{v}/{tarbz2}")

                    # After moving bz2, extract it! This function returns a TarFile obj :D)
                    with taropen(name=f"{v}/{tarbz2}", mode="r:bz2") as bz2:
                        print("Extracting bz2..")
                        bz2.extractall(path=v)
                        print("Cleaning up..")
                        remove(f"{v}/{tarbz2}")
                        print("Done!")

                        # Make a log of this in database
                        cur.execute("INSERT INTO pdfdocs VALUES (?, ?, ?)", (uname, v, date))
                        print("Creating log... This is only local, thought it would be cool to implement :P")
                        queryPdfDocsTable()

                        # Save changes!
                        database.commit()

                        # Close connection!
                        database.close()
        else:
            print("This function will not work as it is supposed to because the python docs cannot be downloaded")

if __name__ == "__main__":
    getPythonDocs(["https://docs.python.org/3/archives/python-3.9.1-docs-pdf-a4.tar.bz2"])
