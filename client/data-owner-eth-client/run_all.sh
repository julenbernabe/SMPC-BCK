#!/bin/bash

# Muestra el menu general
_menu()
{
    echo
    echo "Which step want to run"
    echo "  1) Start"
    echo "  2) Show balance"
    echo "  3) Show reputation"
    echo
    echo "  0) Exit"
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
 
# opcion por defecto
opc="100"
player=""
 
# bucle mientas la opcion indicada sea diferente de 0 (salir)
until [ "$opc" -eq "0" ];
do
    case $opc in
        1)
            clear
            python3 events_consumer.py
            _menu
            ;;
        2)
            clear
            _message "SHOW BALANCE"
            python3 -c 'from utils import balance; balance.my_balance()'
            _menu
            ;;
        3)
            clear
            _message "SHOW REPUTATION"
            python3 -c 'from utils import balance; balance.my_reputation()'
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
