import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

print('Enter the message to display with the bitmap')
message = input('> ').rstrip()

if message == '':
    sys.exit()

#Loop over each line in the bitmap
for line in bitmap.splitlines():
    #Loop over each character in the line
    for i, bit in enumerate(line):
        if bit == ' ':
            #Print an empty space sice thre a space in the  bitmap
            print(' ', end='')
        else:
            #Print  character fromo the message
            print(message[i % len(message)], end='')

    print() #Print a newline
