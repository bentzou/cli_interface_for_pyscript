import inspect
import sys

class CliInterface:
   """
   This class wraps a Python class and provides a CLI interface.

   Assumptions
   - methods beginning with '_' are private and are not shown under Usage.
   - methods are classmethods
   - parent class does not need to be initialized

   Usage
   - At the bottom of the tool script, add:
      import cli_interface
      if __name__ == '__main__':
         cli_interface.CliInterface(PerfPortalTest).run()
   """

   def __init__(self, tool_class):
      self.tool_class = tool_class

   def usage(self):
      print "Usage: {0} command [args...]".format(sys.argv[0])
      print
      print "Available commands and the parameters:"

      for command in sorted(self.tool_class.__dict__.keys()):
         if not command.startswith("_"):
            argspec = inspect.getargspec(getattr(self.tool_class, command))

            if argspec.defaults:
               req_args = argspec.args[1:-len(argspec.defaults)]
               opt_args = argspec.args[-len(argspec.defaults):]
            else:
               req_args = argspec.args[1:]
               opt_args = []

            req_args_str = " ".join(req_args)
            opt_args_str = " ".join(["[" + opt_arg + "]" for opt_arg in opt_args])

            print "   {0:40s} {1} {2}".format(command, req_args_str, opt_args_str)
      print

   def run(self):
      # get arguments
      if len(sys.argv) <= 1:
         self.usage()
         sys.exit(0)
      else:
         command = sys.argv[1]
         arguments = sys.argv[2:]

      try:
         # check if command exists
         if command not in self.tool_class.__dict__:
            raise Exception("{0} is not a valid command\n\n".format(command))
   
         # check if correct # of arguments
         argspec = inspect.getargspec(getattr(self.tool_class, command))
         if argspec.defaults:
            req_args = argspec.args[1:-len(argspec.defaults)]
            opt_args = argspec.args[-len(argspec.defaults):]
         else:
            req_args = argspec.args[1:]
            opt_args = []

         if len(arguments) < len(req_args) or len(arguments) > len(req_args) + len(opt_args):
            raise Exception("Incorrect # of arguments for {0}\n\n".format(command))
      except Exception, e:
         sys.stderr.write(str(e))
         self.usage()
         sys.exit(1)

      # looks good -- run the command
      returncode = getattr(self.tool_class, command)(*arguments)
      sys.exit(returncode)