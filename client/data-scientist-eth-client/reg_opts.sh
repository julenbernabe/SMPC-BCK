#!/bin/bash

_submenu()
{
    echo
    echo "Choose among the following:"
    echo "   1) New campaign."
    echo "   2) Enter working campaign."
    echo "   3) Reuse finished campaign."
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
            _message "POSTING A NEW CAMPAIGN IN ETHEREUM"
            python3 -c 'from src import campaign; campaign.new()'
            _submenu
            ;;
        2)
            clear
            _message "ENTERING ONE OF YOUR CAMPAIGNS"
            python3 -c 'from src import campaign; campaign.working()'
            _submenu
            ;;
        3)
            clear
            _message "REUSING A FINISHED CAMPAIGN"
            python3 -c 'from src import campaign; campaign.reuse()'
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