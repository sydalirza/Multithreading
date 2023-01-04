import threading

input_string = None

def input_thread():
  global input_string
  try:
    input_string = input("Input a string: ")
    print("Inputted String: " + input_string)
  except Exception as e:
    print("Error:", e)
    input_string = None
def reverse_thread(input_string):
  reverse_string = input_string [::-1]
  print("Reversed String: " + reverse_string)

def capital_thread(input_string):
  capital_string = input_string.upper()
  print("Capital String: " +capital_string)

def shift_thread(input_string):
  shift_string = ""
  for i in input_string:
    shift_string += chr(ord(i) + 2)
  print("Shifted String: " +shift_string)

if __name__ == '__main__':
  
  t1 = threading.Thread(target=input_thread, args=())
 
  t1.start()
  t1.join()
  
  t2 = threading.Thread(target=reverse_thread, args=(input_string,))
  t3 = threading.Thread(target=capital_thread, args=(input_string,))
  t4 = threading.Thread(target=shift_thread, args=(input_string,))

  t2.start()
  t3.start()
  t4.start()
