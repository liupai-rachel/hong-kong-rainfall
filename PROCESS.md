# Process

## AI Tools

I mainly used ‘ChatGPT’ to brainstorm the visualisation idea, generate Python/Matplotlib code, and debug errors.

I kept ChatGPT because it helped me turn my visual idea into working code and explain programming concepts that I did not understand.

However, I did not use the generated code without checking it. For example, ChatGPT initially suggested using `get_cmap`, which caused an import error in my environment. I checked the error and changed it to `colormaps`, after which the code worked.

I also checked the CSV structure by printing the first row, one value, and its data type instead of assuming the AI's interpretation was correct.

I rejected ‘pandas’ because the data processing was simple enough to use Python's built-in `csv` module. Using pandas would add an unnecessary dependency.

This process showed me that AI can generate code quickly, but I still need to test, understand, and correct its output.