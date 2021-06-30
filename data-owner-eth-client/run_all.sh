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
 
# opcion por defecto
opc="100"
player=""
 
# bucle mientas la opcion indicada sea diferente de 0 (salir)
until [ "$opc" -eq "0" ];
do
    case $opc in
        1)  
            clear
            python3 -c 'from utils import wallet; wallet.createAccount()'
            _menu
            ;;
        2)
            clear
            python3 events_consumer.py
            echo ""
            echo "###################################"
            echo "OPERATION FINISHED"
            echo "###################################"
            echo ""
            _menu
            ;;
        3)
            clear
            echo ""
            echo "###################################"
            echo "BALANCE"
            echo "###################################"
            echo ""
            python3 -c 'from utils import balance; balance.my_balance()'
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
