import time
import chunkedfile

# Write chunks up to every 60 seconds.
f = chunkedfile.ChunkedFile('filename.txt', 10)

# The first chunk will be written on the first write after the sleep.
f.write('Lorem\n')
time.sleep(15)
f.write('Ipsum\n')

# The last chunk is automatically written when the file is closed.
f.write('Dolor\n')
f.write('Sit\n')

# The directory now contains two files:
# -
# -
