#!/usr/bin/python3
import sys
import os

EXCLUDED_DIRS = [
  "/bin", "/boot", "/dev", "/etc", "/lib", "/proc", "/sys", "/usr", "/var",
  "C:\\Windows", "C:\\Program Files", "C:\\Program Files (x86)", "C:\\Users\\Public", "C:\$Recycle.Bin"
]

def find_directory(directory, dry_run=False):
  # default_path = os.path.abspath(os.sep)
  
  for root, dir, files in os.walk(directory):
    if any(excluded in root for excluded in EXCLUDED_DIRS):
      continue
    print(f"Root: {os.path.basename(root)}\nFull Path: {root}\nDirectories: {dir}\nFiles: {files}\n")

if __name__ == "__main__":
  arguments = sys.argv
  default_path = os.path.abspath(os.sep)
  if len(arguments) < 2:
    print("Usage: python indigo_organizer.py <directory>")
  else:
    find_directory(arguments[1])