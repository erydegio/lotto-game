from lotto.lotto import Lotto
from lotto.printer import Printer

def main():

    def start_game():
        # Ticket creation
        tot_bills = Lotto.arg_parser()
        Lotto.tk_creation(tot_bills)
        Printer.print_all_tickets()

        # Extraction
        Lotto.make_extraction()
        Printer.print_extraction(Lotto.extraction)
        Lotto.define_tk_victory()
        
        # Calculate prizes
        Lotto.add_prize()
        Printer.print_winning_tickets()

    start_game()
    
    
if __name__ == '__main__':
   main()
    

