from test2 import displaytext

def main():
  print('i\'m from test1')
  print('this is the function __name__ in test1', repr(__name__))
  displaytext()
  print('this is the function __name__ in test1', repr(__name__))


if __name__ == '__main__':
  main()