from passkey_gen import *
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App 
from kivy.graphics import Color,Rectangle,Ellipse,RoundedRectangle
from kivy.uix.togglebutton import ToggleButton,ToggleButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from strength_eval import evaluator

class Generator(FloatLayout):
    def __init__(self, **kwargs):
        super(Generator,self).__init__(**kwargs)
        self.base_button = Button(text='Generate passkey',size_hint=(.3,.15),pos_hint={'x':.2,'y':.02})
        self.base_button.background_color=(.2,.5,.6,.7)
        self.base_button.font_size ='50sp'
        self.base_button.font_name = 'C:\WINDOWS\FONTS\SNAP____.TTF'
        self.base_button.bind(on_press=self.generate)
        
        self.add_widget(self.base_button)
    

        self.text_box=text_box=TextInput(multiline=False,size_hint=(.1,.08),pos_hint={'x':.4,'y':.2})
        text_box.allow_copy =True
        text_box.background_color=(.3,.6,.7,.8)
        text_box.font_name='C:\WINDOWS\FONTS\SNAP____.TTF'
        text_box.font_size ='15sp'
        text_box.text_color=(0,1,1,0)
        self.add_widget(text_box)
        text_box.hint_text='Passkey length'
        text_box.hint_text_color=(1,1,1,1)
        

        self.strength = ProgressBar(max=6,size_hint=[.2,1], pos_hint={'x':.22,'y':0})
        #self.strength.value = 0
        
        
        self.strength_dscr = Label(text='',pos_hint={'x':-.22,'y':-.01},font_size='25sp',outline_color=(0,1,0),font_name = 'C:\WINDOWS\FONTS\SNAP____.TTF')
        self.strength_dscr.color=(1,0,0)
        self.pcheck = TextInput(multiline=False,size_hint=(.2,.08),pos_hint={'x':.219,'y':.55},hint_text='Test your passkey for strength',password=True)
        self.pcheck.password_mask='~'
        self.pcheck.font_name='C:\WINDOWS\FONTS\SNAP____.TTF'
        self.pcheck.font_size ='15sp'
        self.pcheck.background_color=(.6,.6,.7,.8)
        
        self.eval = Button(text='check strength',size_hint=(.1,.05),pos_hint={'x':.1,'y':.55})
        self.eval.background_color=(.2,.5,.6,.7)
        self.eval.font_size ='20sp'
        self.eval.font_name = 'C:\WINDOWS\FONTS\SNAP____.TTF'
        self.eval.bind(on_press=self.evAL)

   

             
        self.add_widget((self.strength))
        self.add_widget(self.strength_dscr)
        self.add_widget(self.pcheck)
        self.add_widget(self.eval)
        

        self.length_inst = Label(text='Enter the length of the desired passkey',markup=True,size_hint=(.1,.08),pos_hint={'x':.24,'y':.2})
        self.length_inst.font_name = 'C:\WINDOWS\FONTS\SNAP____.TTF'
        self.length_inst.font_size ='15sp'
        self.length_inst.outline_color=(0,0,0)
        self.length_inst.outline_width = '4sp'
        
        self.add_widget(self.length_inst)

        self.numbers=RadioButton(text='Numeric passkey',size_hint=(.1,.05),pos_hint={'x':0.08,'y':.28})
        self.numbers.group ='Type'
        self.numbers.font_name='C:\WINDOWS\FONTS\SNAP____.TTF'
        self.numbers.on_release = self.setState

        self.alphnum = RadioButton(text='Alphanumeric passkey',size_hint=(.1,.05),pos_hint={'x':0.08,'y':.2})
        self.alphnum.group ='Type'
        self.alphnum.font_name='C:\WINDOWS\FONTS\SNAP____.TTF'
        self.alphnum.on_release = self.set2

        self.legend =RadioButton(text='Legendary key',size_hint=(.1,.05),pos_hint={'x':0.08,'y':.1})
        self.legend.group ='Type'
        self.legend.font_name = 'C:\WINDOWS\FONTS\SNAP____.TTF'
        self.legend.on_release = self.set3

        self.clear = Button(text='Clear display',font_name='C:\WINDOWS\FONTS\SNAP____.TTF',size_hint=(.08,.05),pos_hint={'x':.6,'y':.02})
        
        self.clear.bind(on_press=self.clearer)
        self.add_widget(self.clear)

        self.add_widget(self.numbers)
        self.add_widget(self.alphnum)
        self.add_widget(self.legend)
        self.add_widget(Label(text='LordCipher',markup=True,font_size='150sp',font_name='C:\WINDOWS\FONTS\SNAP____.TTF',outline_color=(0.2,0.1,1),outline_width='4sp',pos_hint={'x':-.1,'y':.4}))
    
    def setState(self):
        self.state=state=1
        return state    
    def set2(self):
        self.state=state=2
        return state 
    def set3(self):
        self.state=state=3
        return state 
    def evAL(self,instance):
        kkk = self.pcheck.text
        self.strength.value=evaluator(kkk)/5
        if self.strength.value <= 2 :
            self.strength_dscr.text = 'Weak'
            self.strength_dscr.color=(1,0,0)
        elif self.strength.value >2 and self.strength.value<=4:
            self.strength_dscr.text = 'Strong'
            self.strength_dscr.color = (0,1,0)
        else:
            self.strength_dscr.text = 'Excellent'
            self.strength_dscr.color = (0,0,1)
            
    def generate(self,instance):
        global cheap_talk
        global new_key
        if self.numbers.state=='down':
            self.numb =(self.text_box.text)
            self.new_key=new_key=Label(text=num_only(self.numb),font_name='C:\WINDOWS\FONTS\SNAP____.TTF',font_size='20sp',pos_hint={'x':.2,'y':-.09})
        elif self.alphnum.state=='down':
            self.numb =(self.text_box.text)
            self.new_key=new_key=Label(text=alnum(self.numb),font_name='C:\WINDOWS\FONTS\SNAP____.TTF',font_size='20sp',pos_hint={'x':.2,'y':-.09})
        elif self.legend.state=='down':
            self.numb =(self.text_box.text)
            self.new_key=new_key=Label(text=strongest(self.numb),font_name='C:\WINDOWS\FONTS\SNAP____.TTF',font_size='20sp',pos_hint={'x':.2,'y':-.09})
        try:
            new_key.color=(0.4,.1,.1,.5)
            new_key.padding=[10,10]
        
        
        
            self.add_widget(new_key)
            cheap_talk=Label(text='Here you have your pass key\n use it to jealously guard\n all your accounts and files',font_name='C:\WINDOWS\FONTS\SNAP____.TTF',font_size='20sp',pos_hint={'x':.3,'y':.04})
            cheap_talk.color=(.8,.1,.51,1)
            if len(self.text_box.text) > 0 and self.text_box.text.isalpha() == False:
                self.add_widget(cheap_talk)
        except Exception as e:
            print(e)
    def clearer(self,instance):
        try:
            
            self.remove_widget(cheap_talk)
            
            self.remove_widget(new_key)
        except Exception as e:
            print(e)
            
        
     
class RadioButton(ToggleButton):
    def _do_press(self):
        if self.state=='normal':
            ToggleButtonBehavior._do_press(self)

class GenApp(App):
    def build(self):

        root =Generator()
        root.bind(size=self.update_shape,pos=self.update_shape)
        ext = Button(text='Exit',font_name='C:\WINDOWS\FONTS\SNAP____.TTF',size_hint=(.08,.05),pos_hint={'x':.8,'y':.02})
        ext.bind(on_press=self.stop)
        root.add_widget(ext)
        self.title = 'Lord Cipher'
        
        with root.canvas.before:
            Color(0.8,0.5,.8,1)
            self.shape = RoundedRectangle(size=(1000,1000))
            Color(0.8,.7,.8,1)
            self.sh = RoundedRectangle(size=(1920,350),pos=(0,0))
            Color(1,1,0,.1)
            self.b = RoundedRectangle(size=(770,56),pos=(974,380))
           
           
        return root
    def update_shape(self,instance,value):
        self.shape.pos = instance.pos
        self.shape.size = instance.size
        self.sh.pos = instance.pos
        #self.b.pos = instance.pos
        
    pass 

if __name__=='__main__':
    GenApp().run()