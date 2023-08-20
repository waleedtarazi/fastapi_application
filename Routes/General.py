from experta import *
import arabic_reshaper
class Symptom(Fact):
    pass



class GeneralTest(KnowledgeEngine):

    disorder = 'none'
    @Rule(NOT(Symptom(W())))
    def sendname(self):
     return ('أهلاً بك، هل يمكننا معرفة اسمك؟')
    def setsmoke(self,smo1):
         self.declare(Symptom(Name = smo1)) 
    @Rule(Symptom(Name = 'لا'))
    def illness1(self):
        return("يبدوا انك تعاني من نوبات الهلع")

    @Rule(Symptom(Name = 'نعم'))
    def sendlive(self):
        return("هل تسكن في الريف أو المناطق العشوائية؟ ")
 

    @Rule(Symptom(live = 'نعم'))
    def smooker(self): 
        return("هل تدخن أو تتعاطى مواد مدمنة؟")

    @Rule(Symptom(smoke = 'نعم'))
    def illness2(self):
        return("على ما يبدو انك تعاني من اضطرابات مزاج")

    @Rule(Symptom(live = 'لا'))
    def livingproblem(self):
        return("هل تواجه مشاكل في سكنك أو يمكنك الإحساس بإنه غير مستقر ؟")
  
    def setlive(self,liv1):
        self.declare(Symptom(Livingproblem = liv1))    
    @Rule(Symptom(Livingproblem = 'نعم'))
    def illness3(self):
        return("على ما يبدو انك تعاني من اضطرابات قلق")

    @Rule(OR(Symptom(Livingproblem = 'لا'), Symptom(smoke ='لا')))
    def Study(self):
        return(('هل أنت طالب في كلية أو معهد ؟'))

    @Rule(Symptom(Student = 'نعم'))
    def StudyDIFF2(self):
        return(('هل أنت قلق من الرسوب أو من الاستنفاذ؟'))
      
    @Rule(Symptom(fail = 'نعم'))
    def illness5(self):
        return("على ما يبدو انك تعاني من اضطرابات قلق")
    @Rule(Symptom(fail = 'لا'))
    def Army(self):
        return(('هل لديك جيش أو قلق بشأنه؟'))

    @Rule(Symptom(army = 'نعم'))
    def illness6(self):
        return("على ما يبدو انك تعاني من اضطرابات قلق")
    @Rule(OR(Symptom(army = 'لا'), Symptom(Student ='لا')))
    def Work1(self):
        return('هل تعمل؟')

    @Rule(Symptom(work = 'نعم'))
    def worknot(self):
        return(('هل عملك في تراجع وغير مستقر؟'))

    @Rule(Symptom(worknot = 'نعم'))
    def illness7(self):
        return("على ما يبدو انك تعاني من اضطرابات قلق")
    @Rule(Symptom(worknot = 'لا'))
    def Work2(self):
        return(('هل بيئة العمل تسبب لك تقلبات في المزاج؟'))

    @Rule(Symptom(plat = 'نعم'))
    def illness8(self):
        return("على ما يبدو انك تعاني من اضطرابات مزاج")

    @Rule(Symptom(work = 'لا'))
    def Work3(self):
        return(('هل تواجه صعوبات في إيجاد عمل؟'))

    @Rule(Symptom(workdifficulties = 'نعم'))
    def illness9(self):
        return("على ما يبدو انك تعاني من اضطرابات قلق")
    @Rule(OR(Symptom(workdifficulties = 'لا'), Symptom(plat ='لا')))
    def family(self):
        return('هل عائلتك على قيد الحياة؟')
    
    @Rule(Symptom(hfamily = 'نعم'))
    def hfamily(self):
        return(('هل علاقتك جيدة معهم؟'))
   
    @Rule(OR(Symptom(familyg = 'لا'), Symptom(familyg ='نعم')))
    def familyg(self):
        return(('هل  كانت حياتك غير مستقرة أو فوضوية أثناء الطفولة'))

    @Rule(Symptom(familypr = 'نعم'))
    def illness11(self):
        return("على ما يبدو انك تعاني من اضطرابات شخصية")

    @Rule(OR(Symptom(hfamily = 'لا'), Symptom(familypr ='لا')))
    def Married(self):
        return(('هل أنت متزوج؟'))

    @Rule(Symptom(married = 'لا'))
    def marry1(self):
        return('هل تراودك أفكار الزواج كثيراً وتسبب لك مشاكل؟')

    @Rule(Symptom(notmaryp = 'نعم'))
    def illness12(self):
        return("على ما يبدو انك تعاني من اضطرابات قلق")    
    @Rule(Symptom(married = 'نعم'))
    def marry(self):
        return('هل علاقتك جيدة معها؟')

    @Rule(Symptom(notgood = 'نعم'))
    def marry3(self):
        return('هل تشعر أحيانا بالندم على زواجك وفي الأحيان الأخرى تكون سعيداً؟')

    @Rule(Symptom(res1 = 'نعم'))
    def illness13(self):
     return("على ما يبدو انك تعاني من اضطرابات مزاج")

    @Rule(Symptom(notgood = 'لا',res1= 'لا'))
    def marry24(self):
        return('هل لديك أطفال؟')

    @Rule(Symptom(res3 = 'لا'))
    def marry4(self):
        return('هل يسبب ذلك لك مشكلة؟')

    @Rule(Symptom(res4 = 'نعم'))
    def illness14(self):
        return("على ما يبدو انك تعاني من اضطرابات قلق")

    @Rule(Symptom(res3 = 'نعم'))
    def marry23(self):
        return('هل علاقتك جيدة معهم؟')
 
  
    @Rule(Symptom(res5 = 'لا'))
    def illness15(self):
        return("على ما يبدو انك تعاني من اضطرابات شخصية")
     # ! call the Mood-Disorder rate  
    @Rule(OR(Symptom(res5 = 'نعم'), Symptom(res4 ='لا'), Symptom(notmaryp ='لا')))
    def pd1(self):
        return('هل تعرضت لصدمة شديدة في حياتك؟')

    @Rule(Symptom(res6 = 'نعم'))
    def pd2(self):
        return('هل  تشاهد كوابيس، أو تواجه صعوبة في النوم؟')

    @Rule(Symptom(res7 = 'نعم'))
    def illness16(self):
        return("على ما يبدو انك تعاني من اضطرابات الصدمة")

    @Rule(OR(Symptom(res7 = 'لا'), Symptom(res6 ='لا')))
    def food(self):
        return('هل تعاني من مشاكل بسبب الوزن الزائد أو النحافة الزائدة؟')
       
    @Rule(Symptom(res8 = 'نعم'))
    def pd24(self):
        return('هل لديك سلوكيات طعام غير طبيعية؟')

    @Rule(Symptom(res9 = 'نعم'))   
    def illness17(self):
        return("على ما يبدو انك تعاني من اضطرابات طعام")

    @Rule(OR(Symptom(res8 = 'لا'), Symptom(res9 ='لا')))
    def illnessfinal(self):
        return("يبدوا انك لا تعاني من شيء مجرّد قلق بسيط يمكنك أخذ قسطاً من الراحة لتعود طبيعياً")
     
      