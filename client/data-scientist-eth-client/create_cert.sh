#!/bin/bash

path=./ipfs/uploads/test/certs

cd $path

if [ $1 = "" ]
then
  echo "Please, introduce a name for your certificate:"
  read name
else
  name=$1
fi

cd $name

key="$name.key"
csr="$name.csr"
crt="$name.crt"
SUBJ="/CN=$name@example.com"

openssl genrsa -out $key 2048
openssl req -new -key $key -subj $SUBJ -out $csr
openssl x509 -req -days 1000 -set_serial 101$ID -CA RootCA.crt -CAkey RootCA.key -in $csr -out $crt
rm $csr