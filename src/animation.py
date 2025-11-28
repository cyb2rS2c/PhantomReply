import pyfiglet
from termcolor import colored

def print_ascii_art():
    fig = pyfiglet.Figlet(font='slant')
    repo_name = "PhantomReply"
    ascii_art_repo_name = fig.renderText(repo_name)
    Author = 'cyb2rS2c'
    Description = 'MULTI-ORIGIN TACTICAL DISPATCH SYSTEM'

    eagle = r'''
           ///,        ////
           \  /,      /  >.
            \  /,   _/  /.
             \_  /_/   /.
              \__/_   <
              /<<< \_\_
             /,)^>>_._ \
             (/   \\ /\\\
                  // ````
                 ((`    
    '''
    print(colored(ascii_art_repo_name, 'green', attrs=['bold']))
    print(colored(eagle, 'yellow'))
    print(colored(f'{Description}', 'red', attrs=['bold', 'underline']))
    print(colored('Author: ', 'white', attrs=['bold']) + colored(f'{Author}', 'cyan', attrs=['bold']))
