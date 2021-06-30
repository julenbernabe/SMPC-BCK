#!/bin/bash

# Muestra el menu general
_menu()
{
    echo
    echo "Which step want to run"
    echo "  1) Create Ethereum Account"
    echo "  2) Start"
    echo "  3) Balance"
    echo
    echo "  0) Exit"
    echo
    echo -n "Choose a number: "
}
 
# Muestra la opcion seleccionada del menu
_message()
{
    echo ""
    echo "###################################"
    echo "$1"
    echo "###################################"
    echo ""
}
 
# opcion por defecto
opc="100"
player=""
 
# bucle mientas la opcion indicada sea diferente de 0 (salir)
until [ "$opc" -eq "0" ];
do
    case $opc in
        1)  
            clear
            _message "CREATING ETH ACCOUNT"
            python3 -c 'from utils import wallet; wallet.createAccount()'
            _message "ETH ACCOUNT READY"
            _menu
            ;;
        2)
            clear
            _message "START REQUEST"
            ./reg_opts.sh
            _message "OPERATION FINISHED"
            _menu
            ;;
        3)
            clear
            _message "BALANCE"
            ./balance.sh
            _menu
            ;;
        *)
            # Esta opcion se ejecuta si no es ninguna de las anteriores
            clear
            _menu
            ;;
    esac
    read opc
done
