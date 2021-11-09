from Domain.aeroport import create_aeroport
from Tests.run_all_tests import run_all_tests
from User_Interface.command_line_console import consola_noua
from User_Interface.consola import consola


def main():
    run_all_tests()
    aeroport=create_aeroport()
    consola(aeroport)

if __name__ == '__main__':
    main()