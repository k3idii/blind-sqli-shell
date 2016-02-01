import argparse
import rlcompleter, readline
readline.parse_and_bind('tab:complete')



def main():
  while True:
    l = raw_input("TEST")
    if 'q' in l:
      return 

  pass





if __name__ == '__main__':
  main()

