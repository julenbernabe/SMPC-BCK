#!/bin/bash

_submenu()
{
    echo
    echo "Choose among the following:"
    echo "   1) New request."
    echo "   2) Update request."
    echo "   3) Enter working request."
    echo
    echo "   0) Back"
    echo
    echo -n "Choose a number: "
}

# Muestra la opcion seleccionada del menu
_message()
{
    clear
    echo ""
    echo "###################################"
    echo "$1"
    echo "###################################"
    echo ""
}

opc="100"
until [ "$opc" -eq "0" ];
do
    case $opc in
        1)
            clear
            _message "POSTING A NEW REQUEST IN ETHEREUM"
            cd ../Programs
            ls
            cd ../client
            python3 -c 'from src import requests; requests.new()'
            _submenu
            ;;
        2)
            clear
            _message "UPDATING AN OLD REQUEST"
            cd ../Programs
            ls
            cd ../client
            python3 -c 'from src import requests; requests.update()'
            _submenu
            ;;
        3)
            clear
            _message "ENTERING ONE OF YOUR REQUESTS"
            cd ../Programs
            ls
            cd ../client
            python3 -c 'from src import enter_request; enter_request.main()'
            _submenu
            ;;
        *)
            # Esta opcion se ejecuta si no es ninguna de las anteriores
            clear
            _submenu
            ;;
    esac
    read opc
done
clear