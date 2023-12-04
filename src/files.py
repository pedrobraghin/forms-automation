whitelist_filename='whitelist.txt'
blacklist_filename='blacklist.txt'


def load_users():
  whilelist = []
  blacklist =[]

  with open(blacklist_filename, 'r') as blacklist_file:
      for name in blacklist_file:
        blacklist.append(name.strip())

  with open(whitelist_filename, 'r') as whilelist_file:
    for line in whilelist_file:
      name, gender = line.strip().split(',')

      if name in blacklist:
        continue

      whilelist.append((name, gender))
  
  with open(blacklist_filename, 'a') as blacklist_file:
    for name, _ in whilelist:
      if name in blacklist:
        continue
      
      blacklist_file.write(name + '\n')

  return whilelist
