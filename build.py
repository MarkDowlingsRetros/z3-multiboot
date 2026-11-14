#!/usr/bin/env python3
"""Pack the readable source back into the single-file player.

    python3 build.py            ->  index.html (one self-contained file)

Reads z3-multiboot-readable.html from this folder, gzips it and stores it as
base64 inside a tiny loader that unpacks it in the browser. Uses Zopfli for the
smallest output if installed (pip install zopfli), otherwise gzip.
The published index.html is made exactly this way, so it matches the readable file.
No game story file is built in: players drop their own .z3 onto the page.
The only disk included is our own Welcome Disk, compiled from welcome.inf and kept inside
the readable file.
The unpacker is built in, so it does not depend on the browser having one.
"""
import base64, gzip, pathlib, re

here = pathlib.Path(__file__).parent
page = (here / "z3-multiboot-readable.html").read_text(encoding="utf-8")
assert "window.__ZSTORY = Uint8Array" not in page, "no story should be built in"
# The Welcome Disk lives inside the readable file as base64, so that file plays on its own.
# After recompiling welcome.inf, run  python3 build.py --welcome welcome.z3  to put the new
# disk into the readable file. Either way it is packed separately below, like the page.
import sys
WRE = r"(\s*<script>\s*// The Welcome Disk:.*?atob\(\n)(.*?)(,\n\s*\),\n\s*\(c\) => c.charCodeAt\(0\),.*?</script>)"
if "--welcome" in sys.argv:
    z = (here / sys.argv[sys.argv.index("--welcome") + 1]).read_bytes()
    w = base64.b64encode(z).decode()
    body = " +\n".join('          "' + w[i : i + 96] + '"' for i in range(0, len(w), 96))
    src = here / "z3-multiboot-readable.html"
    txt, n = re.subn(WRE, lambda m: m.group(1) + body + m.group(3), src.read_text(encoding="utf-8"), count=1, flags=re.S)
    assert n == 1, "Welcome Disk script not found"
    src.write_text(txt, encoding="utf-8")
    page = txt
    print(f"Welcome Disk updated in the readable file: {len(z):,} bytes")
m = re.search(WRE, page, flags=re.S)
assert m, "Welcome Disk script not found"
welcome = base64.b64decode("".join(re.findall(r'"([A-Za-z0-9+/=]+)"', m.group(2))))
assert welcome[0] == 3, "Welcome Disk is not a version 3 story file"
page = page[: m.start()] + page[m.end() :]

try:
    import zopfli.gzip as zg
    pack = lambda b: zg.compress(b, numiterations=60)
except ImportError:
    pack = lambda b: gzip.compress(b, 9)

b64 = lambda b: base64.b64encode(pack(b)).decode()

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>Z3 Multiboot</title>
<meta name="claude:viewport-fit-sides" content="cover">
<!--
Z3 Multiboot
Version 1.0. Developed by Mark Dowling, Melbourne, Australia, November 2026.
Released into the public domain (see LICENSE at github.com/MarkDowlingsRetros/z3-multiboot).
Hacks and remixes welcome. A credit is appreciated if you share your own version.
-->
<meta name="author" content="Mark Dowling, Melbourne, Australia">
<!--
The Welcome Disk was compiled with Inform 6 and the PunyInform library (github.com/johanberntsson/PunyInform):
MIT License

Copyright (c) 2019 Fredrik Ramsberg and Johan Berntsson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-->
<style>html,body{height:100%;margin:0;background:#111316}#zld{padding:16px;color:#8a929e;font:13px ui-monospace,Menlo,monospace}</style></head><body>
<div id="zld">Unpacking…</div>
"""
LOADER = """<script>
function zInflate(d){
 let p=10,f=d[3];
 if(d[0]!==31||d[1]!==139||d[2]!==8)throw Error('not gzip');
 if(f&4)p+=2+(d[10]|d[11]<<8);
 if(f&8)while(d[p++]);
 if(f&16)while(d[p++]);
 if(f&2)p+=2;
 let bb=0,bc=0,o=new Uint8Array(d.length*4),n=0;
 const need=k=>{if(n+k>o.length){const t=new Uint8Array(Math.max(o.length*2,n+k));t.set(o);o=t}};
 const bits=k=>{let v=bb;while(bc<k){if(p>=d.length)throw Error('truncated');v|=d[p++]<<bc;bc+=8}bb=v>>>k;bc-=k;return v&((1<<k)-1)};
 const build=(L,s,c)=>{const cnt=new Uint16Array(16),sym=new Uint16Array(c),off=new Uint16Array(16);for(let i=0;i<c;i++)cnt[L[s+i]]++;cnt[0]=0;for(let i=1;i<16;i++)off[i]=off[i-1]+cnt[i-1];for(let i=0;i<c;i++)if(L[s+i])sym[off[L[s+i]]++]=i;return[cnt,sym]};
 const dec=h=>{let c=0,fi=0,ix=0;for(let l=1;l<16;l++){c|=bits(1);const k=h[0][l];if(c-k<fi)return h[1][ix+c-fi];ix+=k;fi+=k;fi<<=1;c<<=1}throw Error('bad code')};
 const LB=[3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,35,43,51,59,67,83,99,115,131,163,195,227,258],LE=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0],DB=[1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,257,385,513,769,1025,1537,2049,3073,4097,6145,8193,12289,16385,24577],DE=[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13],OR=[16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15];
 let fl,fd;
 for(let last=0;!last;){
  last=bits(1);const t=bits(2);
  if(t===0){bb=bc=0;const len=d[p]|d[p+1]<<8;p+=4;need(len);o.set(d.subarray(p,p+len),n);n+=len;p+=len;continue}
  let lh,dh;
  if(t===1){if(!fl){const L=new Uint8Array(320);L.fill(8,0,144);L.fill(9,144,256);L.fill(7,256,280);L.fill(8,280,288);L.fill(5,288,320);fl=build(L,0,288);fd=build(L,288,32)}lh=fl;dh=fd}
  else if(t===2){const hl=bits(5)+257,hd=bits(5)+1,hc=bits(4)+4,C=new Uint8Array(19);for(let i=0;i<hc;i++)C[OR[i]]=bits(3);const ch=build(C,0,19),L=new Uint8Array(hl+hd);for(let i=0;i<hl+hd;){const s=dec(ch);if(s<16)L[i++]=s;else{let r,v=0;if(s===16){v=L[i-1];r=3+bits(2)}else if(s===17)r=3+bits(3);else r=11+bits(7);L.fill(v,i,i+r);i+=r}}lh=build(L,0,hl);dh=build(L,hl,hd)}
  else throw Error('bad block');
  for(;;){const s=dec(lh);if(s<256){need(1);o[n++]=s}else if(s===256)break;else{const i=s-257,len=LB[i]+bits(LE[i]),j=dec(dh),dist=DB[j]+bits(DE[j]);need(len);for(let k=0;k<len;k++,n++)o[n]=o[n-dist]}}
 }
 return o.subarray(0,n);
}
(()=>{
const ld=document.getElementById('zld');
try{
const raw=s=>{const b=atob(s),u=new Uint8Array(b.length);for(let i=0;i<b.length;i++)u[i]=b.charCodeAt(i);return u};
const A="%%PAGE%%",B="%%WELCOME%%";
const html=new TextDecoder().decode(zInflate(raw(A)));
window.__ZWELCOME=zInflate(raw(B)).slice();
const doc=new DOMParser().parseFromString(html,'text/html');
ld.remove();
const put=(n,parent)=>{
  if(n.nodeName==='SCRIPT'){const s=document.createElement('script');s.textContent=n.textContent;parent.append(s);}
  else if(n.nodeName==='TITLE'){}
  else parent.append(document.importNode(n,true));
};
for(const n of [...doc.head.childNodes])put(n,document.head);
for(const n of [...doc.body.childNodes])put(n,document.body);
}catch(e){ld.textContent='Sorry, the player could not be unpacked on this browser ('+(e&&e.message||e)+'). Please report it at github.com/MarkDowlingsRetros/z3-multiboot/issues';}
})();
</script>
</body></html>"""

out = HEAD + LOADER.replace("%%PAGE%%", b64(page.encode("utf-8"))).replace("%%WELCOME%%", b64(welcome))
(here / "index.html").write_text(out, encoding="utf-8")
print(f"index.html written: {len(out):,} bytes")
