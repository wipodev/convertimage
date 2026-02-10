import sys
from src.convert import convert
from src.resize_ui import start_resize
from src.optimizer_ui import start_optimizer
from src.cut_ui import start_cut
from src.optimizer_engine import start_optimize_files
from src.pack import pack
from src.helper import is_command, show_help

def main() -> None:
  args = [a for a in sys.argv[1:]]
  if not args:
    show_help()
    return  
  command = args[0].lower()

  if is_command(command, "convert"):
    if len(args) < 3:
      show_help()
      return
    convert(args[1], args[2])
    return
  
  if is_command(command, "resize"):
    if len(args) < 2:
      show_help()
      return
    start_resize(args[1])

  if is_command(command, "optimize"):
    if len(args) < 2:
      show_help()
      return
    start_optimizer(args[1])

  if is_command(command, "optimize-default"):
    if len(args) < 2:
      show_help()
      return
    start_optimize_files(args[1:])

  if is_command(command, "cut"):
    if len(args) < 2:
      show_help()
      return
    start_cut(args[1])

  if is_command(command, "svg"):
    if len(args) < 2:
      show_help()
      return
  
  if is_command(command, "pack"):
    if len(args) < 2:
      show_help()
      return
    dll_name = args[2] if len(args) >= 3 else None
    pack(args[1], dll_name)
    return
  
  if is_command(command, "help"):
    show_help()
    return
  
  show_help()

if __name__ == "__main__":
  main()