#speaking with cmd using python lab 
import os
os.system("echo hello terminal")
print("--------------------------------------------------------------")
os.system("echo  ls list iles and directories")
y=os.popen("ls") 
y=y.read()
print(y)
print("--------------------------------------------------------------")
os.system("echo  cd To navigate through the Linux files and directories ")
a=os.popen("cd") 
a=a.read()
print(a)

print("--------------------------------------------------------------")
os.system("echo  cat It lists, combines, and writes file content to the standard output.")
b=os.popen("cat testfile.txt") 
b=b.read()
print(b)

print("--------------------------------------------------------------")
os.system("echo  cp Use the cp command to copy files or directories and their content")
c=os.popen("cp testfile.txt") 
c=c.read()
print(c)

print("--------------------------------------------------------------")
os.system("echo  mv is to move and rename files and directories. Additionally, it doesn’t produce an output upon execution.")
d=os.popen("mv which.txt") 
d=d.read()
print(d)

print("--------------------------------------------------------------")
os.system("echo  mkdir command to create one or multiple directories at once and set permissions for each of them")
e=os.popen("mkdir Music/Songs") 
e=e.read()
print(e)

print("--------------------------------------------------------------")
os.system("echo  To permanently delete an empty directory, use the rmdir command. ")
f=os.popen("rmdir") 
f=f.read()
print(f)

print("--------------------------------------------------------------")
os.system("echo  rm command is used to delete files within a directory i tested once lol")
g=os.popen("rm which.txt") 
g=g.read()
print(g)

print("--------------------------------------------------------------\n")
os.system("echo  touch command allows you to create an empty file or generate and modify a timestamp in the Linux command line.")
h=os.popen("touch /home/username/Documents/Web.html") 
h=h.read()
print(h)

print("--------------------------------------------------------------\n")
os.system("echo locate command can find a file in the database system")
i=os.popen("locate -i comm*not") 
i=i.read()
print(i)

print("--------------------------------------------------------------\n")
os.system("echo  find command to search for files within a specific directory and perform subsequent operations.")
j=os.popen("find /home me.c") 
j=j.read()
print(j)

print("--------------------------------------------------------------\n")
os.system("echo  grep or global regular expression print. It lets you find a word by searching through all the texts in a specific file.")
k=os.popen("grep test testfile.txt") 
k=k.read()
print(k)

print("--------------------------------------------------------------")
os.system("echo  df command to report the system’s disk space usage, shown in percentage and kilobyte (KB).")
l=os.popen("df-h ") 
l=l.read()
print(l)

print("--------------------------------------------------------------")
os.system("echo  du command If you want to check how much space a file or a directory takes up.")
m=os.popen("du /home/Documents") 
m=m.read()
print(m)

print("--------------------------------------------------------------")
os.system("echo head command allows you to view the first ten lines of a text. Adding an option lets you change the number of lines shown. ")
n=os.popen("head -n 2 testfile.txt") 
n=n.read()
print(n)

print("--------------------------------------------------------------")
os.system("echo   tail command displays the last ten lines of a file. It allows users to check whether a file has new data or to read error messages.")
nr=os.popen("tail -n commands.txt ") 
nr=nr.read()
print(nr)

print("--------------------------------------------------------------")
os.system("echo  diff command compares two contents of a file line by line. After analyzing them, it will display the parts that do not match.")
o=os.popen("diff testfile.txt test2.txt") 
o=o.read()
print(o)

print("--------------------------------------------------------------\n")
os.system("echo tar command archives multiple files into a TAR file – a common Linux format similar to ZIP, with optional compression.the follwing command will creat a new tar document")
p=os.popen("tar -cvf newarchive.tar /home/Desktop") 
p=p.read()
print(p)

print("--------------------------------------------------------------\n")
os.system("echo  chmod is a common command that modifies a file or directory’s read, write, and execute permissions.")
q=os.popen("chmod 777 test2.txt") 
q=q.read()
print(q)

print("--------------------------------------------------------------\n")
os.system("echo chown command lets you change the ownership of a file, directory, or symbolic link to a specified username.")
r=os.popen("chown memo test2.txt") 
r=r.read()
print(r)

print("--------------------------------------------------------------")
os.system("echo  jobs command will display all the running processes along with their statuses. Remember that this command is only available in csh, bash, tcsh, and ksh shells.")
s=os.popen("jobs -l") 
s=s.read()
print(s)

print("--------------------------------------------------------------")
os.system("echo kill command to terminate an unresponsive program manually. It will signal misbehaving applications and instruct them to close their processes. EX: kill SIGKILL 63773 ")
'''t=os.popen("ls") 
t=t.read()
print(t)
'''
print("--------------------------------------------------------------")
os.system("echo ping command is one of the most used basic Linux commands for checking whether a network or a server is reachable. In addition, it is used to troubleshoot various connectivity issues.")
u=os.popen("ping google.com") 
u=u.read()
print(u)

print("--------------------------------------------------------------")
os.system("echo wget command retrieves files using HTTP, HTTPS, and FTP protocols. It can perform recursive downloads, which transfer website parts by following directory structures and links, creating local versions of the web pages.")
v=os.popen("wget https://wordpress.org/latest.zip") 
v=v.read()
print(v)

print("--------------------------------------------------------------")
os.system("echo uname or unix name command will print detailed information about your Linux system and hardware.This includes the machine name, operating system, and kernel.  ")
w=os.popen("uname -a") 
w=w.read()
print(w)

print("--------------------------------------------------------------")
os.system("echo  top command in Linux Terminal will display all the running processes and a dynamic real-time view of the current system. It sums up the resource utilization, from CPU to memory usage.The top command can also help you identify and terminate a process that may use too many system resources.")
x=os.popen("top") 
x=x.read()
print(x)

print("--------------------------------------------------------------")
os.system("echo history, the system will list up to 500 previously executed commands, allowing you to reuse them without re-entering.")
z=os.popen("history") 
z=z.read()
print(z)

print("--------------------------------------------------------------")
os.system("echo man command provides a user manual of any commands or utilities you can run in Terminal, including the name, description, and options.")
aa=os.popen("man 2 ls") 
aa=aa.read()
print(aa)

print("--------------------------------------------------------------")
os.system("echo  echo command is a built-in utility that displays a line of text or string using the standard output.")
bb=os.popen("echo \a") 
bb=bb.read()
print(bb)

print("--------------------------------------------------------------")
os.system("echo  zip command to compress your files into a ZIP file, a universal format commonly used on Linux. It can automatically choose the best compression ratio.")
cc=os.popen("zip archive.zip test3.txt") 
cc=cc.read()
print(cc)

print("--------------------------------------------------------------")
os.system("echo hostname command to know the system’s hostname. You can execute it with or without an option. ")
dd=os.popen("hostname -i") 
dd=dd.read()
print(dd)

print("--------------------------------------------------------------")
os.system("echo  useradd is used to create a new account, while the passwd command allows you to add a password. Only those with root privileges or sudo can run the useradd command.")
'''ee=os.popen("ls") 
ee=ee.read()
print(ee)
'''
print("--------------------------------------------------------------")
os.system("echo apt-get is a command line tool for handling Advanced Package Tool (APT) libraries in Linux. It lets you retrieve information and bundles from authenticated sources to manage, update, remove, and install software and its dependencies.")
ff=os.popen("apt-get check") 
ff=ff.read()
print(ff)

print("--------------------------------------------------------------")
os.system("Linux allows users to edit and manage files via a text editor, such as nano, vi, or jed. nano and vi come with the operating system, while jed has to be installed.")
gg=os.popen("jed") 
gg=gg.read()
print(gg)

print("--------------------------------------------------------------")
os.system("echo alias allows you to create a shortcut with the same functionality as a command, file name, or text. When executed, it instructs the shell to replace one string with another. ex: alais k='kill'")
'''hh=os.popen("ls") 
hh=hh.read()
print(hh)
'''
print("--------------------------------------------------------------")
os.system("echo The switch user or su command allows you to run a program as a different user.")
'''ii=os.popen("ls") 
ii=ii.read()
print(ii)
'''
print("--------------------------------------------------------------")
os.system("echo htop command is an interactive program that monitors system resources and server processes in real time. ")
jj=os.popen("htop -d") 
jj=jj.read()
print(jj)

print("--------------------------------------------------------------")
os.system("echo The process status or ps command produces a snapshot of all running processes in your system. The static results are taken from the virtual files in the /proc file system.")
kk=os.popen("ps -e") 
kk=kk.read()
print(kk)


