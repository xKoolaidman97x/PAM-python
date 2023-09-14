etimo=/opt/PAM
tanke=$etimo/bin
cara=$etimo/
cascara=/usr/local/bin/PAM
DB=$tanke/shell
if ! [ -e $etimo ] ; 
then
echo 'PAM not found.'
#read -p 'Would you like to install? [Y/n]: ' query
#if [[ $query == 'y' || $query == 'Y' ]]
then sudo mkdir $etimo
ls -l | awk '{ print $9 }' > tmp.fil 
while read -r line
do cp -rv ./$line $etimo/
done < tmp.fil 
sudo echo "python3 $cara" > $cascara
#else echo 'Exiting..'
#exit 1
#fi
fi
