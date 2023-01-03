import threading

# Global variable to store the input string
input_string = None

def input_thread():
  global input_string
  input_string = input("Input a string: ")

def reverse_thread(input_string):
  reverse_string = input_string [::-1]
  print(reverse_string)

def capital_thread(input_string):
  capital_string = input_string.upper()
  print(capital_string)

def shift_thread(input_string):
  shift_string = ""
  for i in input_string:
    shift_string += chr(ord(i) + 2)
  print(shift_string)

if __name__ == '__main__':
  # Create the threads
  t1 = threading.Thread(target=input_thread, args=())
 
  # Start the input thread
  t1.start()
  t1.join()

  # Start the other threads with the input string as an argument
  t2 = threading.Thread(target=reverse_thread, args=(input_string,))
  t3 = threading.Thread(target=capital_thread, args=(input_string,))
  t4 = threading.Thread(target=shift_thread, args=(input_string,))

  t2.start()
  t3.start()
  t4.start()