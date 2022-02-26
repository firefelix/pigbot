
class PigArt:

    sitting_pig = """                 
                     (\____/)  'oink.'
                     / @__@ \\
                    (  (oo)  )
                     `-.~~.-'
                      /    \\
                    @/      \_
                   (/ /    \ \)
                    WW`----'WW"""
    
    big_pig = """                                   
    'Reeeeee'
                                                 __
             ____               ________     ,',.`.
           \`''-.`-._..--...-'''        ```--':_ ) )
            `-.._` '              -..           ' /
     ,'`..__..'' -. _ `._                         \\
    ('';`      _ ,''       .-'            ,'       :
     `-._     `*/     ,                  '      .  |
        _.:._   `-'`-'  ;   \                  ,'  ;
     .':::::'`    ,' \,'     :         ;          /
      `-..__        ,'/      |       ,'         ,'
            ``---;'` \ `     ;.____..-'`.     ,'\\
                /   / \:    :            :   (\ `\\
              ,'  .'   \    :           ;'   / )  )
             /,_,.;::.  `.   \         /   ,',',_(:::.
                          `.  `.     ,'  ;'
                           /,_,'::. `-'`'::.
    """
    @staticmethod
    def get_pig_art():
        return [PigArt.sitting_pig, PigArt.big_pig]

if __name__ == "__main__":
    print(PigArt.big_pig)
    print(PigArt.sitting_pig)