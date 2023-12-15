from io_manager import write_code
from llm import generate_code
import argparse

EXAMPLE_COMMAND = "Print all prime numbers from 1 to 1000 for me."

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--command", help="Your command to the AGI", default=EXAMPLE_COMMAND)

def main(command: str):
  generated_code = generate_code(command)

  write_code(generated_code)

  user_confirmation = input("Be sure to inspect any generated code. Continue? ")

  if not user_confirmation.lower() in ["y", "yes"]:
    return
  
  from generated import generated_function

  output = generated_function()
  print(output)

if __name__ == "__main__":
  args = parser.parse_args()

  main(args.command)
