clear
echo 'Updating ...'
apt update -y > /dev/null
clear
echo 'Upgrading ...'
apt upgrade -y > /dev/null
clear
echo 'Installing python3 & python3-pip'
apt install python3 -y > /dev/null  && apt install python3-pip -y > /dev/null
clear
echo 'finished !'
echo 'Now you can run the tool using "python3 main.py"'