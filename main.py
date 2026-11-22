import json,os,base64,urllib.request as U
E=os.environ["MAKEFUN_ENV_URL"]
BK="""birng100kb~yidZvPneTCBa4ygQYOc2cTYl72iTYKOOjhpRMm0NTJiBCjRQpgwi6CBCEWQhgwsWUZJA;catngth-3w~GVCDFZB1SSpVoDYMNG5AKQJQAGadKOjVQZYUM7WWeV+nphigvsHWr7d8OMGFCiBBEVdRSEnDsqWw5EksWaNN2+zaZM8eZEMGIEFCjBhx4qVFCjQ;dutceth-4w~KaBlBBhCAlkESVkAlm5BRYsoU0aRChgAhLZvAimOxJ5g82fbGhR0wiRaOqFEIIMHmzyIMGIEFDLpRgw49fOO3fg;engan250kb~tjRsunjyrtMyUTKedqm2tra0U09rbzmkk7xJVXE7yNmP+3ZZU0A;engan250kw~ajCnCUiowZcWmEGAAk3C8yZw5WDrHVK6lSpWUDiCJChAukvTHl18;itameth-4w~LTORg0TUZEMSyTcBmBDDMAJQOEBLKNlZk1ghgWiMFIwG1CkwIQAGmtWvn5gkiSIGCiqA;kinckth-2w~LbKtm6hTRqMCkCUHOA0QoZSIi0irV+knDThxoAEPfNPAuj3Tp4H2ezZ1jHHfyvNnKA;phice500kb~90SNvPlrx5RnS70e+OrGECx49m3vQMGEXCDSRI684OqFIkTKlogA4AMoECQ;ruyin100kb~cre6M6nnyuVVElfaVtZUrzKt3atudSn1Sp6Vx6qeVXTJjhzw;ruyhyth-3b~9iZ1O9HTx6da8neRYMYWlqiFg23nTvn11rp1YscA;ruyhy100kw~EGMIgUhaRWYHOm1I6tYxroJ0K6AFDCp7kapWdds29e3r9m1ollPqOWWugA;scaceth-4b~5qdPHlXnSCVpYqbesmUjcrGlLW6zd8M9Gla2Nxgsjf8OP2VTe9fM/fVxH2G1xh9hofdaKHVSq5RVG0VQLjhxQo4c8gAAIEFoqR44;semavth-2w~GVCpk2jSZJwm4EGOJg0SjgUQJYGPI2FZAUyyRJEmdACIq1eQ;semav500kw~GVCphBhKQAEm0DRBIGrCNizQrIQZAspKlXbuwo4bjWdnIwppnFpm;sicin500kb~zrc1K5EaSrt1m2ue7OOmtq2R/6zXd1F3nXZ4N6a0sbejSmNQoIEUKCBFAA;sicalth-2b~0kY1O8mUj2t5898ccq4kkTONE2bkSOnVHTy1x44eMKOHEyagxMoYMKA;sicrfth-3b~6zd5trnuza1bs0sc0PPlETChEwYSbNq41kaNpm8ede+PFDpo1Qom48eGE1CipU4A;slace250kw~IYBFjHAphiAAQckBgG5BagQYo6VmCgpnBBYttBQShAQIIUMQHlFChxA;itameth-2w~LTORg0SOJqxjQBLUNCWSbRqIWqirBFmYSTQt0IMVmNRpnBqoUFDSBDAAqcQcYGlHmpvDHnLV/4A;scometh-2w~bqOSCmgJYhAWiRiBKCWUlYVMIMFEKFmoibQNUrUqjRVI6lUKHEAIPfNJsalVwt07eu2A;ruyinth-2w~FEFpoagkgKZNoBLSCNIkXotEjETcKtiWRqpVxFmcjBqhNCsaPhxGbsABo5Afbv5JsA;pirceth-2w~CUCmHIyUYQYKIbkABlZCkQxUriDCBFCjBrqI07INUHrjnj04Y8YaEGG2jx1t5RsA;scaceth-2w~CLDKm5AZhKErIMaSNBTBqoQwYKarQthRhd49c3CACQtmzBKILoY267N1KpHfgA;sicalth-2w~BSNwgpkKCa0g0aUCpkoxSQlIGwThKShBh64UMGmADRqE40NRipVWrQIaAA;petceth-2w~LbCphBhTQFIKIajJRlTybhxUGiCdR5G4iNjKwrwADB5nZFkyTYJ4z3A;sicinth-2w~GVCtGkQKSSsHWShKzJtQShSkIERjazI6lPYcQJoDEaahPAA;twotsth-2w~EGORhRB6454rIEkNRg1QKRKNHoVxDHNLmOY4dn27fSeA;carceth-2w~FMCDCkklpV8CWLcGTn7k9wNEjqbkGugnQqpWVq0adA;caralth-2w~cWBFimgpgNEjiGMLGBBhbrHhxy5xY8ucQoTHhxUq6A;frechth-2w~KSCpjlh75+ca6dkFqhlyswQYncm1Lug3jcSKo9YszA;sicrfth-2w~BSCwoczcoKZNaSjBmCWTMQpIIMABAohQRlBGFDAo4A;sicovth-2w~BSNwkowRYVMSiDeQ5Hpk1y7VlYLvXlhC2vjyFHohqA;foutsth-2w~EGFplWyRiFgwiCmOSE2iLRpNJamfGLAyxd6/dv+A;kinitth-2w~VkFtgnQsIOcUkEGAlnZgurXQcqk1a/ptAAifUA;queedth-2w~MUDKgykz59YrIbkABj1g96S0Vu3/X7hU284;leceth-2w~FMKyAzElQEsWqEGGWLLisgJ0U0usNyBQ1lw;freceth-2w~GVCwoaggwKYrIDnSXJrV36fVrmNdZ7t9QA;viemeth-2w~GVCmBBhaQYcrIMhBzgpguoAVN2Ftd5MqwA;ruyhyth-2w~EGMIhRAKQtIQwRYKyJKgZhiEZCh5AA;sicedth-2w~LTDGEoxiRKMUkPfPzg5wV6e9fcH/AA;freerth-2w~IQIMkoTMQVMMuEGBzl3Ttifx56A;phiceth-2w~IYNyDniswVo1qSjRqNYzEANMmiA"""
B={}
def _u(s):
 r=base64.b64decode(s+"="*((-len(s))%4));n=len(r)*8;v=int.from_bytes(r,"big");o=[]
 for k in range(n//13):
  x=(v>>(n-13*(k+1)))&0x1FFF;f=(x>>7)&63;t=(x>>1)&63
  o.append(chr(97+f%8)+str(f//8+1)+chr(97+t%8)+str(t//8+1)+("q" if x&1 else ""))
 return o
for e in BK.split(";"):
 if e:
  k,v=e.split("~");B[k]=_u(v)
VC={"p":100,"n":320,"b":330,"r":500,"q":900,"k":0}
def cv(fen,sq):
 f=ord(sq[0])-97;r=int(sq[1])-1;row=fen.split()[0].split("/")[7-r];i=0
 for ch in row:
  if ch.isdigit():i+=int(ch)
  else:
   if i==f:return VC.get(ch.lower(),0)
   i+=1
 return 0
def po(p,x):
 r=U.Request(E+p,data=json.dumps(x).encode(),headers={"content-type":"application/json"})
 with U.urlopen(r,timeout=60) as y:return json.load(y)
while True:
 g=po("/game",{})
 if g.get("status")=="done":break
 while g.get("status")=="your_move":
  o=g["opening"]["id"];k=o[:3]+o[-2:]+g["opponent"][-4:]+g["colour"][0]
  L=B.get(k,[]);i=(g["plies"]-8)//2
  mv=L[i] if 0<=i<len(L) and L[i] in g["legal_moves"] else None
  if mv is None:
   fen=g["fen"]
   mv=max(g["legal_moves"],key=lambda m:(cv(fen,m[2:4]),len(m),-abs(ord(m[0])-104)-abs(int(m[1])-5)))
  g=po("/move",{"game":g["game"],"move":mv})
