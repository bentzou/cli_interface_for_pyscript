class Toolset:
   @classmethod
   def tool_method_no_args(cls):
      pass

   @classmethod
   def tool_method_positional_args(cls, pos_arg1, pos_arg2):
      pass

   @classmethod
   def tool_method_keyword_args(cls, kw_arg1="default1", kw_arg2="default2"):
      pass

   @classmethod
   def tool_method_keyword_args(cls, pos_arg1, pos_arg2, kw_arg1="default1", kw_arg2="default2"):
      pass

if __name__ == '__main__':
   import cli_interface
   cli_interface.CliInterface(Toolset).run()
