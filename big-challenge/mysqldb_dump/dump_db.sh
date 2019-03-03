#!/bin/bash

if [ $# = 0 ]
  then
    echo "No environment selected. e.g, staging/dev/dev2/dev3"
    exit 1
fi

ENV=$1
SOURCE_HOST=127.0.0.1
SOURCE_USER=root
SOURCE_PASSWD=PASSWORD
TARGET_HOST=127.0.0.1
TARGET_USER=root
TARGET_PASSWD=PASSWORD

declare -a databases=(yolar)

for db in "${databases[@]}"
do
    DUMP_FILE=${db}_localhost_dump.sql
    SOURCE_DB=${db}_localhost
    TARGET_DB=${db}_${ENV}


    # Dump data
    printf "> Dumping $db to $DUMP_FILE ... "
    # mysqldump --host=$SOURCE_HOST --user=$SOURCE_USER --password=$SOURCE_PASSWD --single-transaction --set-gtid-purged=OFF $SOURCE_DB > $DUMP_FILE
    mysqldump --opt -u $SOURCE_USER -p $SOURCE_DB > $DUMP_FILE
    printf "Finished\n"

    #Restore from dumps
    printf "> Restore $db from $DUMP_FILE ... "
    # mysql --host=$TARGET_HOST --user=$TARGET_USER --password=$TARGET_PASSWD $TARGET_DB < $DUMP_FILE
    mysql -u $TARGET_USER -p $TARGET_DB < $DUMP_FILE
    printf "Finished\n"
done

if [ $ENV = dev ]
    then
        ENV=Develop
fi

if [ $ENV = dev2 ]
    then
        ENV=Develop2
fi

if [ $ENV = dev3 ]
    then
        ENV=Develop3
fi

if [ $ENV = dev4 ]
    then
        ENV=Develop4
fi

if [ $ENV = dev5 ]
    then
        ENV=Develop5
fi

python3 -m test.py $ENV