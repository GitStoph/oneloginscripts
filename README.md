# Onelogin scripts 
Only ended up needing to use one of these, so that's all we're sharing here today. This script uses the onelogin-python-sdk to reset users' passwords. As many as you'd like, as long as they're comma separated. 

A use-case could be, if your company can reset user passwords with Onelogin, it could be used for one-off's by the Helpdesk. Or if you work security and 20 people clicked a phishing link and are suspected to have given up their credentials, you can reset all 20 at the same time.

Use common sense. If you nuke someone's password and get in trouble, that's on you. I take no responsibility for resume generating events. 

# Installation
```
#Clone, then cd into the clone directory.
#If using a venv# Also, you should be using a venv. Don't be a barbarian.
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
#If using system-wide tools#
umask 022
python3 -m pip install --upgrade -r requirements.txt
```

# Usage
`resetpass.py username1,username2,username3`