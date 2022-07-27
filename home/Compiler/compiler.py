import os
import subprocess

def executePython(code, data):
    with open('home\Compiler\Code Files\python.txt','w') as f:
        f.write(code)
    s = subprocess.run('py "home\Compiler\Code Files\python.txt"', stdin = data, shell = True, capture_output = True)

    if s.returncode == 0:
        return {"statusCode" : s.returncode, "output" : s.stdout.decode('utf-8')}
    else:
        return {"statusCode" : s.returncode, "output" : s.stderr.decode('utf-8')}


def executeJava(code, data):
    with open('home\Compiler\Code Files\java.txt','x') as f:
        f.write(code)
        f.close()

    if os.path.exists("home\Compiler\Code Files\java.java"):
      os.remove("home\Compiler\Code Files\java.java")
    if os.path.exists("home\Compiler\Code Files\java.class"):
      os.remove("home\Compiler\Code Files\java.class")

    f = 'home\Compiler\Code Files\java.txt'
    base = os.path.splitext(f)[0]
    os.rename(f, base + '.java')

    subprocess.run('javac "D:\Projects\HugsForBugs\Hugs-for-Bugs-Online-Compiler-main\\backend\home\Compiler\Code Files\java.java"', shell = True)
    s = subprocess.run('java "D:\Projects\HugsForBugs\Hugs-for-Bugs-Online-Compiler-main\\backend\home\Compiler\Code Files\java.java"', stdin = data, shell = True, capture_output = True)

    if s.returncode == 0:
        return {"statusCode" : s.returncode, "output" : s.stdout.decode('utf-8')}
    else:
        return {"statusCode" : s.returncode, "output" : s.stderr.decode('utf-8')}


def executeCpp(code, data):
    with open('home\Compiler\Code Files\c++.txt','x') as f:
        f.write(code)
        f.close()

    if os.path.exists("home\Compiler\Code Files\c++.cpp"):
      os.remove("home\Compiler\Code Files\c++.cpp")
    if os.path.exists("home\Compiler\Code Files\c++.exe"):
      os.remove("home\Compiler\Code Files\c++.exe")

    f = 'home\Compiler\Code Files\c++.txt'
    base = os.path.splitext(f)[0]
    os.rename(f, base + '.cpp')

    a = subprocess.run('g++ "D:\Projects\HugsForBugs\Hugs-for-Bugs-Online-Compiler-main\\backend\home\Compiler\Code Files\c++.cpp" -o "D:\Projects\HugsForBugs\Hugs-for-Bugs-Online-Compiler-main\\backend\home\Compiler\Code Files\c++.exe"', shell = True)
    s = subprocess.run('"D:\Projects\HugsForBugs\Hugs-for-Bugs-Online-Compiler-main\\backend\home\Compiler\Code Files\c++.exe"', stdin = data, shell = True,  capture_output = True)
    
    if s.returncode == 0:
        return {"statusCode" : s.returncode, "output" : s.stdout.decode('utf-8')}
    else:
        return {"statusCode" : s.returncode, "output" : s.stderr.decode('utf-8')}

def run(language, code, inp):
    data, temp = os.pipe()
    os.write(temp, bytes(inp, encoding='utf8'))
    os.close(temp)
    if language == 'Python':
        return executePython(code, data)

    elif language == 'Java':
        return executeJava(code, data)

    elif language == 'C++':
        return executeCpp(code, data)
