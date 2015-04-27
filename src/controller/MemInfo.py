import subprocess
import re

class MemInfo:
  """
  Stateless Memory Information Utility Class.
  ! May : Instance Method -> Static Method
  """
  mem_re = re.compile("^(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+).*$")

  def __init__(self):
    print "MemInfo Service Started..."


  def get_mem_info(self):
    p = subprocess.Popen(["adb", "shell", "procrank"], stdout=subprocess.PIPE)
    p.wait()
    out, err = p.communicate()

    if err is None:
      new_mem = []
      for line in out.split("\r\n"):
        match = MemInfo.mem_re.match(line.strip())
        if not match is None:
          pid, vss, rss, pss, uss, cmd = match.groups()
          new_mem.append({
            "pid" : pid,
            "pss" : pss,
            "uss" : uss,
            "cmd" : cmd,
          })
      return new_mem
    else:
      print "Error doing procrank..."
      return []


if __name__ == "__main__":
  mi = MemInfo()
  print mi.get_mem_info()
