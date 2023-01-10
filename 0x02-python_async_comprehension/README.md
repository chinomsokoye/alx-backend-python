Curriculum <br>
**Short Specializations** <br>

# 0x02. Python - Async Comprehension

`Python` `Back-end`

**Concepts:**

_For this project, look at these concepts:_

* [Advanced Python](https://www.alx-intranet.hbtn.io/concepts/554)

## Resources

**Read or watch:**

* [PEP 530 - Asynchronous Comprehensions](https://www.peps.python.org/pep-0530/)
* [What's New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
* [Type-hints for generators](https://www.stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)

## General Requirements

* Allowed editors: `vi`, `vim`, `emacs`
* Files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
* First line of file using exactly shebang `#!/usr/bin/env python3`
* Mandatory `README.md` file
* Code use the `pycodestyle` (version 2.5.x)
* File must be executable
* Length of file tested using `wc`
* All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All functions (inside / outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* A documentation explaining purpose of the module or class or method (length will be verified)
* All functions and coroutines must be type-annotated.

## General Learning & Setup

`main.py`
<details>
  <summary>Click to show/hide file contents</summary>

  ```python3
  #!/usr/bin/env python3

  import asyncio
  
  var = __import__('file').var

  async def print_yielded_values():
  	result = []
	async for i in async_generator():
	      result.append(i)
	print(result)

  asyncio.run(print_yielded_values())
  ```
</details>

## Finally...
