from enum import Enum

COMMENT_NUM = 143
STRING_VALUE_NUM = 144
VARIABLE_NUM = 145
NUMBER_NUM = 146
SPACE_NUM = 147
NEXT_LINE_NUM = 149
code_numbers = Enum('code_numbers', '''+ - * / := : = < > . ( ) [ ] { } ; \' \" $ @ #
                            & ^ _ ~ % and end nil set array file not then 
                            begin for of to case function For While
                            or type const goto packed until div if
                            procedure var do integer in program while downto label record
                            with else mod repeat writeln Writeln maxlongint maxint read real
                            boolean char string Byte ShortInt Word Comp Integer LongInt Real
                            Single Double Extended Boolean Char Array String Record Set Text
                            File >= <= xor true false sin cos arctan abs
                            ln exp sqr sqrt pi round trunc frac random odd
                            ord chr pred succ readln write Assign Reset ReWrite Append
                            Close ReadLn Read WriteLn Write ,''', start=1)
