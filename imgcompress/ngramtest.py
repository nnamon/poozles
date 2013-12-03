def generate_ngrams(data, ngrams=4):
    ngramdata = []
    for i in range(0, len(data)-(ngram-1)):
        ngramdata.append("%s" % data[i:i+ngram])
    return ngramdata

def search_ngrams(data, ngramdata):
    ngramlen = len(ngramdata[0])
    for i in range(0, len(data) - (ngramlen-1)):
        print "%s" % (data[i:i+ngramlen])
    
def main():
    data = "iVBORw0KGgo@4ANSUhEUg@3AGQ@3ABkCAY@3ABw4pVU@3AFX0lEQVR4nO3cMW7cMBAF0DmDr2G3TpUrJC7cJoX6JGdI4SpAYBgpUmybysBWuUKO4CO4cRukZ5qdBUXPDGdEUqKk+QBhOwsTEt9ySGnlAHg8Ho/H4/F4PJ44h+EYDsMxLH0cnlMQ5OLyVmxLH+cucnF5Gw7DMTw9PofDcAxv3n45t4vL21c/O0yj4OC+eftlBIIoFIbDNEo62Ajx9PismikOUzHpOz2eIXHjZkoNGN9EnCKVoXSG4FcK5NPVd7JpYOK+5zrvLiNhcCD4PQfw790PsnEw6UzcLQr1LudKVzpoWghp8Y93cg4C9OzQrCUWCGm9oTB2i8LNDgokfidbMTgQCcNBBIwYpBYGV6rSjcPSYzRbrLOD2kVpMLi1I1eqdglC3Y+qDZL2l+7UHCQT6QaiZlurAdFgOIiQw3AMIYQRjgbEiuEg+QQACHFwsDgYB5knZ5h0AFMYCQQA1BgOIidg4wYz3aH5+tEu59kBmXc4AIxgOJBcPw4i57x+ADOQcEIbru/CcH032gCkJYvrw0H0OWMAMZiQLPoIgol3ZhoIB8kngLCGQAJCoeAaI/XjIMoM13ciBihBLM0/+hWC6wIYQB4+/HKQVkEQDgMSlIcPv4pA/OGITCgMCgQAzhgO0jDcnVnYKEj3T2fWAAHlzgpBouuW5kkHnfo8h3oOYFYgfKBB+twCCJDh+u4VCBgw5gTRAOTabCi5D5CeHp9DvB2G6Co93fLCCQMUKMSVfZNIn5ZqGvV7rY4VAMYgEk6MQGHEIJbZ0RKEexTp7/uf6sbBtDjec7hnpSSUKdccXLlqcZJxv1aEtHHPINQ83lG0ILUad4e41vnE/ZdApCgtj/lVtKWrFILCqHlyGozPV9/Y1h1KLQxpgeQW2tLjlzAkBAvO7CgAdWA4iLS24/efr74VnRiHMQWiSxSA8TWKpkm7qNzPNUBijHRgpWuMVaFYEqPk9vIpBp74lJOSMCwXfxaUVYJQ1wDUazkQbkbi6xSG5gLQgsKBdI3CzRCplKUnHJ9Ubi3D179+/DHCsFx5W2bL6mZJbiNADQgHYtlUHIbjCEM6xtx6NgWkWxRqYZfendTJ4mvWXR3+HaT2WHOzZROLu7TTok6ewpgKgiiW47WiSCBdomhAUowpINJ9tJooqy9bVN3nrtBrgbzc3I/+fcojRRYULUgXKBJIDmNqyaoBAkD/8dImQWIU6eTSE9FghBDCy839+evUsgXAzxILSHdlSwLJ1WMryMvN/atWAgJAz5ISkMVRpGsHbps7dXakKPG60rJsbQYkRsnVYS0IlqqWM2TVIAA6lBprB1W2egRZHEVzywNRLBhxvxRI/KBeydP0ll3hKkAA9CiWmUH1me6wHESIFkVbpqT+4nLlIEJqPyyR9sfdQqkJMnXb29X1SJyaKEuD5G4uciBdoaSfuef+V6CS0lWKAbATkN8Pf8Lvhz/iQ90aEM3TMA6SSQyCKLkB55q2j5LjrQnS5TpiBdH0MxdIDoMDwcHfDYjUD/VUiiUO0gClZLZYQFIMB3EQe2oPonYtqQmiLVebBFl6luCATl0/4sFPf+4iewfpCgNgeRALSs1yhf3VGMOq2TNIl5kygNIgpv3VLFsl5cpBZgDhMHIXhF2nBxANiqVcxSCrgcCsCcRSrlYHATB98HoAkWbH6iAwawPJzY5Vzoo4awHJYaweAjN1/WgBIvXJgWwGAqBs4JYG2RQEZi0gMcYmIQDoQasBUtovB7JZCMycICV9bh4CoA4GNXitkDcfB+ks+MRH2iwYHEhpv7sEoVIDpEa/DnJKq4HzcjUxXLnhWou+W52bx+PxeDwej6eH/AfYSl5l/FOZkQ@4ABJRU5ErkJ@3g=="
    generate_ngrams(data)
    
if __name__ == "__main__":
    main()
