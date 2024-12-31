
import random as rr
rand = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=[]\';./,)(*&^%$#@!~`)"
try: 
  print('''
  The Choice you can choose
  * Encryption --> 1 *
  * Decryption --> 0 *''')
  choice = int(input("Enter your choice: "))
  match choice:
    case 1  :
      def encry_decry():
        word = input("Enter the text for Encryption: ")
        new_word = word.split(" ")

        for text in new_word:
        # Encryption
          if len(text) >= 3:
            strnew = rr.sample(rand , 3) + list(text[1:]) +list(text[0]) + rr.sample(rand , 3) 
            str = ''.join(strnew)
            print(str ,end=' ')
          else :
            reversed_string = ''.join(reversed(text))
            print(reversed_string,end=' ')
      encry_decry()

    case 0:
      def encry_decry():
        word = input("Enter the text for Decryption: ")
        new_word = word.split(" ")

        for text in new_word:
        # Decryption
          if len(text) >= 3:
            stnew = text[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            newwords = ''.join(stnew)
            print(newwords,end=' ')
          else :
            reversed_string = ''.join(reversed(text))
            print(reversed_string,end=' ')
      encry_decry()

    case _ :
          print("Invalid choice")

except ValueError:
  print("Enter the given choice not a String or Special Character , Please re-run the Program")
    
  