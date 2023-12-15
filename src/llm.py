# Load LLM model
from llama_cpp import Llama


MODELS_FOLDER = f'./models'

# MODEL = f'{MODELS_FOLDER}/openhermes-2.5-mistral-7b.Q5_K_M.gguf'
MODEL = f'{MODELS_FOLDER}/codellama-13b-instruct.Q5_K_M.gguf'

llm_model = Llama(model_path=MODEL, n_ctx=4096, verbose=False)

# Prompt for creating requested python code.
def generate_code(user_prompt: str) -> str:
  formatted_prompt = f"""# Description
A python file with a single function that performs the following action:
{user_prompt}

The main function is called "generated_function" which takes no arguments.
Only standard python libraries are used and all relevant imports are present.
The code is complete and ready to be executed.

The code starts and ends denoted by ```.

# Code
```
"""

  output = llm_model(prompt=formatted_prompt, stop=["```"], max_tokens=4096)
  output_code = output["choices"][0]["text"]
  return output_code