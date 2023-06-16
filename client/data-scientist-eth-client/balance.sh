#!/bin/bash

_submenu()
{
    echo
    echo "Choose among the following:"
    echo "   1) Show balance."
    echo "   2) Withdraw tokens."
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
            _message "SHOWING BALANCE"
            python3 -c 'from utils import balance; balance.balance_printer()'
            _submenu
            ;;
        2)
            clear
            _message "WITHDRAWAL OF TOKENS"
            python3 -c 'from utils import balance; balance.increase_balance()'
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