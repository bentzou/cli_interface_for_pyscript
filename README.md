## cli_interface_for_pyscript
The class provides a CLI interface for an existing toolset written in Python.

#### Contract
1. Methods beginning with '_' are considered private and not displayed under Usage.
2. Tool class contains exclusively classmethods.

#### Usage
At the bottom of your script, add:
```python
if __name__ == '__main__':
   import cli_interface
   cli_interface.CliInterface(Toolset).run()
```

#### Example
```python
class Toolset:
   @classmethod
   def tool_method_no_args(cls):
      pass

   @classmethod
   def tool_method_positional_args(cls, pos_arg1, pos_arg2):
      pass

   @classmethod
   def tool_method_keyword_args(cls, kw_arg1, kw_arg2):
      pass

   @classmethod
   def tool_method_keyword_args(cls, pos_arg1, pos_arg2, kw_arg1, kw_arg2):
      pass

if __name__ == '__main__':
   import cli_interface
   cli_interface.CliInterface(Toolset).run()
```

#### Output
```
$> python toolset.py
Usage: toolset.py command [args...]

Available commands and the parameters:
   tool_method_keyword_args                 pos_arg1 pos_arg2 [kw_arg1] [kw_arg2]
   tool_method_no_args
   tool_method_positional_args              pos_arg1 pos_arg2
```
