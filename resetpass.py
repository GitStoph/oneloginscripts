#!/usr/bin/env python3
# GitStoph
#########################################################
import os, sys
from rich import pretty, print
from rich.console import Console
from onelogin.api.client import OneLoginClient
from dotenv import load_dotenv
import random
import string

pretty.install()
console = Console()

#os.chdir('/opt/oneloginscripts')
"""Uncomment this line if you install to /opt, then want to add
 the script to your bin to run from."""
fpath = os.getcwd()
sys.path.append(fpath)
load_dotenv(os.path.join(fpath, '.env'))

# Gotta initiate the OneLoginClient object.
client = OneLoginClient(
    os.getenv('CLIENT_ID'), 
    os.getenv('CLIENT_SECRET'),
    'us'
)

def randompassword():
    """This creates a random 50-60 char password."""
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(50, 60)
    return ''.join(random.choice(chars) for x in range(size))


def find_user(query):
    """Searches for the user by samaccountname."""
    search = {'samaccountname': query}
    try:
        return client.get_users(search)[0].__dict__
    except:
        console.log("[red]Error: "+str(sys.exc_info()))


def reset_pass(userid):
    """Creates the random password, then sets it on the userid
    that was pass to the function. If desired, you could additionally
    pass the "newpass" variable to manually set passwords with an arg
    passed when running the script."""
    newpass = randompassword()
    result = client.set_password_using_clear_text(userid, newpass, newpass)
    return result


if len(sys.argv) <= 1:
    console.print("[green]Usage: resetpass.py comma,separated,users")
    console.print("[green]Users will have their passwords reset at random to 50-60 alphanumerics.")
    exit()
if len(sys.argv) > 2:
    console.print("[red]Too many args passed. Review usage.")
    exit()
users = sys.argv[1].split(',')
console.print("[yellow]{0} will have their passwords reset.".format(str(users)))
for u in users:
    reset_pass(find_user(u)['id'])
    console.print("[green]{0} has been reset.".format(u['samaccountname']))