# Hello!
Hello ***hackers*** and ***pentesters***, this tool will really help you during your pen tests and it will be helpful to have on your tool belt! 

# WebHunter
WebHunter Project. Directory Busting made easy!


# For legal use
***Please dont use it for any illegal purposes. I will not be responsible for the damage you may cause.***

# Made for Linux, partially work for windows. Windows version will be launched soon.
I am working for the windows version and many other features too! Please wait and I will soon add more features. Will be fixed soon :)

# Requirements
- [x] Python 2 or python 3 
- [x] Linux OS (windows version coming soon)

# Usage
WebHunter makes directory busting and sub-domain hunting easy. Its very easy to use. 

First give execution permission to the file setup.sh by running `chmod 777 setup.sh`
Then run the setup.sh file using this command: `./setup.sh`

If you face any error while running the setup.sh file, run these commands manually:
`sudo apt update`
`sudo apt-get update`
`sudo apt-get install python-pip`
`pip install colorama`
`pip install pyfiglet`
`pip3 install pyfiglet`

I have include two wordlists. One for subdomain and one for directories. You can use any worlist you like. 
    i) Directory wordlist: files-and-dirs-wordlist.txt
    ii) Subdomain wordlist: subdomains-wordlist.txt
  
Now once you have done the above steps, run the tool using the command: `python webhunter.py`

Now use it, its very easy to use :)
This is a wordlist attack. The speed of completion will depend upon the ***length of the wordlist*** and ***your internet speed.***

# Facing Issues?
Just post them in the issues tab here: https://github.com/jyotisko/WebHunter/issues. If I did not reply within 72hours, mail me here: jyotisko2006@gmail.com

# Updates!
### 1. Now works with both python versions! (python 2 qnd python 3) 

### 2. Exception handlings improved to allow user understand what's going wrong
