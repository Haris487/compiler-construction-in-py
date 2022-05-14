def read_file(filename):
  with open(filename) as f:
    lines = f.readlines()
    text = ""
    for line in lines:
      text += line
    
    return text

def write_file(filename,text):
  with open(filename, 'w') as f:
    f.write(text)