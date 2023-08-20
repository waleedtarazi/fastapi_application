from typing import Union
import Routes.General as GTest
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

class Answer(BaseModel):
    answer: str


engine = GTest.GeneralTest()
DiagnoseRouter = APIRouter(prefix="/diagnose", tags=["Diagnose"])

@DiagnoseRouter.get("/answer1")
def question1():
    engine.reset()
    engine.run()
    return engine.sendlive()
s=0
@DiagnoseRouter.post("/answer2")
async def answer2(answer1:Answer):
    global s
    if(answer1.answer=='لا'):
     s=1
     return engine.livingproblem()
    if(answer1.answer=='نعم'):
     s=2
     return engine.smooker()
@DiagnoseRouter.post("/answer3")
async def answer3(answer1:Answer):
   if(answer1.answer=='نعم'):
    if s==1:
      return engine.illness3()
    if s==2:
      return engine.illness2()
   if(answer1.answer=='لا'):
     return engine.Study()
z=0
@DiagnoseRouter.post("/answer4")
async def answer4(answer1:Answer):
   global z
   if(answer1.answer=='نعم'):
      z=1
      return engine.StudyDIFF2()
   if(answer1.answer=='لا'):
     z=2
     return engine.Work1()
v=0   
@DiagnoseRouter.post("/answer5")
async def answer5(answer1:Answer):
   global v
   if(z==1):

    if(answer1.answer=='نعم'):
        return engine.illness5()
    if(answer1.answer=='لا'):
      v=1
      return engine.Army()
   if(z==2): 
    if(answer1.answer=='نعم'):
        v=2
        return engine.worknot()
    if(answer1.answer=='لا'):
      v=3
      return engine.Work3()
c=0 
@DiagnoseRouter.post("/answer6")    
async def answer6(answer1:Answer):
  global c
  if(v==1):

   if(answer1.answer=='نعم'):
      return engine.illness6()
   if(answer1.answer=='لا'):
     c=1
     return engine.Work1()
  if(v==2):
   if(answer1.answer=='نعم'):
      return engine.illness7()
   if(answer1.answer=='لا'):
     c=2
     return engine.Work2()
  if(v==3):
   if(answer1.answer=='نعم'):
      return engine.illness9()
   if(answer1.answer=='لا'):
     c=3
     return engine.family()
d=0
@DiagnoseRouter.post("/answer7")
async def answer7(answer1:Answer):
   global d
   if(c==1):
    
    if(answer1.answer=='نعم'):
        return engine.worknot()
    if(answer1.answer=='لا'):
      d=1
      return engine.Work3()
   if(c==2): 
    if(answer1.answer=='نعم'):
        return engine.illness8()
    if(answer1.answer=='لا'):
      d=2
      return engine.family()
   if(c==3): 
    if(answer1.answer=='نعم'):
        d=3
        return engine.hfamily()
    if(answer1.answer=='لا'):
      d=4
      return engine.Married()
b=0
@DiagnoseRouter.post("/answer8")
async def answer8(answer1:Answer):
   global b
   if(d==1):
    if(answer1.answer=='نعم'):
        return engine.illness9()
    if(answer1.answer=='لا'):
      b=1
      return engine.family()
   if(d==2): 
    if(answer1.answer=='نعم'):
        b=2
        return engine.hfamily()
    if(answer1.answer=='لا'):
      b=3
      return engine.Married()
   if(d==3): 
    if(answer1.answer=='نعم' or answer1.answer=='لا'):
        b=4
        return engine.familyg()
   if(d==4): 
    if(answer1.answer=='نعم'):
        b=5
        return engine.marry()
    if(answer1.answer=='لا'):
      b=6
      return engine.marry1()
vc=0
@DiagnoseRouter.post("/answer9")
async def answer9(answer1:Answer):
  global vc
  if(b==1): 
   if(answer1.answer=='نعم'):
      vc=1
      return engine.hfamily()
   if(answer1.answer=='لا'):
     vc=2
     return engine.Married()
  if(b==2): 
   if(answer1.answer=='نعم' or answer1.answer=='لا'):
      vc=3
      return engine.familyg()
  if(b==3): 
   if(answer1.answer=='نعم'):
      vc=4
      return engine.marry()
   if(answer1.answer=='لا'):
     vc=5
     return engine.marry1()
  if(b==4): 
   if(answer1.answer=='نعم'):
      return engine.illness11()
   if(answer1.answer=='لا'):
     vc=6
     return engine.Married()
  if(b==5): 
   if(answer1.answer=='نعم'):
      vc=7
      return engine.marry3()
   if(answer1.answer=='لا'):
     vc=8
     return engine.marry24()
  if(b==6): 
   if(answer1.answer=='نعم'):
      return engine.illness12()
   if(answer1.answer=='لا'):
     vc=9
     return engine.pd1()
f=0
@DiagnoseRouter.post("/answer10")
async def answer10(answer1:Answer):
  global f
  if(vc==1): 
   if(answer1.answer=='نعم' or answer1.answer=='لا'):
    f=1
    return engine.familyg()
  if(vc==2 or vc==6): 
   if(answer1.answer=='نعم'):
      f=2
      return engine.marry()
   if(answer1.answer=='لا'):
     f=3
     return engine.marry1()
  if(vc==3): 
   if(answer1.answer=='نعم'):
      return engine.illness11()
   if(answer1.answer=='لا'):
     f=4
     return engine.Married()
  if(vc==4): 
   if(answer1.answer=='نعم'):
      f=5
      return engine.marry3()
   if(answer1.answer=='لا'):
     f=6
     return engine.marry24()
  if(vc==5): 
   if(answer1.answer=='نعم'):
      return engine.illness12()
   if(answer1.answer=='لا'):
     f=7
     return engine.pd1()
  if(vc==7): 
   if(answer1.answer=='نعم'):
      return engine.illness13()
   if(answer1.answer=='لا'):
     f=6
     return engine.marry24()
  if(vc==8): 
   if(answer1.answer=='نعم'):
      f=7
      return engine.marry23()
   if(answer1.answer=='لا'):
     f=8
     return engine.marry4()
  if(vc==9): 
   if(answer1.answer=='نعم'):
      f=9
      return engine.pd2()
   if(answer1.answer=='لا'):
     f=10
     return engine.food()
   
x=0     
@DiagnoseRouter.post("/answer11")
async def answer11(answer1:Answer):
  global x
  if(f==1): 
   if(answer1.answer=='نعم'):
      return engine.illness11()
   if(answer1.answer=='لا'):
     x=1
     return engine.Married()
  if(f==2): 
   if(answer1.answer=='نعم'):
      x=2
      return engine.marry3()
   if(answer1.answer=='لا'):
     x=3
     return engine.marry24()
  if(f==3): 
   if(answer1.answer=='نعم'):
      return engine.illness12()
   if(answer1.answer=='لا'):
     x=4
     return engine.pd1()
  if(f==4):  
   if(answer1.answer=='نعم'):
      x=5
      return engine.marry()
   if(answer1.answer=='لا'):
     x=6
     return engine.marry1()
  if(f==5): 
   if(answer1.answer=='نعم'):
      return engine.illness13()
   if(answer1.answer=='لا'):
     x=7
     return engine.marry24()
  if(f==6):
   if(answer1.answer=='نعم'):
      x=8
      return engine.marry23()
   if(answer1.answer=='لا'):
     x=9
     return engine.marry4()
   
  if(f==7):
   if(answer1.answer=='لا'):
      return engine.illness15()
   if(answer1.answer=='نعم'):
     x=10
     return engine.pd1()
  if(f==8):
   if(answer1.answer=='نعم'):
      return engine.illness14()
   if(answer1.answer=='لا'):
     x=10
     return engine.pd1()
  if(f==9):
   if(answer1.answer=='نعم'):
      return engine.illness16()
   if(answer1.answer=='لا'):
     x=11
     return engine.food()
  if(f==10):
   if(answer1.answer=='لا'):
      return engine.illnessfinal()
   if(answer1.answer=='نعم'):
     x=12
     return engine.pd24()
h=0   
@DiagnoseRouter.post("/answer12")
async def answer12(answer1:Answer):
  global h 
  if(x==1): 
   if(answer1.answer=='نعم'):
      h=1
      return engine.marry()
   if(answer1.answer=='لا'):
     h=2
     return engine.marry1() 
  if(x==2): 
   if(answer1.answer=='نعم'):
      return engine.illness13()
   if(answer1.answer=='لا'):
     h=3
     return engine.marry24()
  if(x==3): 
   if(answer1.answer=='نعم'):
      h=4
      return engine.marry23()
   if(answer1.answer=='لا'):
     h=5
     return engine.marry4()
  if(x==4):
   if(answer1.answer=='نعم'):
      h=6
      return engine.pd2()
   if(answer1.answer=='لا'):
     h=7
     return engine.food()
  if(x==5):
   if(answer1.answer=='نعم'):
      h=8
      return engine.marry3()
   if(answer1.answer=='لا'):
     h=9
     return engine.marry24()
  if(x==6): 
   if(answer1.answer=='نعم'):
      return engine.illness12()
   if(answer1.answer=='لا'):
     h=10
     return engine.pd1()
  if(x==7): 
   if(answer1.answer=='نعم'):
      h=11
      return engine.marry23()
   if(answer1.answer=='لا'):
     h=12
     return engine.marry4()
   
  if(x==8): 
   if(answer1.answer=='لا'):
      return engine.illness15()
   if(answer1.answer=='نعم'):
     h=10
     return engine.pd1()
  if(x==9): 
   if(answer1.answer=='نعم'):
      return engine.illness14()
   if(answer1.answer=='لا'):
     h=10
     return engine.pd1()
  if(x==9): 
   if(answer1.answer=='نعم'):
      return engine.illness14()
   if(answer1.answer=='لا'):
     h=10
     return engine.pd1()
   
  if(x==10): 
       
   if(answer1.answer=='نعم'):
      h=6
      return engine.pd2()
   if(answer1.answer=='لا'):
     h=7
     return engine.food()
  if(x==11): 
   if(answer1.answer=='لا'):
      return engine.illnessfinal()
   if(answer1.answer=='نعم'):
     h=13
     return engine.pd24()
   if(x==12): 
    if(answer1.answer=='لا'):
      return engine.illnessfinal()
    if(answer1.answer=='نعم'):
     return engine.illness17()
a=0
@DiagnoseRouter.post("/answer13")
async def answer13(answer1:Answer):
  global a
  if(h==1): 
   if(answer1.answer=='نعم'):
      a=1
      return engine.marry3()
   if(answer1.answer=='لا'):
     a=2
     return engine.marry24()
  if(h==2): 
   if(answer1.answer=='لا'):
      a=3
      return engine.pd1()
   if(answer1.answer=='نعم'):
     return engine.illness12()
  if(h==3): 
   if(answer1.answer=='نعم'):
      a=4
      return engine.marry23()
   if(answer1.answer=='لا'):
     a=5
     return engine.marry4() 
  if(h==4): 
   if(answer1.answer=='لا'):
      return engine.illness15()
   if(answer1.answer=='نعم'):
     a=3
     return engine.pd1() 
  if(h==5): 
   if(answer1.answer=='نعم'):
      return engine.illness14()
   if(answer1.answer=='لا'):
     a=3
     return engine.pd1()
  if(h==6):
   if(answer1.answer=='نعم'):
      return engine.illness16()
   if(answer1.answer=='لا'):
     a=6
     return engine.food()
  if(h==7):
   if(answer1.answer=='لا'):
      return engine.illnessfinal()
   if(answer1.answer=='نعم'):
     a=7
     return engine.pd24()
  if(h==8):
   if(answer1.answer=='نعم'):
      return engine.illness13()
   if(answer1.answer=='لا'):
     a=2
     return engine.marry24()
  if(h==9):
   if(answer1.answer=='نعم'):
      a=4
      return engine.marry23()
   if(answer1.answer=='لا'):
     a=5
     return engine.marry4()
  if(h==10):
   if(answer1.answer=='نعم'):
      a=8
      return engine.pd2()
   if(answer1.answer=='لا'):
     a=6
     return engine.food()
  if(h==11):
   if(answer1.answer=='لا'):
      return engine.illness15()
   if(answer1.answer=='نعم'):
     a=3
     return engine.pd1()
   
  if(h==12):
   if(answer1.answer=='نعم'):
      return engine.illness14()
   if(answer1.answer=='لا'):
     a=3
     return engine.pd1()
  if(h==13):
    if(answer1.answer=='لا'):
      return engine.illnessfinal()
    if(answer1.answer=='نعم'):
     return engine.illness17()
q=0   
@DiagnoseRouter.post("/answer14")
async def answer14(answer1:Answer):
  global q 
  if(a==1):
   if(answer1.answer=='نعم'):
      return engine.illness13()
   if(answer1.answer=='لا'):
     q=1
     return engine.marry24()
  if(a==2):
   if(answer1.answer=='نعم'):
      q=2
      return engine.marry23()
   if(answer1.answer=='لا'):
     q=3
     return engine.marry4() 
  if(a==3):
   if(answer1.answer=='نعم'):
      q=4
      return engine.pd2()
   if(answer1.answer=='لا'):
     q=5
     return engine.food()
  if(a==4): 
   if(answer1.answer=='لا'):
      return engine.illness15()
   if(answer1.answer=='نعم'):
     q=6 
     return engine.pd1()
  if(a==5):
   if(answer1.answer=='نعم'):
      return engine.illness14()
   if(answer1.answer=='لا'):
     q=6
     return engine.pd1()
  if(a==6):
   if(answer1.answer=='لا'):
      return engine.illnessfinal()
   if(answer1.answer=='نعم'):
     q=7
     return engine.pd24()
   if(a==7):
    if(answer1.answer=='لا'):
      return engine.illnessfinal()
    if(answer1.answer=='نعم'):
     return engine.illness17()
   if(a==8):
    if(answer1.answer=='نعم'):
      return engine.illness16()
    if(answer1.answer=='لا'):
     q=5
     return engine.food()
e=0
@DiagnoseRouter.post("/answer15")
async def answer15(answer1:Answer):
  global e 
  if(q==1):
   if(answer1.answer=='نعم'):
      e=1
      return engine.marry23()
   if(answer1.answer=='لا'):
     e=2
     return engine.marry4() 
  if (q==2):
   if(answer1.answer=='لا'):
      return engine.illness15()
   if(answer1.answer=='نعم'):
     e=3
     return engine.pd1()
  if (q==3):
   if(answer1.answer=='نعم'):
      return engine.illness14()
   if(answer1.answer=='لا'):
     e=3
     return engine.pd1()
  if (q==4):
    if(answer1.answer=='نعم'):
      return engine.illness16()
    if(answer1.answer=='لا'):
      e=4
      return engine.food()
  if (q==5):
   if(answer1.answer=='لا'):
      return engine.illnessfinal()
   if(answer1.answer=='نعم'):
     e=5
     return engine.pd24()
  if (q==6):
   if(answer1.answer=='نعم'):
      e=6
      return engine.pd2()
   if(answer1.answer=='لا'):
     e=4
     return engine.food()
  if (q==7):
   if(answer1.answer=='لا'):
      return engine.illnessfinal()
   if(answer1.answer=='نعم'):
     return engine.illness17()
g=0
@DiagnoseRouter.post("/answer16")
async def answer16(answer1:Answer):
  global g 
  if(e==1):
   if(answer1.answer=='لا'):
      return engine.illness15()
   if(answer1.answer=='نعم'):
     g=1
     return engine.pd1()
  if(e==2):
   if(answer1.answer=='نعم'):
      return engine.illness14()
   if(answer1.answer=='لا'):
     g=1
     return engine.pd1()
  if(e==3):
   if(answer1.answer=='نعم'):
      g=2
      return engine.pd2()
   if(answer1.answer=='لا'):
     g=3
     return engine.food()
  if(e==4):
   if(answer1.answer=='لا'):
      return engine.illnessfinal()
   if(answer1.answer=='نعم'):
     g=4
     return engine.pd24()
  if (e==5):
   if(answer1.answer=='لا'):
      return engine.illnessfinal()
   if(answer1.answer=='نعم'):
     return engine.illness17()
  if (e==6):
    if(answer1.answer=='نعم'):
      return engine.illness16()
    if(answer1.answer=='لا'):
      g=3
      return engine.food()
n=0    
@DiagnoseRouter.post("/answer17")
async def answer17(answer1:Answer):
  global n 
  if(g==1):
   if(answer1.answer=='نعم'):
      n=1
      return engine.pd2()
   if(answer1.answer=='لا'):
     n=2
     return engine.food()
   if (g==2):
    if(answer1.answer=='نعم'):
      return engine.illness16()
    if(answer1.answer=='لا'):
      n=2
      return engine.food()
   if(g==3):
      if(answer1.answer=='لا'):
         return engine.illnessfinal()
      if(answer1.answer=='نعم'):
       n=3
       return engine.pd24()
   if(g==4):
      if(answer1.answer=='لا'):
         return engine.illnessfinal()
      if(answer1.answer=='نعم'):
       return engine.illness17()
l=0         
@DiagnoseRouter.post("/answer18")
async def answer18(answer1:Answer):
  global l 
  l=0
  if (n==1):
    if(answer1.answer=='نعم'):
      return engine.illness16()
    if(answer1.answer=='لا'):
      l=1
      return engine.food()
  if(n==2):
      if(answer1.answer=='لا'):
         return engine.illnessfinal()
      if(answer1.answer=='نعم'):
       l=2
       return engine.pd24()
      
  if(n==3):
      if(answer1.answer=='لا'):
         return engine.illnessfinal()
      if(answer1.answer=='نعم'):
       return engine.illness17()
t=0
@DiagnoseRouter.post("/answer19")
async def answer19(answer1:Answer):
  global t 
  if (l==1):
      if(answer1.answer=='لا'):
         return engine.illnessfinal()
      if(answer1.answer=='نعم'):
       t=1
       return engine.pd24()
  if(l==2):
      if(answer1.answer=='لا'):
         return engine.illnessfinal()
      if(answer1.answer=='نعم'):
       
       return engine.illness17()

@DiagnoseRouter.post("/answer20")
async def answer20(answer1:Answer):    
  
  if(t==1):
      if(answer1.answer=='لا'):
         return engine.illnessfinal()
      if(answer1.answer=='نعم'):
       
       return engine.illness17()
anx1 = 0 
anx2=0
anx3=0
anx4=0
anx5=0
anx6=0
@DiagnoseRouter.get("/Anxiety1")
def Anxiety1():
    return ('هل تعاني من الهواجس ؟')
@DiagnoseRouter.post("/Anxiety2")
async def Anxiety2(answer1:Answer):
    global anx1
    anx1=0
    if(answer1.answer=='لا'):
     anx1=1
     return ("هل لديك خوف أو قلق شديد ؟")
    if(answer1.answer=='نعم'):
     anx1=2
     return ("هل تستهلك الهواجس/السلوكيات وقتا طويلا من حياتك؟")
@DiagnoseRouter.post("/Anxiety3")
async def Anxiety3(answer1:Answer):
    global anx2
    anx2=0
    if(anx1==2):
      anx2=2
      return ("هل تتعارض هذه الانشطة القهرية مع قيمك وحياتك الشخصية؟ ")
    if(anx1==1):
       if(answer1.answer=='نعم'):
         anx2=1
         return(" هل تعاني من أحد هذه الأعراض: 1-زيادة في ضربات القلب 2-أمل في الصدر 3-ضيق تنفس 4-تعرق شديد 5-الشعور بالدوخة 6-الارتجاف والقشعريرة 7-الغثيان")
       if(answer1.answer=='لا'):
         return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
@DiagnoseRouter.post("/Anxiety4")
async def Anxiety4(answer1:Answer):
    global anx3
    if(anx2==2):
       if(answer1.answer=='نعم'):
          return("يبدوا انك تعاني من الوسواس القهري")
       if(answer1.answer=='لا'):
          anx3=1
          return("هل لديك خوف أو قلق شديد؟")
    if(anx2==1):
       if(answer1.answer=='نعم'):
         return("يبدوا انك تعاني من نوبات الهلع")
       if(answer1.answer=='لا'):
          anx3=2
          return('هل تعاني من تعب متكرر في الجسم؟')
@DiagnoseRouter.post("/Anxiety5")
async def Anxiety5(answer1:Answer):
    global anx4
    if(anx3==2):
       if(answer1.answer=='نعم'):
        anx4=1
        return('هل تعاني إحدى هذه الأعراض: -مشاكل في التركيز -مشاكل في النوم -تغضب بسهولة؟')
       if(answer1.answer=='لا'):
         return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
    if(anx3==1):
       if(answer1.answer=='نعم'):
         anx4=2
         return(" هل تعاني من أحد هذه الأعراض: 1-زيادة في ضربات القلب 2-أمل في الصدر 3-ضيق تنفس 4-تعرق شديد 5-الشعور بالدوخة 6-الارتجاف والقشعريرة 7-الغثيان")
       if(answer1.answer=='لا'):
         return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
@DiagnoseRouter.post("/Anxiety6")
async def Anxiety6(answer1:Answer):
    global anx5
    if(anx4==1):
       if(answer1.answer=='نعم'):
        return("يبدو انك تعاني من اضطراب القلق عام")
       if(answer1.answer=='لا'):
         return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
    if(anx4==2):
       if(answer1.answer=='نعم'):
         return("يبدوا انك تعاني من نوبات الهلع")
       if(answer1.answer=='لا'):
          anx5=1
          return("هل تعاني من تعب متكرر في الجسم؟")
@DiagnoseRouter.post("/Anxiety7")
async def Anxiety7(answer1:Answer):
   global anx6
   if(anx5==1):
       if(answer1.answer=='نعم'):
        anx6=1
        return('هل تعاني إحدى هذه الأعراض: -مشاكل في التركيز -مشاكل في النوم -تغضب بسهولة؟')
       if(answer1.answer=='لا'):
         return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
@DiagnoseRouter.post("/Anxiety8")
async def Anxiety8(answer1:Answer):
    if(anx6==1):
       if(answer1.answer=='نعم'):
        return('يبدو انك تعاني من اضطراب القلق عام')
       if(answer1.answer=='لا'):
         return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")


@DiagnoseRouter.post("/Eating")
async def Eating(height:int,weight:int):
 bmi= (height *height)/weight
 if(bmi<16):
  return ("يبدوا انك تعاني من نحافة شديدة")
 if(bmi>=16 and bmi <=17):
  return ("يبدوا انك تعاني من نحافة معتدلة")
 if(bmi>17 and bmi <=18.5):
  return ("يبدوا انك تعاني من نحافة خفيفة ، لا داعي للقلق")
 if(bmi>18.5 and bmi <=25):
  return ("يبدوا انك في وزنك طبيعي ، لا داعي للقلق")
 if(bmi>25 and bmi <=30):
  return ("يبدوا انك تعاني من زيادة في الوزن")
 if(bmi>30 and bmi <=35):
  return ("يبدوا انك تعاني السمنة من الفئة الأولى")
 if(bmi>35 and bmi <=40):
  return ("يبدوا انك تعاني السمنة من الفئة الثانية")
 if(bmi>40):
  return ("يبدوا انك تعاني السمنة من الفئة الثالثة")

@DiagnoseRouter.get("/PSTD1")
def PSTD1():
    return ('هل تعاني من صعوبة في النوم أو التركيز ؟')
ps=0
ps1=0
ps2=0
ps3=0
@DiagnoseRouter.post("/PSTD2")
async def PSTD2(answer1:Answer):
   global ps
   if(answer1.answer=='نعم'):
    ps=1
    return ('هل تشاهد أحلام أو كوابيس مزعجة عن حدث حصل معك في الماضي؟')
   if(answer1.answer=='لا'):
     ps=2
     return('هل تحاول تجنب التفكير في حدث معين أو التحدث عنه؟')
   
@DiagnoseRouter.post("/PSTD3")
async def PSTD3(answer1:Answer):
  global ps1
  if(ps==1):
   if(answer1.answer=='نعم'):
    return ("يبدوا انك تعاني من اضطراب ما بعد الصدمة")
   if(answer1.answer=='لا'):
    ps1=1
    return ('هل تسترجع تفاصيل حدث وكأنه يحدث مرة أخرى معك؟')
  if(ps==2):
   if(answer1.answer=='نعم'):
    ps1=2
    return ('هل تشعر بأنك تفكر بشكل سلبي أو بتقلب في المزاج؟')
   if(answer1.answer=='لا'):
     return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")

@DiagnoseRouter.post("/PSTD4")
async def PSTD4(answer1:Answer):
 global ps2
 if(ps1==1):
   if(answer1.answer=='نعم'):
    return ("يبدوا انك تعاني من اضطراب ما بعد الصدمة")
   if(answer1.answer=='لا'):
    ps2=1
   return('هل تحاول تجنب التفكير في حدث معين أو التحدث عنه؟')
 if(ps1==2):
   if(answer1.answer=='نعم'):
    ps2=2
    return ('هل تعاني من نوبات غضب أو سلوك عدواني؟')
   if(answer1.answer=='لا'):
     return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")

@DiagnoseRouter.post("/PSTD5")
async def PSTD5(answer1:Answer):
 global ps3
 if(ps2==1):
   if(answer1.answer=='نعم'):
    ps3=1
    return ('هل تحاول تجنب الأماكن أو الأنشطة أو الأشخاص الذين يذكرونك بالحدث؟')
   if(answer1.answer=='لا'):
     return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
 if(ps2==2):
   if(answer1.answer=='نعم'):
    return ("يبدوا انك تعاني من اضطراب ما بعد الصدمة")
   if(answer1.answer=='لا'):
     return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
@DiagnoseRouter.post("/PSTD6")
async def PSTD6(answer1:Answer):
   if(ps3==1):
    if(answer1.answer=='نعم'):
     return ('هل تشعر بأنك تفكر بشكل سلبي أو بتقلب في المزاج؟')
    if(answer1.answer=='لا'):
      return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
@DiagnoseRouter.post("/PSTD7")
async def PSTD7(answer1:Answer):
   if(answer1.answer=='نعم'):
    return ('هل تعاني من نوبات غضب أو سلوك عدواني؟')
   if(answer1.answer=='لا'):
     return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
@DiagnoseRouter.post("/PSTD8")
async def PSTD8(answer1:Answer): 
    if(answer1.answer=='نعم'):
     return ("يبدوا انك تعاني من اضطراب ما بعد الصدمة")
    if(answer1.answer=='لا'):
     return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
m=0
@DiagnoseRouter.get("/Mood1")
def Mood1():
    return ('هل تشعر انك بمزاج سيء أو انك حزين؟')
@DiagnoseRouter.post("/Mood2")
async def Mood2(answer1:Answer): 
    global m
    if(answer1.answer=='نعم'):
     m += 1
    return ('هل تشعر بأرق أو فرط في النوم؟')
@DiagnoseRouter.post("/Mood3")
async def Mood3(answer1:Answer):
    global m 
    if(answer1.answer=='نعم'):
     m += 1
    return ('هل خسرت مؤخراً من وزنك؟')
@DiagnoseRouter.post("/Mood4")
async def Mood4(answer1:Answer): 
    global m
    if(answer1.answer=='نعم'):
     m += 1
    return ('هل تشعر بالخمول أو قلة التركيز؟')
@DiagnoseRouter.post("/Mood5")
async def Mood5(answer1:Answer): 
    global m
    if(answer1.answer=='نعم'):
     m += 1
    return ('هل تشعر بالذنب لأشياء فعلتها سابقاً؟')

@DiagnoseRouter.post("/Mood6")
async def Mood6(answer1:Answer): 
    global m
    if(answer1.answer=='نعم'):
        m += 1
    if(m > 3):
        return ("يبدوا انك تعاني من اضطراب اكتئاب شديد")
    else:
        return('هل تشعر بفرط في نشاطك؟')
n=0
@DiagnoseRouter.post("/Mood7")
async def Mood7(answer1:Answer): 
    global n
    n=0
    if(answer1.answer=='نعم'):
        n += 1
    return ('هل تشعر بأنك تثرثر بشمل غير عادي؟')
@DiagnoseRouter.post("/Mood8")
async def Mood8(answer1:Answer): 
    global n
    if(answer1.answer=='نعم'):
        n += 1
    return ('هل تشعر بانخفاض حاجتك إلى النوم؟')
@DiagnoseRouter.post("/Mood9")
async def Mood9(answer1:Answer): 
    global n
    if(answer1.answer=='نعم'):
        n += 1
    return ('هل تشعر بتسارع في أفكارك؟')

@DiagnoseRouter.post("/Mood10")
async def Mood10(answer1:Answer): 
    global n
    if(answer1.answer=='نعم'):
        n += 1
    return ('هل تعاني من سوء اتخاذ في قراراتك؟')

@DiagnoseRouter.post("/Mood11")
async def Mood11(answer1:Answer): 
    global n
    if(answer1.answer=='نعم'):
         n += 1
    return ('هل تشعر بانك في مزاج سيء او مكتئب؟')
@DiagnoseRouter.post("/Mood12")
async def Mood12(answer1:Answer): 
    global n
    if(answer1.answer=='نعم'):
           n += 1
    return ('هل تشعر بتعب وأرق متكرر؟')

@DiagnoseRouter.post("/Mood12")
async def Mood12(answer1:Answer): 
    global n
    if(answer1.answer=='نعم'):
         n += 1
    return ('هل تراودك مؤخراً أفكار انتحارية؟')
@DiagnoseRouter.post("/Mood13")
async def Mood13(answer1:Answer): 
    global n
    if(answer1.answer=='نعم'):
         n += 1
    return ('هل تشعر بفقدان المتعة أو بالذنب بأي شيء تفعله؟')
@DiagnoseRouter.post("/Mood14")
async def Mood14(answer1:Answer): 
    global n
    if(answer1.answer=='نعم'):
        n += 1
    if(n > 6):
        return ("يبدوا انك تعاني من اضطراب ثنائي القطب")
    else:
     return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")

@DiagnoseRouter.get("/PD1")
def PD1():
    return ('هل تشعر بصعوبة في التركيز؟')
c=0
@DiagnoseRouter.post("/PD2")
async def PD2(answer1:Answer): 
    global c
    c=0
    if(answer1.answer=='نعم'):
         c += 1
    return ('هل تشعر برغبة ببذل جهد أكبر في حياتك بشكل عام؟')

@DiagnoseRouter.post("/PD3")
async def PD3(answer1:Answer): 
    global c
    if(answer1.answer=='نعم'):
         c += 1
    return ('هل تشعر بصعوبة في تحمل المسؤولية؟ ')
@DiagnoseRouter.post("/PD4")
async def PD4(answer1:Answer): 
    global c
    if(answer1.answer=='نعم'):
         c += 1
    return ('هل تشعر بالعجز؟')
@DiagnoseRouter.post("/PD5")
async def PD5(answer1:Answer): 
    global c
    if(answer1.answer=='نعم'):
         c += 1
    return ('هل تشعر بالخوف والقلق المستمر من ترك من حوله لك؟')
@DiagnoseRouter.post("/PD6")
async def PD6(answer1:Answer): 
    global c
    if(answer1.answer=='نعم'):
         c += 1
    return ('هل تشعر بالحاجة الملحة للعلاقات دائماً؟')
@DiagnoseRouter.post("/PD7")
async def PD7(answer1:Answer): 
    global c
    if(answer1.answer=='نعم'):
        c += 1
    if(c > 4):
        return ("يبدوا انك تعاني من اضطراب الشخصية الاعتمادية")
    else:
      return('هل تتجنب التعامل مع الآخرين؟')
d=0
@DiagnoseRouter.post("/PD8")
async def PD8(answer1:Answer): 
    global d
    d=0
    if(answer1.answer=='نعم'):
         d += 1
    return ('هل تعاني من قلق التعرض للانتقاد؟')
@DiagnoseRouter.post("/PD9")
async def PD9(answer1:Answer): 
    global d
    if(answer1.answer=='نعم'):
         d += 1
    return ('هل تشعر بعدم الكفاءة؟')
@DiagnoseRouter.post("/PD10")
async def PD10(answer1:Answer): 
    global d
    if(answer1.answer=='نعم'):
         d += 1
    return ('هل تشعر بعدم الكفاءة للقيام بأي شيء؟')
@DiagnoseRouter.post("/PD11")
async def PD11(answer1:Answer): 
    global d
    if(answer1.answer=='نعم'):
         d += 1
    return ('هل تحاول البقاء وحيداً في أغلب الأوقات؟')
@DiagnoseRouter.post("/PD12")
async def PD12(answer1:Answer): 
    global d
    if(answer1.answer=='نعم'):
         d += 1
    return ('هل تتجنب العلاقات الجدية؟')
@DiagnoseRouter.post("/PD13")
async def PD13(answer1:Answer): 
    global d
    if(answer1.answer=='نعم'):
         d += 1
    return ('هل تتجنب أي عمل يتطلب التواصل الاجتماعي مع الأخرين؟')
@DiagnoseRouter.post("/PD14")
async def PD14(answer1:Answer): 
    global d
    if(answer1.answer=='نعم'):
        d += 1
    if(d > 4):
        return ("يبدوا انك تعاني من اضطراب الشخصية التجنبية")
    else:
      return('هل تشعر بصعوبة السيطرة على غضبك؟')
pd=0
@DiagnoseRouter.post("/PD15")
async def PD15(answer1:Answer): 
    global pd
    pd=0
    if(answer1.answer=='نعم'):
         pd += 1
    return('هل تشعر بالفراغ الدائم؟')
@DiagnoseRouter.post("/PD16")
async def PD16(answer1:Answer): 
    global pd
    if(answer1.answer=='نعم'):
         pd += 1
    return('هل تشعر بعدم استقرار وضعك العاطفي؟')
@DiagnoseRouter.post("/PD17")
async def PD17(answer1:Answer): 
    global pd
    if(answer1.answer=='نعم'):
         pd += 1
    return('هل تبذل جهود كبيرة تجنباً لهجر أحدهم لك؟')
@DiagnoseRouter.post("/PD18")
async def PD18(answer1:Answer): 
    global pd
    if(answer1.answer=='نعم'):
         pd += 1
    return('هل تشعر بفقدان الأعصاب نتيجة الغضب؟')
@DiagnoseRouter.post("/PD19")
async def PD19(answer1:Answer): 
    global pd
    if(answer1.answer=='نعم'):
         pd += 1
    return('هل تشعر بانك تتصرف بشكل طائش؟')
@DiagnoseRouter.post("/PD20")
async def PD20(answer1:Answer): 
    global pd
    if(answer1.answer=='نعم'):
         pd += 1
    return('هل تعاني من نمط غير مستقر من العلاقات العاطفية؟')
@DiagnoseRouter.post("/PD14")
async def PD14(answer1:Answer): 
    global pd
    if(answer1.answer=='نعم'):
        pd += 1
    if(pd > 4):
        return ("يبدوا انك تعاني من اضطراب الشخصية الحدية")
    else:
      return('هل تشعر بانك تستحق امتيازات ومعاملة خاصة؟')
s=0
@DiagnoseRouter.post("/PD21")
async def PD21(answer1:Answer): 
    global s
    s=0
    if(answer1.answer=='نعم'):
         s += 1
    return('هل تشعر بالاستياء الدائم من الآخرين؟')
@DiagnoseRouter.post("/PD22")
async def PD22(answer1:Answer): 
    global s
    if(answer1.answer=='نعم'):
         s += 1
    return('هل تشعر بعدم القدرة على تمييز احتياجات الآخرين ومشاعرهم؟')
@DiagnoseRouter.post("/PD23")
async def PD23(answer1:Answer): 
    global s
    if(answer1.answer=='نعم'):
         s += 1
    return('هل تشعر بانه يجب ان يفعل الآخرون ما تريده بدون طلب منهم ذلك؟')
@DiagnoseRouter.post("/PD24")
async def PD24(answer1:Answer): 
    global s
    if(answer1.answer=='نعم'):
         s += 1
    return('هل تصر بان تحصل على الأفضل في كل شيء رغم انك لا تملكه؟')

@DiagnoseRouter.post("/PD25")
async def PD25(answer1:Answer): 
    global s
    if(answer1.answer=='نعم'):
         s += 1
    return('هل تشعر بأنك الأفضل في كل شيء؟')
@DiagnoseRouter.post("/PD26")
async def PD26(answer1:Answer): 
    global s
    if(answer1.answer=='نعم'):
        s += 1
    if(s > 3):
        return ("يبدوا انك تعاني من اضطراب الشخصية النرجسية")
    else:
       return('هل تشعر بأنك عدواني أو حاد الطباع؟')
va=0
@DiagnoseRouter.post("/PD26")
async def PD26(answer1:Answer): 
    global va
    va=0
    if(answer1.answer=='نعم'):
         va += 1
    return('هل تشعر بأنك غير قادر على تحمل المسؤولية؟')
@DiagnoseRouter.post("/PD27")
async def PD27(answer1:Answer): 
    global va
    if(answer1.answer=='نعم'):
         va += 1
    return('هل ستفعل أي شيء للحصول على ما تريده؟')
@DiagnoseRouter.post("/PD28")
async def PD28(answer1:Answer): 
    global va
    if(answer1.answer=='نعم'):
         va += 1
    return('هل تشعر بأن رأيك هو الصحيح دائماً؟')
@DiagnoseRouter.post("/PD29")
async def PD29(answer1:Answer): 
    global va
    if(answer1.answer=='نعم'):
         va += 1
    return('هل تشعر بأن جميع من حولك غير مهم وان سعادتك الشخصية هي المهمة فقط؟')
@DiagnoseRouter.post("/PD30")
async def PD30(answer1:Answer): 
    global va
    if(answer1.answer=='نعم'):
        va += 1
    if(va > 3):
        return ("يبدوا انك تعاني من اضطراب الشخصية المعادية للمجتمع")
    else:
     return ("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
@DiagnoseRouter.post("/sys")
async def symptoms(answer1: Answer):
   if answer1.answer == '"يبدوا انك تعاني من الوسواس القهري"':
      return "الهواجس ، السلوكيات القهرية"
 
   if answer1.answer == '"يبدوا انك تعاني من نوبات الهلع"':
     return "خوف ، قلق ، زيادة ضربات القلب ، ضيق في التنفس ، ألم في الصدر ، تعرق شديد ، دوخة شديدة ،ارتجاف وقشعريرة "

   if answer1.answer == '"يبدو انك تعاني من اضطراب القلق عام"':
     return ("مشاكل في النوم ، مشاكل في التركيز ، تعب متكرر ، توتر ، قلق ، الالآم في العضلات")
   
   if answer1.answer == '"يبدوا انك تعاني من اضطراب الشخصية الاعتمادية"':
     return ("صعوبة التعبير ، الخوف ، الشعور بالعجز ، الرغبة في بذل جهد أكبر ، الحاجة الملحة للعلاقات")
   
   if answer1.answer == '"يبدوا انك تعاني من اضطراب الشخصية الحدية"':
     return ("صعوبة السيطرة على الغضب ، شعور مزمن بالفراغ ، عدم الاستقرار العاطفي  ، سلوك انتحاري ، اضطراب الهوية ، بذل جهود لتجنب الهجر ، الاندفاع")
   
   if answer1.answer == '"يبدوا انك تعاني من اضطراب الشخصية التجنبية"':
     return ("تجنب أي عمل يتطلب التواصل الاجتماعي ، قلق ، الخجل ، العزلة ، تجنب العلاقات الجدية ، السعور بعدم الكفاءة")
   
   if answer1.answer == "يبدوا انك تعاني من اضطراب الشخصية المعادية للمجتمع":
     return ("الانفعال والعدوانية ، عدم المسؤولية ، التهور ، الاندفاع ، خداع الآخرين")
   
   if answer1.answer == '"يبدوا انك تعاني من اضطراب الشخصية النرجسية"':
     return (" الاستياء من الآخرين ، عظمة الذات ، أوهام النجاح غير المتناهي ، الشعور بالاستحقاق الدائم ، السلوك القمعي ، عدم التعاطف ، الأنانية ، الغرور")
   
   if answer1.answer == '"يبدوا انك تعاني من اضطراب ثنائي القطب"':

     return ("تعب ، ارق ، أفكار انتحارية ، تردد ، فقدان متعة ، نشاط مفرط ، اكتئاب ")
   if answer1.answer == '"يبدوا انك تعاني من اضطراب اكتئاب شديد"':

     return ("فقدان وزن ، خمول ، شعور بالذنب ، قلة تركيز ، فرط نوم ، آرق")
   
   if answer1.answer == '"يبدوا انك تعاني من اضطراب ما بعد الصدمة"':

     return (" التعرض المباشر ، الإجهاد ، تغير في المزاج ، التجنب ")