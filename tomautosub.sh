URL=codegolf.hostbin.org/submit.php



#if [ $# -ne 1 ]; then

#       echo "Usage: $0 <file.c>"

#       exit 0;

#elif [ ! -f $1 ]; then

#       echo "Cant read $1"

#       exit 0;

#fi

USER=$*

#echo $USER

#read -p "Username: " USER



curl "$URL" --form "user=$USER" --form "code=@tomanchor.c"
