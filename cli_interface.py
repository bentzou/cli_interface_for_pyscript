from inspect import getargspec
from inspect import getdoc
from json import dumps
import sys

class CliInterface(object):
   def __init__(self, tool_class):
      self.tool_class = tool_class
      self.commands = sorted(self.tool_class.__dict__.keys() + ["help"])

   def usage(self):
      print "Usage: {0} command [args...]".format(sys.argv[0])
      print
      print "Available commands and the parameters:"

      for command in self.commands:
         if command.startswith("_"):
            pass
         elif command == "help":
            print "   {0:40s} {1}".format("help", "[command]")
         else:
            argspec = getargspec(getattr(self.tool_class, command))

            if argspec.defaults:
               req_args = argspec.args[1:-len(argspec.defaults)]
               opt_args = argspec.args[-len(argspec.defaults):]
            else:
               req_args = argspec.args[1:]
               opt_args = []

            req_args_str = " " + " ".join(req_args) if req_args else ""
            opt_args_str = " " + " ".join(["[" + opt_arg + "]" for opt_arg in opt_args])

            print "   {0:40s}{1}{2}".format(command, req_args_str, opt_args_str)

   def print_command_help(self, command=None):
      # check correct help usage
      if command is list and len(command) > 1:
         raise Exception("Incorrect # of arguments for help\n".format(command))

      # print usage
      if not command:
         self.usage()
      elif command in self.tool_class.__dict__:
         print getdoc(getattr(self.tool_class, command))
      else:
         raise Exception("{0} is not a valid command\n".format(command))

   def run_command(self, command, arguments):
      # get argspec
      argspec = getargspec(getattr(self.tool_class, command))

      if argspec.defaults:
         req_args = argspec.args[1:-len(argspec.defaults)]
         opt_args = argspec.args[-len(argspec.defaults):]
      else:
         req_args = argspec.args[1:]
         opt_args = []

      # check if correct # of arguments
      if len(arguments) < len(req_args) or len(arguments) > len(req_args) + len(opt_args):
         raise Exception("Incorrect # of arguments for {0}\n".format(command))

      return getattr(self.tool_class, command)(*arguments)

   def run(self):
      # get arguments
      if len(sys.argv) <= 1:
         self.usage()
         sys.exit(0)
      else:
         command = sys.argv[1]
         arguments = sys.argv[2:]
   
      # check if command exists
      if command != "help" and command not in self.tool_class.__dict__:
         sys.stderr.write("{0} is not a valid command\n\n".format(command))
         self.usage()
         sys.exit(1)

      # run the command
      try:
         if command == "help":
            self.print_command_help(arguments[0] if arguments else None)
         else:
            return_value = self.run_command(command, arguments)
            if return_value:
               print dumps(return_value)
      except Exception, e:
         sys.stderr.write(str(e))
         sys.exit(1)
