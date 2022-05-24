def ipadd(ip):
    new=""
    split=ip.split(".")
    sep="[.]"
    new=sep.join(split)
    return new
ip=input()
ip=ipadd(ip)
print(ip)