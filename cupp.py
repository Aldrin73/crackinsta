#!/usr/bin/python3
#
#  [Program]
#
#  CUPP
#  Common User Passwords Profiler
#
#  [Author]
#
#  Muris Kurgas aka j0rgan
#  j0rgan [at] remote-exploit [dot] org
#  http://www.remote-exploit.org
#  http://www.azuzi.me
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See ‘LICENSE’ for more information.

Import argparse
Import configparser
Import csv
Import functools
Import gzip
Import os
Import sys
Import urllib.error
Import urllib.parse
Import urllib.request

__author__ = “Muris Kurgas”
__license__ = “GPL”
__version__ = “3.2.5-alpha”

CONFIG = {}


Def read_config(filename):
    “””Read the given configuration file and update global variables to reflect
    Changes (CONFIG).”””

    If os.path.isfile(filename):

        # global CONFIG

        # Reading configuration file
        Config = configparser.ConfigParser()
        Config.read(filename)

        CONFIG[“global”] = {
            “years”: config.get(“years”, “years”).split(“,”),
            “chars”: config.get(“specialchars”, “chars”).split(“,”),
            “numfrom”: config.getint(“nums”, “from”),
            “numto”: config.getint(“nums”, “to”),
            “wcfrom”: config.getint(“nums”, “wcfrom”),
            “wcto”: config.getint(“nums”, “wcto”),
            “threshold”: config.getint(“nums”, “threshold”),
            “alectourl”: config.get(“alecto”, “alectourl”),
            “dicturl”: config.get(“downloader”, “dicturl”),
        }

        # 1337 mode configs, well you can add more lines if you add it to the
        # config file too.
        Leet = functools.partial(config.get, “leet”)
        Leetc = {}
        Letters = {“a”, “I”, “e”, “t”, “o”, “s”, “g”, “z”}

        For letter in letters:
            Leetc[letter] = config.get(“leet”, letter)

        CONFIG[“LEET”] = leetc

        Return True

    Else:
        Print(“Configuration file “ + filename + “ not found!”)
        Sys.exit(“Exiting.”)

        Return False


Def make_leet(x):
    “””convert string to leet”””
    For letter, leetletter in CONFIG[“LEET”].items():
        X = x.replace(letter, leetletter)
    Return x


# for concatenations…
Def concats(seq, start, stop):
    For mystr in seq:
        For num in range(start, stop):
            Yield mystr + str(num)


# for sorting and making combinations…
Def komb(seq, start, special=””):
    For mystr in seq:
        For mystr1 in start:
            Yield mystr + special + mystr1


# print list to file counting words


Def print_to_file(filename, unique_list_finished):
    F = open(filename, “w”)
    Unique_list_finished.sort()
    f.write(os.linesep.join(unique_list_finished))
    f.close()
    f = open(filename, “r”)
    lines = 0
    for line in f:
        lines += 1
    f.close()
    print(
        “[+] Saving dictionary to \033[1;31m”
        + filename
        + “\033[1;m, counting \033[1;31m”
        + str(lines)
        + “ words.\033[1;m”
    )
    Print(
        “[+] Now load your pistolero with \033[1;31m”
        + filename
        + “\033[1;m and shoot! Good luck!”
    )


Def print_cow():
    Print(“ ___________ “)
    Print(“ \033[07m  cupp.py! \033[27m                # Common”)
    Print(“      \                     # User”)
    Print(“       \   \033[1;31m,__,\033[1;m             # Passwords”)
    Print(“        \  \033[1;31m(\033[1;moo\033[1;31m)____\033[1;m         # Profiler”)
    Print(“           \033[1;31m(__)    )\ \033[1;m  “)
    Print(
        “           \033[1;31m   ||--|| \033[1;m\033[05m*\033[25m\033[1;m      [ Muris Kurgas | j0rgan@remote-exploit.org ]”
    )
    Print(28 * “ “ + “[ Mebus | https://github.com/Mebus/]\r\n”)


Def version():
    “””Display version”””

    Print(“\r\n	\033[1;31m[ cupp.py ]  “ + __version__ + “\033[1;m\r\n”)
    Print(“	* Hacked up by j0rgan – j0rgan@remote-exploit.org”)
    Print(“	* http://www.remote-exploit.org\r\n”)
    Print(“	Take a look ./README.md file for more info about the program\r\n”)


Def improve_dictionary(file_to_open):
    “””Implementation of the -w option. Improve a dictionary by
    Interactively questioning the user.”””

    Kombinacija = {}
    Komb_unique = {}

    If not os.path.isfile(file_to_open):
        Exit(“Error: file “ + file_to_open + “ does not exist.”)

    Chars = CONFIG[“global”][“chars”]
    Years = CONFIG[“global”][“years”]
    Numfrom = CONFIG[“global”][“numfrom”]
    Numto = CONFIG[“global”][“numto”]

    Fajl = open(file_to_open, “r”)
    Listic = fajl.readlines()
    Listica = []
    For x in listic:
        Listica += x.split()

    Print(“\r\n      *************************************************”)
    Print(“      *                    \033[1;31mWARNING!!!\033[1;m                 *”)
    Print(“      *         Using large wordlists in some         *”)
    Print(“      *       options bellow is NOT recommended!      *”)
    Print(“      *************************************************\r\n”)

    Conts = input(
        “> Do you want to concatenate all words from wordlist? Y/[N]: “
    ).lower()
If conts == “y” and len(listic) > CONFIG[“global”][“threshold”]:
        Print(
            “\r\n[-] Maximum number of words for concatenation is “
            + str(CONFIG[“global”][“threshold”])
        )
        Print(“[-] Check configuration file for increasing this number.\r\n”)
        Conts = input(
            “> Do you want to concatenate all words from wordlist? Y/[N]: “
        ).lower()

    Cont = [“”]
    If conts == “y”:
        For cont1 in listica:
            For cont2 in listica:
                If listica.index(cont1) != listica.index(cont2):
                    Cont.append(cont1 + cont2)

    Spechars = [“”]
    Spechars1 = input(
        “> Do you want to add special chars at the end of words? Y/[N]: “
    ).lower()
    If spechars1 == “y”:
        For spec1 in chars:
            Spechars.append(spec1)
            For spec2 in chars:
                Spechars.append(spec1 + spec2)
                For spec3 in chars:
                    Spechars.append(spec1 + spec2 + spec3)

    Randnum = input(
        “> Do you want to add some random numbers at the end of words? Y/[N]:”
    ).lower()
    Leetmode = input(“> Leet mode? (i.e. leet = 1337) Y/[N]: “).lower()

    # init
    For I in range(6):
        Kombinacija[i] = [“”]

    Kombinacija[0] = list(komb(listica, years))
    If conts == “y”:
        Kombinacija[1] = list(komb(cont, years))
    If spechars1 == “y”:
        Kombinacija[2] = list(komb(listica, spechars))
        If conts == “y”:
            Kombinacija[3] = list(komb(cont, spechars))
    If randnum == “y”:
        Kombinacija[4] = list(concats(listica, numfrom, numto))
        If conts == “y”:
            Kombinacija[5] = list(concats(cont, numfrom, numto))

    Print(“\r\n[+] Now making a dictionary…”)

    Print(“[+] Sorting list and removing duplicates…”)

    For I in range(6):
        Komb_unique[i] = list(dict.fromkeys(kombinacija[i]).keys())

    Komb_unique[6] = list(dict.fromkeys(listica).keys())
    Komb_unique[7] = list(dict.fromkeys(cont).keys())

    # join the lists
    Uniqlist = []
    For I in range(8):
        Uniqlist += komb_unique[i]

    Unique_lista = list(dict.fromkeys(uniqlist).keys())
    Unique_leet = []
    If leetmode == “y”:
        For (
            X
        ) in (
            Unique_lista
        ):  # if you want to add more leet chars, you will need to add more lines in cupp.cfg too…
            X = make_leet(x)  # convert to leet
            Unique_leet.append(x)

    Unique_list = unique_lista + unique_leet

    Unique_list_finished = []

    Unique_list_finished = [
        X
        For x in unique_list
        If len(x) > CONFIG[“global”][“wcfrom”] and len(x) < CONFIG[“global”][“wcto”]
    ]

    Print_to_file(file_to_open + “.cupp.txt”, unique_list_finished)

    Fajl.close()


Def interactive():
    “””Implementation of the -I switch. Interactively question the user and
    Create a password dictionary file based on the answer.”””

    Print(“\r\n[+] Insert the information about the victim to make a dictionary”)
    Print(“[+] If you don’t know all the info, just hit enter when asked! ;)\r\n”)

    # We need some information first!

    Profile = {}

    Name = input(“> First Name: “).lower()
    While len(name) == 0 or name == “ “ or name == “  “ or name == “   “:
        Print(“\r\n[-] You must enter a name at least!”)
        Name = input(“> Name: “).lower()
    Profile[“name”] = str(name)

    Profile[“surname”] = input(“> Surname: “).lower()
    Profile[“nick”] = input(“> Nickname: “).lower()
    Birthdate = input(“> Birthdate (DDMMYYYY): “)
    While len(birthdate) != 0 and len(birthdate) != 8:
        Print(“\r\n[-] You must enter 8 digits for birthday!”)
        Birthdate = input(“> Birthdate (DDMMYYYY): “)
    Profile[“birthdate”] = str(birthdate)

    Print(“\r\n”)

    Profile[“wife”] = input(“> Partners) name: “).lower()
    Profile[“wifen”] = input(“> Partners) nickname: “).lower()
    Wifeb = input(“> Partners) birthdate (DDMMYYYY): “)
    While len(wifeb) != 0 and len(wifeb) != 8:
        Print(“\r\n[-] You must enter 8 digits for birthday!”)
        Wifeb = input(“> Partners birthdate (DDMMYYYY): “)
    Profile[“wifeb”] = str(wifeb)
    Print(“\r\n”)

    Profile[“kid”] = input(“> Child’s name: “).lower()
    Profile[“kidn”] = input(“> Child’s nickname: “).lower()
    Kidb = input(“> Child’s birthdate (DDMMYYYY): “)
    While len(kidb) != 0 and len(kidb) != 8:
        Print(“\r\n[-] You must enter 8 digits for birthday!”)
        Kidb = input(“> Child’s birthdate (DDMMYYYY): “)
    Profile[“kidb”] = str(kidb)
    Print(“\r\n”)

    Profile[“pet”] = input(“> Pet’s name: “).lower()
    Profile[“company”] = input(“> Company name: “).lower()
    Print(“\r\n”)

    Profile[“words”] = [“”]
    Words1 = input(
        “> Do you want to add some key words about the victim? Y/[N]: “
    ).lower()
    Words2 = “”
    If words1 == “y”:
        Words2 = input(
            “> Please enter the words, separated by comma. [i.e. hacker,juice,black], spaces will be removed: “
        ).replace(“ “, “”)
    Profile[“words”] = words2.split(“,”)

    Profile[“spechars1”] = input(
        “> Do you want to add special chars at the end of words? Y/[N]: “
    ).lower()

    Profile[“randnum”] = input(
        “> Do you want to add some random numbers at the end of words? Y/[N]:”
    ).lower()
    Profile[“leetmode”] = input(“> Leet mode? (i.e. leet = 1337) Y/[N]: “).lower()

    Generate_wordlist_from_profile(profile)  # generate the wordlist


Def generate_wordlist_from_profile(profile):
    “”” Generates a wordlist from a given profile “””

    Chars = CONFIG[“global”][“chars”]
    Years = CONFIG[“global”][“years”]
    Numfrom = CONFIG[“global”][“numfrom”]
    Numto = CONFIG[“global”][“numto”]

    Profile[“spechars”] = []

    If profile[“spechars1”] == “y”:
        For spec1 in chars:
            Profile[“spechars”].append(spec1)
            For spec2 in chars:
                Profile[“spechars”].append(spec1 + spec2)
                For spec3 in chars:
                    Profile[“spechars”].append(spec1 + spec2 + spec3)

    Print(“\r\n[+] Now making a dictionary…”)

    # Now me must do some string m# Birthdays first

    Birthdate_yy = profile[“birthdate”][-2:]
    Birthdate_yyy = profile[“birthdate”][-3:]
    Birthdate_yyyy = profile[“birthdate”][-4:]
    Birthdate_xd = profile[“birthdate”][1:2]
    Birthdate_xm = profile[“birthdate”][3:4]
    Birthdate_dd = profile[“birthdate”][:2]
    Birthdate_mm = profile[“birthdate”][2:4]

    Wifeb_yy = profile[“wifeb”][-2:]
    Wifeb_yyy = profile[“wifeb”][-3:]
    Wifeb_yyyy = profile[“wifeb”][-4:]
    Wifeb_xd = profile[“wifeb”][1:2]
    Wifeb_xm = profile[“wifeb”][3:4]
    Wifeb_dd = profile[“wifeb”][:2]
    Wifeb_mm = profile[“wifeb”][2:4]

    Kidb_yy = profile[“kidb”][-2:]
    Kidb_yyy = profile[“kidb”][-3:]
    Kidb_yyyy = profile[“kidb”][-4:]
    Kidb_xd = profile[“kidb”][1:2]
    Kidb_xm = profile[“kidb”][3:4]
    Kidb_dd = profile[“kidb”][:2]
    Kidb_mm = profile[“kidb”][2:4]

    # Convert first letters to uppercase…

    Nameup = profile[“name”].title()
    Surnameup = profile[“surname”].title()
    Nickup = profile[“nick”].title()
    Wifeup = profile[“wife”].title()
    Wifenup = profile[“wifen”].title()
    Kidup = profile[“kid”].title()
    Kidnup = profile[“kidn”].title()
    Petup = profile[“pet”].title()
    Companyup = profile[“company”].title()

    Wordsup = []
    Wordsup = list(map(str.title, profile[“words”]))

    Word = profile[“words”] + wordsup

    # reverse a name

    Rev_name = profile[“name”][::-1]
    Rev_nameup = nameup[::-1]
    Rev_nick = profile[“nick”][::-1]
    Rev_nickup = nickup[::-1]
    Rev_wife = profile[“wife”][::-1]
    Rev_wifeup = wifeup[::-1]
    Rev_kid = profile[“kid”][::-1]
    Rev_kidup = kidup[::-1]

    Reverse = [
        Rev_name,
        Rev_nameup,
        Rev_nick,
        Rev_nickup,
        Rev_wife,
        Rev_wifeup,
        Rev_kid,
        Rev_kidup,
    ]
    Rev_n = [rev_name, rev_nameup, rev_nick, rev_nickup]
    Rev_w = [rev_wife, rev_wifeup]
    Rev_k = [rev_kid, rev_kidup]
    # Let’s do some serious work! This will be a mess of code, but… who cares? 

    # Birthdays combinations

    Bds = [
        Birthdate_yy,
        Birthdate_yyy,
        Birthdate_yyyy,
        Birthdate_xd,
        Birthdate_xm,
        Birthdate_dd,
        Birthdate_mm,
    ]

    Bdss = []

    For bds1 in bds:
        Bdss.append(bds1)
        For bds2 in bds:
            If bds.index(bds1) != bds.index(bds2):
                Bdss.append(bds1 + bds2)
                For bds3 in bds:
                    If (
                        Bds.index(bds1) != bds.index(bds2)
                        And bds.index(bds2) != bds.index(bds3)
                        And bds.index(bds1) != bds.index(bds3)
                    ):
                        Bdss.append(bds1 + bds2 + bds3)

                # For a woman…
    Wbds = [wifeb_yy, wifeb_yyy, wifeb_yyyy, wifeb_xd, wifeb_xm, wifeb_dd, wifeb_mm]

    Wbdss = []

    For wbds1 in wbds:
        Wbdss.append(wbds1)
        For wbds2 in wbds:
            If wbds.index(wbds1) != wbds.index(wbds2):
                Wbdss.append(wbds1 + wbds2)
                For wbds3 in wbds:
                    If (
                        Wbds.index(wbds1) != wbds.index(wbds2)
                        And wbds.index(wbds2) != wbds.index(wbds3)
                        And wbds.index(wbds1) != wbds.index(wbds3)
                    ):
                        Wbdss.append(wbds1 + wbds2 + wbds3)

                # and a child…
    Kbds = [kidb_yy, kidb_yyy, kidb_yyyy, kidb_xd, kidb_xm, kidb_dd, kidb_mm]

    Kbdss = []

    For kbds1 in kbds:
        Kbdss.append(kbds1)
        For kbds2 in kbds:
            If kbds.index(kbds1) != kbds.index(kbds2):
                Kbdss.append(kbds1 + kbds2)
                For kbds3 in kbds:
                    If (
                        Kbds.index(kbds1) != kbds.index(kbds2)
                        And kbds.index(kbds2) != kbds.index(kbds3)
                        And kbds.index(kbds1) != kbds.index(kbds3)
                    ):
                        Kbdss.append(kbds1 + kbds2 + kbds3)

                # string combinations….

    Kombinaac = [profile[“pet”], petup, profile[“company”], companyup]

    Kombina = [
        Profile[“name”],
        Profile[“surname”],
        Profile[“nick”],
        Nameup,
        Surnameup,
        Nickup,
    ]

    Kombinaw = [
        Profile[“wife”],
        Profile[“wifen”],
        Wifeup,
        Wifenup,
        Profile[“surname”],
        Surnameup,
    ]

    Kombinak = [
        Profile[“kid”],
        Profile[“kidn”],
        Kidup,
        Kidnup,
        Profile[“surname”],
        Surnameup,
    ]

    Kombinaa = []
    For kombina1 in kombina:
        Kombinaa.append(kombina1)
        For kombina2 in kombina:
            If kombina.index(kombina1) != kombina.index(kombina2) and kombina.index(
                Kombina1.title()
            ) != kombina.index(kombina2.title()):
                Kombinaa.append(kombina1 + kombina2)

    Kombinaaw = []
    For kombina1 in kombinaw:
        Kombinaaw.append(kombina1)
        For kombina2 in kombinaw:
            If kombinaw.index(kombina1) != kombinaw.index(kombina2) and kombinaw.index(
                Kombina1.title()
            ) != kombinaw.index(kombina2.title()):
                Kombinaaw.append(kombina1 + kombina2)

    Kombinaak = []
    For kombina1 in kombinak:
        Kombinaak.append(kombina1)
        For kombina2 in kombinak:
            If kombinak.index(kombina1) != kombinak.index(kombina2) and kombinak.index(
                Kombina1.title()
            ) != kombinak.index(kombina2.title()):
                Kombinaak.append(kombina1 + kombina2)
Kombi = {}
    Kombi[1] = list(komb(kombinaa, bdss))
    Kombi[1] += list(komb(kombinaa, bdss, “_”))
    Kombi[2] = list(komb(kombinaaw, wbdss))
    Kombi[2] += list(komb(kombinaaw, wbdss, “_”))
    Kombi[3] = list(komb(kombinaak, kbdss))
    Kombi[3] += list(komb(kombinaak, kbdss, “_”))
    Kombi[4] = list(komb(kombinaa, years))
    Kombi[4] += list(komb(kombinaa, years, “_”))
    Kombi[5] = list(komb(kombinaac, years))
    Kombi[5] += list(komb(kombinaac, years, “_”))
    Kombi[6] = list(komb(kombinaaw, years))
    Kombi[6] += list(komb(kombinaaw, years, “_”))
    Kombi[7] = list(komb(kombinaak, years))
    Kombi[7] += list(komb(kombinaak, years, “_”))
    Kombi[8] = list(komb(word, bdss))
    Kombi[8] += list(komb(word, bdss, “_”))
    Kombi[9] = list(komb(word, wbdss))
    Kombi[9] += list(komb(word, wbdss, “_”))
    Kombi[10] = list(komb(word, kbdss))
    Kombi[10] += list(komb(word, kbdss, “_”))
    Kombi[11] = list(komb(word, years))
    Kombi[11] += list(komb(word, years, “_”))
    Kombi[12] = [“”]
    Kombi[13] = [“”]
    Kombi[14] = [“”]
    Kombi[15] = [“”]
    Kombi[16] = [“”]
    Kombi[21] = [“”]
    If profile[“randnum”] == “y”:
        Kombi[12] = list(concats(word, numfrom, numto))
        Kombi[13] = list(concats(kombinaa, numfrom, numto))
        Kombi[14] = list(concats(kombinaac, numfrom, numto))
        Kombi[15] = list(concats(kombinaaw, numfrom, numto))
        Kombi[16] = list(concats(kombinaak, numfrom, numto))
        Kombi[21] = list(concats(reverse, numfrom, numto))
    Kombi[17] = list(komb(reverse, years))
    Kombi[17] += list(komb(reverse, years, “_”))
    Kombi[18] = list(komb(rev_w, wbdss))
    Kombi[18] += list(komb(rev_w, wbdss, “_”))
    Kombi[19] = list(komb(rev_k, kbdss))
    Kombi[19] += list(komb(rev_k, kbdss, “_”))
    Kombi[20] = list(komb(rev_n, bdss))
    Kombi[20] += list(komb(rev_n, bdss, “_”))
    Komb001 = [“”]
    Komb002 = [“”]
    Komb003 = [“”]
    Komb004 = [“”]
    Komb005 = [“”]
    Komb006 = [“”]
    If len(profile[“spechars”]) > 0:
        Komb001 = list(komb(kombinaa, profile[“spechars”]))
        Komb002 = list(komb(kombinaac, profile[“spechars”]))
        Komb003 = list(komb(kombinaaw, profile[“spechars”]))
        Komb004 = list(komb(kombinaak, profile[“spechars”]))
        Komb005 = list(komb(word, profile[“spechars”]))
        Komb006 = list(komb(reverse, profile[“spechars”]))

    Print(“[+] Sorting list and removing duplicates…”)

    Komb_unique = {}
    For I in range(1, 22):
        Komb_unique[i] = list(dict.fromkeys(kombi[i]).keys())

    Komb_unique01 = list(dict.fromkeys(kombinaa).keys())
    Komb_unique02 = list(dict.fromkeys(kombinaac).keys())
    Komb_unique03 = list(dict.fromkeys(kombinaaw).keys())
    Komb_unique04 = list(dict.fromkeys(kombinaak).keys())
    Komb_unique05 = list(dict.fromkeys(word).keys())
    Komb_unique07 = list(dict.fromkeys(komb001).keys())
    Komb_unique08 = list(dict.fromkeys(komb002).keys())
    Komb_unique09 = list(dict.fromkeys(komb003).keys())
    Komb_unique010 = list(dict.fromkeys(komb004).keys())
    Komb_unique011 = list(dict.fromkeys(komb005).keys())
    Komb_unique012 = list(dict.fromkeys(komb006).keys())

    Uniqlist = (
        Bdss
        + wbdss
        + kbdss
        + reverse
        + komb_unique01
        + komb_unique02
        + komb_unique03
        + komb_unique04
        + komb_unique05
    )

    For I in range(1, 21):
        Uniqlist += komb_unique[i]

    Uniqlist += (
        Komb_unique07
        + komb_unique08
        + komb_unique09
        + komb_unique010
        + komb_unique011
        + komb_unique012
    )
    Unique_lista = list(dict.fromkeys(uniqlist).keys())
    Unique_leet = []
    If profile[“leetmode”] == “y”:
        For (
            X
        ) in (
            Unique_lista
        ):  # if you want to add more leet chars, you will need to add more lines in cupp.cfg too…

            X = make_leet(x)  # convert to leet
            Unique_leet.append(x)

    Unique_list = unique_lista + unique_leet

    Unique_list_finished = []
    Unique_list_finished = [
        X
        For x in unique_list
        If len(x) < CONFIG[“global”][“wcto”] and len(x) > CONFIG[“global”][“wcfrom”]
    ]

    Print_to_file(profile[“name”] + “.txt”, unique_list_finished)


Def download_http(url, targetfile):
    Print(“[+] Downloading “ + targetfile + “ from “ + url + “ … “)
    webFile = urllib.request.urlopen(url)
    localFile = open(targetfile, “wb”)
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()


def alectodb_download():
    “””Download csv from alectodb and save into local file as a list of
    Usernames and passwords”””
     url = CONFIG[“global”][“alectourl”]

    print(“\r\n[+] Checking if alectodb is not present…”)

    targetfile = “alectodb.csv.gz”

    if not os.path.isfile(targetfile):

        download_http(url, targetfile)

    f = gzip.open(targetfile, “rt”)

    data = csv.reader(f)

    usernames = []
    passwords = []
    for row in data:
        usernames.append(row[5])
        passwords.append(row[6])
    gus = list(set(usernames))
    gpa = list(set(passwords))
    gus.sort()
    gpa.sort()

    print(
        “\r\n[+] Exporting to alectodb-usernames.txt and alectodb-passwords.txt\r\n[+] Done.”
    )
    F = open(“alectodb-usernames.txt”, “w”)
    f.write(os.linesep.join(gus))
    f.close()

    f = open(“alectodb-passwords.txt”, “w”)
    f.write(os.linesep.join(gpa))
    f.close()


def download_wordlist():
    “””Implementation of -l switch. Download wordlists from http repository as
    Defined in the configuration file.”””
Print(“	\r\n	Choose the section you want to download:\r\n”)

    Print(“     1   Moby            14      french          27      places”)
    Print(“     2   afrikaans       15      german          28      polish”)
    Print(“     3   american        16      hindi           29      random”)
    Print(“     4   aussie          17      hungarian       30      religion”)
    Print(“     5   chinese         18      italian         31      russian”)
    Print(“     6   computer        19      japanese        32      science”)
    Print(“     7   croatian        20      latin           33      spanish”)
    Print(“     8   czech           21      literature      34      swahili”)
    Print(“     9   danish          22      movieTV         35      swedish”)
    Print(“    10   databases       23      music           36      turkish”)
    Print(“    11   dictionaries    24      names           37      yiddish”)
    Print(“    12   dutch           25      net             38      exit program”)
    Print(“    13   finnish         26      norwegian       \r\n”)
    Print(
        “	\r\n	Files will be downloaded from “
        + CONFIG[“global”][“dicturl”]
        + “ repository”
    )
    Print(
        “	\r\n	Tip: After downloading wordlist, you can improve it with -w option\r\n”
    )

    Filedown = input(“> Enter number: “)
    Filedown.isdigit()
    While filedown.isdigit() == 0:
        Print(“\r\n[-] Wrong choice. “)
        Filedown = input(“> Enter number: “)
    Filedown = str(filedown)
    While int(filedown) > 38 or int(filedown) < 0:
        Print(“\r\n[-] Wrong choice. “)
        Filedown = input(“> Enter number: “)
    Filedown = str(filedown)

    Download_wordlist_http(filedown)
    Return filedown


Def download_wordlist_http(filedown):
    “”” do the HTTP download of a wordlist “””

    Mkdir_if_not_exists(“dictionaries”)

    # List of files to download:
    Arguments = {
        1: (
            “Moby”,
            (
                “mhyph.tar.gz”,
                “mlang.tar.gz”,
                “moby.tar.gz”,
                “mpos.tar.gz”,
                “mpron.tar.gz”,
                “mthes.tar.gz”,
                “mwords.tar.gz”,
            ),
        ),
        2: (“afrikaans”, (“afr_dbf.zip”,)),
        3: (“american”, (“dic-0294.tar.gz”,)),
        4: (“aussie”, (“oz.gz”,)),
        5: (“chinese”, (“chinese.gz”,)),
        6: (
            “computer”,
            (
                “Domains.gz”,
                “Dosref.gz”,
                “Ftpsites.gz”,
                “Jargon.gz”,
                “common-passwords.txt.gz”,
                “etc-hosts.gz”,
                “foldoc.gz”,
                “language-list.gz”,
                “unix.gz”,
            ),
        ),
        7: (“croatian”, (“croatian.gz”,)),
        8: (“czech”, (“czech-wordlist-ascii-cstug-novak.gz”,)),
        9: (“danish”, (“danish.words.gz”, “dansk.zip”)),
        10: (
            “databases”,
            (“acronyms.gz”, “att800.gz”, “computer-companies.gz”, “world_heritage.gz”),
        ),
        11: (
            “dictionaries”,
            (
                “Antworth.gz”,
                “CRL.words.gz”,
                “Roget.words.gz”,
                “Unabr.dict.gz”,
                “Unix.dict.gz”,
                “englex-dict.gz”,
                “knuth_britsh.gz”,
                “knuth_words.gz”,
                “pocket-dic.gz”,
                “shakesp-glossary.gz”,
                “special.eng.gz”,
                “words-english.gz”,
            ),
        ),
        12: (“dutch”, (“words.dutch.gz”,)),
        13: (
            “finnish”,
            (“finnish.gz”, “firstnames.finnish.gz”, “words.finnish.FAQ.gz”),
        ),
        14: (“french”, (“dico.gz”,)),
        15: (“german”, (“deutsch.dic.gz”, “germanl.gz”, “words.german.gz”)),
        16: (“hindi”, (“hindu-names.gz”,)),
        17: (“hungarian”, (“hungarian.gz”,)),
        18: (“italian”, (“words.italian.gz”,)),
        19: (“japanese”, (“words.japanese.gz”,)),
        20: (“latin”, (“wordlist.aug.gz”,)),
        21: (
            “literature”,
            (
                “LCarrol.gz”,
                “Paradise.Lost.gz”,
                “aeneid.gz”,
                “arthur.gz”,
                “cartoon.gz”,
                “cartoons-olivier.gz”,
                “charlemagne.gz”,
                “fable.gz”,
                “iliad.gz”,
                “myths-legends.gz”,
                “odyssey.gz”,
                “sf.gz”,
                “shakespeare.gz”,
                “tolkien.words.gz”,
            ),
        ),
        22: (“movieTV”, (“Movies.gz”, “Python.gz”, “Trek.gz”)),
        23: (
            “music”,
            (
                “music-classical.gz”,
                “music-country.gz”,
                “music-jazz.gz”,
                “music-other.gz”,
                “music-rock.gz”,
                “music-shows.gz”,
                “rock-groups.gz”,
            ),
        ),
        24: (
            “names”,
            (
                “ASSurnames.gz”,
                “Congress.gz”,
                “Family-Names.gz”,
                “Given-Names.gz”,
                “actor-givenname.gz”,
                “actor-surname.gz”,
                “cis-givenname.gz”,
                “cis-surname.gz”,
                “crl-names.gz”,
                “famous.gz”,
                “fast-names.gz”,
                “female-names-kantr.gz”,
                “female-names.gz”,
                “givennames-ol.gz”,
                “male-names-kantr.gz”,
                “male-names.gz”,
                “movie-characters.gz”,
                “names.french.gz”,
                “names.hp.gz”,
                “other-names.gz”,
                “shakesp-names.gz”,
                “surnames-ol.gz”,
                “surnames.finnish.gz”,
                “usenet-names.gz”,
            ),
        ),
        25: (
            “net”,
            (
                “hosts-txt.gz”,
                “inet-machines.gz”,
                “usenet-loginids.gz”,
                “usenet-machines.gz”,
                “uunet-sites.gz”,
            ),
        ),
        26: (“norwegian”, (“words.norwegian.gz”,)),
        27: (
            “places”,
            (
                “Colleges.gz”,
                “US-counties.gz”,
                “World.factbook.gz”,
                “Zipcodes.gz”,
                “places.gz”,
            ),
        ),
        28: (“polish”, (“words.polish.gz”,)),
        29: (
            “random”,
            (
                “Ethnologue.gz”,
                “abbr.gz”,
                “chars.gz”,
                “dogs.gz”,
                “drugs.gz”,
                “junk.gz”,
                “numbers.gz”,
                “phrases.gz”,
                “sports.gz”,
                “statistics.gz”,
            ),
        ),
        30: (“religion”, (“Koran.gz”, “kjbible.gz”, “norse.gz”)),
        31: (“russian”, (“russian.lst.gz”, “russian_words.koi8.gz”)),
        32: (
            “science”,
            (
                “Acr-diagnosis.gz”,
                “Algae.gz”,
                “Bacteria.gz”,
                “Fungi.gz”,
                “Microalgae.gz”,
                “Viruses.gz”,
                “asteroids.gz”,
                “biology.gz”,
                “tech.gz”,
            ),
        ),
        33: (“spanish”, (“words.spanish.gz”,)),
        34: (“swahili”, (“swahili.gz”,)),
        35: (“swedish”, (“words.swedish.gz”,)),
        36: (“turkish”, (“turkish.dict.gz”,)),
        37: (“yiddish”, (“yiddish.gz”,)),
    }

    # download the files

    Intfiledown = int(filedown)

    If intfiledown in arguments:

        Dire = “dictionaries/” + arguments[intfiledown][0] + “/”
        Mkdir_if_not_exists(dire)
        Files_to_download = arguments[intfiledown][1]

        For fi in files_to_download:
            url = CONFIG[“global”][“dicturl”] + arguments[intfiledown][0] + “/” + fi
            tgt = dire + fi
            download_http(url, tgt)

        print(“[+] files saved to “ + dire)

    else:
        print(“[-] leaving.”)


# create the directory if it doesn’t exist
Def mkdir_if_not_exists(dire):
    If not os.path.isdir(dire):
        Os.mkdir(dire)


# the main function
Def main():
    “””Command-line interface to the cupp utility”””

    Read_config(os.path.join(os.path.dirname(os.path.realpath(__file__)), “cupp.cfg”))

    Parser = get_parser()
    Args = parser.parse_args()

    If not args.quiet:
        Print_cow()

    If args.version:
        Version()
    Elif args.interactive:
        Interactive()
    Elif args.download_wordlist:
        Download_wordlist()
    Elif args.alecto:
        Alectodb_download()
    Elif args.improve:
        Improve_dictionary(args.improve)
    Else:
        Parser.print_help()


# Separate into a function for testing purposes
Def get_parser():
    “””Create and return a parser (argparse.ArgumentParser instance) for main()
    To use”””
    Parser = argparse.ArgumentParser(description=”Common User Passwords Profiler”)
    Group = parser.add_mutually_exclusive_group(required=False)
    Group.add_argument(
        “-I”,
        “—interactive”,
        Action=”store_true”,
        Help=”Interactive questions for user password profiling”,
    )
    Group.add_argument(
        “-w”,
        Dest=”improve”,
        Metavar=”FILENAME”,
        Help=”Use this option to improve existing dictionary,”
        “ or WyD.pl output to make some pwnsauce”,
    )
    Group.add_argument(
        “-l”,
        Dest=”download_wordlist”,
        Action=”store_true”,
        Help=”Download huge wordlists from repository”,
    )
    Group.add_argument(
        “-a”,
        Dest=”alecto”,
        Action=”store_true”,
        Help=”Parse default usernames and passwords directly”
        “ from Alecto DB. Project Alecto uses purified”
        “ databases of Phenoelit and CIRT which were merged”
        “ and enhanced”,
    )
    Group.add_argument(
        “-v”, “—version”, action=”store_true”, help=”Show the version of this program.”
    )
    Parser.add_argument(
        “-q”, “—quiet”, action=”store_true”, help=”Quiet mode (don’t print banner)”
    )

    Return parser

 
If __name__ == “__main__”:
    Main()




