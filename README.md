# ChunkedFile

A file handle that groups subsequence writes together and periodically writes
them as separate files. Useful for file systems like GCS FUSE that do not
support file appending. Pathlib can be patched to replace files opened in
append mode with chunked files, so external libraries need not be changed.

## Usage

Using `ChunkedFile`:

```python
import time
import chunkedfile

# Write chunks up to every 10 minutes.
with chunkedfile.ChunkedFile('filename.txt', 600) as f:

  # The first chunk will be written on the first write after the sleep.
  f.write('Lorem\n')
  time.sleep(1000)
  f.write('Ipsum\n')

  # The last chunk is automatically written when the file is closed.
  f.write('Dolor\n')
  f.write('Sit\n')

# The directory now contains two files:
# - filename.txt-1-20210904T130400
# - filename.txt-2-20210904T132100
```

Using `pathlib.Path`:

```python
import time
import pathlib
import chunkedfile

# Path objects opened in append mode will be replaced by chunked files.
chunkedfile.patch_pathlib_append(600)

# Write chunks up to every 10 minutes.
with pathlib.Path('filename.txt').open('a') as f:

  # The first chunk will be written during the sleep command.
  f.write('Lorem\n')
  f.write('Ipsum\n')
  time.sleep(1000)

  # The last chunk is automatically written when the file is closed.
  f.write('Dolor\n')
  f.write('Sit\n')

# The directory now contains two files:
# - filename.txt-1-20210904T130400
# - filename.txt-2-20210904T132100
```
