# Builds a single self-contained preview file (images inlined as data URIs) for sharing as an artifact.
import re,base64,mimetypes,sys
src=open("index.html",encoding="utf-8").read()
def inline(m):
    p=m.group(2); mt=mimetypes.guess_type(p)[0]
    return m.group(1)+"data:%s;base64,%s"%(mt,base64.b64encode(open(p,"rb").read()).decode())
out=re.sub(r'(src=")(assets/[^"]+)(?=")',lambda m:inline(m),src)
open(sys.argv[1],"w",encoding="utf-8").write(out); print(len(out)//1024,"KB")
