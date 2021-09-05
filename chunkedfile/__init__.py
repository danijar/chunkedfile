import datetime
import pathlib
import time


class ChunkedFile:

  def __init__(self, path, duration):
    assert duration >= 10
    self.path = path
    self.queue = None
    self.start = None
    self.dur = duration
    self.number = 1

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self._write_chunk()

  def __del__(self):
    try:
      self._write_chunk()
    except Exception:
      pass

  def write(self, text):
    if self.queue is None:
      self.queue = []
      self.start = time.time()
    self.queue.append(text)
    self._maybe_write_chunk()

  def flush(self):
    self._maybe_write_chunk()

  def close(self):
    self._write_chunk()

  def _maybe_write_chunk(self):
    if time.time() >= self.start + self.dur:
      self._write_chunk()

  def _write_chunk(self):
    if not self.queue:
      return
    stamp = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    chunk = ''.join(self.queue)
    pathlib.Path(f'{str(self.path)}-{self.number}-{stamp}').write_text(chunk)
    self.queue = []
    self.start = time.time()
    self.number += 1


def patch_pathlib_append(duration):
  _orig_open = pathlib.PosixPath.open
  def _open(path, mode='r', *args, **kwargs):
    if mode == 'a':
      return ChunkedFile(path, duration)
    return _orig_open(path, mode, *args, **kwargs)
  pathlib.PosixPath.open = _open
