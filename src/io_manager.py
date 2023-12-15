GENERATED_CODE_PATH = './src/generated/__init__.py'

def write_code(code: str):
  with open(GENERATED_CODE_PATH, "w") as f:
      f.write(code)
