#!/bin/bash
clear
echo "
██╗    ██╗██╗███████╗██╗███████╗██╗  ██╗██╗   ██╗
██║    ██║██║██╔════╝██║██╔════╝██║ ██╔╝╚██╗ ██╔╝
██║ █╗ ██║██║█████╗  ██║███████╗█████╔╝  ╚████╔╝ 
██║███╗██║██║██╔══╝  ██║╚════██║██╔═██╗   ╚██╔╝  
╚███╔███╔╝██║██║     ██║███████║██║  ██╗   ██║   
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
                                                  
▀▀█▀▀ █▀▀█ █▀▀█ █   █▀▀ ~Instaler By Ⓜ Ⓐ Ⓝ Ⓘ Ⓢ Ⓢ Ⓞ  ☪ ~
  █   █  █ █  █ █   ▀▀█ 
  ▀   ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀             

                                                ";

echo "[✔] Checking directories...";
if [ -d "/usr/share/doc/wifisky" ] ;
then
echo "[◉] A directory wifisky was found! Do you want to replace it? [Y/n]:" ; 
read mama
if [ $mama == "y" ] ; 
then
 rm -R "/usr/share/doc/wifisky"
else
 exit
fi
fi

 echo "[✔] Installing ...";
 echo "";
 git clone https://github.com/Manisso/wifisky.git /usr/share/doc/wifisky;
 echo "#!/bin/bash 
 python /usr/share/doc/wifisky/wifisky.py" '${1+"$@"}' > wifisky;
 chmod +x wifisky;
 sudo cp wifisky /usr/bin/;
 rm wifisky;


if [ -d "/usr/share/doc/wifisky" ] ;
then
echo "";
echo "[✔]Tool istalled with success![✔]";
echo "";
  echo "[✔]====================================================================[✔]";
  echo "[✔] ✔✔✔  All is done!! You can execute tool by typing wifisky  !   ✔✔✔ [✔]"; 
  echo "[✔]====================================================================[✔]";
  echo "";
else
  echo "[✘] Installation faid![✘] ";
  exit
fi
