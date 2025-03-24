#!/usr/bin/python3
import sys
import os

def find_directory(directory, dry_run=False):
  # default_path = os.path.abspath(os.sep)
  EXCLUDED_DIRS = [
    "/bin", "/boot", "/dev", "/etc", "/lib", "/proc", "/sys", "/usr", "/var",
    "C:\\Windows", "C:\\Program Files", "C:\\Program Files (x86)", "C:\\Users\\Public", "C:\\$Recycle.Bin"
  ]
  
  for root, dir, files in os.walk(directory):
    if any(excluded in root for excluded in EXCLUDED_DIRS):
      continue
    
    print(f"Root: {os.path.basename(root)}\nFull Path: {root}\nDirectories: {dir}\nFiles: {files}\n")

def find_file(target_file, start_directory=os.path.abspath(os.sep)):
  for root, dir, files in os.walk(start_directory):
    if target_file in files:
      print(f"File located at path: {root}")
      return
  print("File not found")
  return

if __name__ == "__main__":
  arguments = sys.argv
  default_path = os.path.abspath(os.sep)
  if len(arguments) < 2:
    print("Usage: python indigo_organizer.py <directory>")
  else:
    # find_directory(arguments[1])
    find_file(arguments[2], arguments[1])