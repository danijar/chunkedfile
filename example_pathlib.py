import time
import pathlib
import chunkedfile

# Path objects opened in append mode will be replaced by chunked files.
chunkedfile.patch_pathlib_append(10)

# Write chunks up to every 60 seconds.
with pathlib.Path('filename.txt').open('a') as f:

  # The first chunk will be written during the sleep command.
  f.write('Lorem\n')
  f.write('Ipsum\n')
  time.sleep(15)

  # The last chunk is automatically written when the file is closed.
  f.write('Dolor\n')
  f.write('Sit\n')

# The directory now contains two files:
# -
# -
