import pygame

#uimaker
class apic:
 def __init__(self,a,b=True):
  self.pic=a
  self.look=b
 def draw(self,win,x,y):
  if self.look:
    win.blit(self.pic,(x,y))

class t_pic:
 def __init__(self,a,b,c,d=True):
  self.wx=a
  self.wy=b
  self.pic=c
  self.look=d
 def draw(self,win):
  if self.look:
    self.pic.draw(win,self.wx,self.wy)

class butn:
 my=0
 def __init__(self,a,b,c,d,e,f=0,g=1):
  self.wx=a
  self.wy=b
  self.lx=c
  self.ly=d
  self.pic=e
  self.xz=f
  self.look=g
 def draw(self,win):
  if self.look==1:
    self.pic.draw(win,self.wx,self.wy)
 def sure(self,a,b):
  if self.look==1:
   if self.xz==0:
       if self.wx<=a<=self.wx+self.lx and self.wy<=b<=self.wy+self.ly:return True
   elif self.xz==1:
    if self.wx+10<=a<=self.wx+self.lx-10 and self.wy+10<=b<=self.wy+self.ly-10:return True
  return False
  
class ljk:
 my=1
 def __init__(self,a,b,c,d,e,f,g=0,h=1):
  self.wx=a
  self.wy=b
  self.lx=c
  self.ly=d
  self.pic1=e
  self.pic2=f
  self.xz=g
  self.look=h
 def change(self):
  self.look+=1
  if self.look>=3:
   self.look=1
 def draw(self,win):
  if self.look==1:
    self.pic1.draw(win,self.wx,self.wy)
  elif self.look==2:
    self.pic2.draw(win,self.wx,self.wy)
 def sure(self,a,b):
  if self.look>=1:
   if self.xz==0:
       if self.wx<=a<=self.wx+self.lx and self.wy<=b<=self.wy+self.ly:return True
   elif self.xz==1:
    if self.wx+10<=a<=self.wx+self.lx-10 and self.wy+10<=b<=self.wy+self.ly-10:return True
  return False
   

auiz=[]
muiz=[]
uitalk=[]

class aui:
  pictures=[]
  def __init__(self,a,b):
    #window
    pygame.init()
    self.window = pygame.display.set_mode((a, b))

  #picture
  def pics(self,path,look=True):
    self.pictures.append(apic(pygame.image.load(path),look))
  #create
  def ct_pic(self,a,b,c,d=True):
    muiz.append(t_pic(a,b,self.pictures[c],d))
  def cbutn(self,a,b,c,d,e,f=0,g=1):
    auiz.append(butn(a,b,c,d,self.pictures[e],f,g))
    uitalk.append(0)
  def cljk(self,a,b,c,d,e,f,g=0,h=1):
    auiz.append(ljk(a,b,c,d,self.pictures[e],self.pictures[f],g,h))
    uitalk.append(0)

  def draw(self):
    for x in range(len(auiz)):
      auiz[x].draw(self.window)
    for x in range(len(muiz)):
      muiz[x].draw(self.window)
  def sure(self,a,b):
    for x in range(len(auiz)):
      if auiz[x].sure(a,b):
        if auiz[x].my==0:
          uitalk[x]+=1
        else:
          auiz[x].change()
          uitalk[x]=auiz[x].look-1

  def uidraw(self):
    self.window.fill((255, 255, 255))
    self.draw()