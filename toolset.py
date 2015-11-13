class Toolset:
   @classmethod
   def tool_method_no_args(cls):
      """
      This method tool_method_no_args has no args.
      """
      print "tool_method_no_args"

   @classmethod
   def tool_method_positional_args(cls, pos_arg1, pos_arg2):
      """
      This method has positional args (pos_arg1, pos_arg2).
      """
      print "tool_method_positional_args"

   @classmethod
   def tool_method_keyword_args(cls, kw_arg1="default1", kw_arg2="default2"):
      """
      This method has keyword args (kw_arg1, kw_arg2).
      """
      print "tool_method_keyword_args"

   @classmethod
   def tool_method_positional_and_keyword_args(cls, pos_arg1, pos_arg2, kw_arg1="default1", kw_arg2="default2"):
      """
      This method has positional args (pos_arg1, pos_arg2) and keyword args (kw_arg1, kw_arg2).
      """
      print "tool_method_positional_and_keyword_args"

if __name__ == '__main__':
   import cli_interface
   cli_interface.CliInterface(Toolset).run()
