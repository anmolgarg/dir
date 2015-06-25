echo "updating bash"

# create .bash_profile backup
scp ~/.bash_profile ~/.bash_profile_backup

# get the z script
curl -k https://raw.githubusercontent.com/rupa/z/master/z.sh -o ~/z.sh

# copy bash_profile to root
scp bash_profile ~/.bash_profile


 
check_if_line_exists()
{
    grep -qsFx "$LINE_TO_ADD" ~/.bash_profile
}
 
add_line_to_profile()
{
    printf "%s\n\n" "$LINE_TO_ADD" >> ~/.bash_profile
}

echo "Please enter your desired default startup directory: i.e. ~/Documents"
read LOC
LINE_TO_ADD="cd $LOC"
check_if_line_exists || add_line_to_profile

source ~/.bash_profile