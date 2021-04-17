import kivy
import kivymd
import math
import random
from kivy.core.audio import SoundLoader
from fractions import Fraction
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

screen_helper = """
ScreenManager:
	id: screen_manager
	MenuScreen:
<txt>:
<MenuScreen>:
	name: 'menu'
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
        		        title: 'Calculator'
        		        type: 'top'
			            left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
			            elevation:10
			        MDTextField:
			        	text: app.the_text
			        	id: tex
			        	width: 500
			        	multiline: True
						font_size: 50
						mode: 'rectangle'
				        size_hint: 2,0.4
				        padding_x: 10
				        text_color: 0,0,0,1
			        GridLayout:
				    	cols: 5
				    	spacing: 20
				    	padding:15
				        size_hint: 0,1
				        MDFillRoundFlatButton:
				        	text: '+'
				        	font_size: 50
	                        size: 10, 120
                            size_hint: None, None
				        	bold: True
				        	on_press:
				        		app.the_text+='+'
				        MDFillRoundFlatButton:
				        	text: ' - '
				        	height: 120
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+= '-'		        	
				        MDFillRoundFlatButton:
				        	text: '×'
				        	height: 120
				        	font_size: 50
				        	bold: True
				        	on_press:app.the_text+='×'
				        MDFillRoundFlatButton:
				        	text: '÷'
				        	height: 120
				        	font_size: 50
				        	bold: True
				        	on_press:app.the_text+='÷'
				        MDIconButton:
				        	icon: 'close-circle-outline'
				        	height: 120
				        	on_press:
				        		app.the_text=app.the_text[0:len(app.the_text)-1]
				        MDFillRoundFlatButton:
				        	text: '1'
				        	height: 120
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='1'
				        MDFillRoundFlatButton:
				        	text: '2'
				        	height: 120
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='2'
				        MDFillRoundFlatButton:
				        	text: '3'
				        	height: 120
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='3'
				        MDFillRoundFlatButton:
				        	text: 'sin'
				        	height: 120
				        	font_size: 20
				        	bold: True
				        	on_press:app.the_text+='sin('   		
				        MDFillRoundFlatButton:
				        	id: 'factorial'
				        	text: ' ! '
				        	height: 120
				        	font_size: 30
				        	bold: True
				        	on_press:app.the_text+='!'
				        MDFillRoundFlatButton:
				        	text: '4'
				        	height: 120
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='4'				        	
				        MDFillRoundFlatButton:
				        	text: '5'
				        	height: 120
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='5'				        	
				        MDFillRoundFlatButton:
				        	text: '6'
				        	height: 120
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='6'
				        MDFillRoundFlatButton:
				        	text: 'cos'
				        	height: 120
				        	font_size: 18
				        	bold: True
				        	on_press:app.the_text+='cos('
				        MDFillRoundFlatButton:
				        	text: '√'
				        	height: 120
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='√'
				        MDFillRoundFlatButton:
				        	text: '7'
				        	height: 120
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='7'
						MDFillRoundFlatButton:
							text: '8'
							height: 120
							font_size: 40
							bold: True
							on_press: app.the_text+='8'
				        MDFillRoundFlatButton:
				        	text: '9'
				        	height: 120
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='9'
				        MDFillRoundFlatButton:
				        	text: 'tan'
				        	height: 120
				        	font_size: 20
				        	bold: True
				        	on_press:app.the_text+='tan('
						MDFillRoundFlatButton:
				        	text: '.'
				        	height: 120
				        	font_size: 80
				        	bold: True
				        	on_press:app.the_text+='.'
				        MDFillRoundFlatButton:
				        	text: 'AC'
				        	height: 120
				        	font_size: 20
				        	bold: True
				        	on_press:app.the_text =''
				        MDFillRoundFlatButton:
				        	text: '0'
				        	height: 120
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='0'
				        MDFillRoundFlatButton:
				        	text: '='
				        	height: 120
				        	font_size: 40
				        	bold: True
				        	on_press:root.calc()
				        MDFillRoundFlatButton:
				        	text: 'log'
				        	height: 120
				        	font_size: 20
				        	bold: True
				        	on_press:app.the_text+='log('
				        MDFillRoundFlatButton:
				        	text: 'rad'
				        	height: 120
				        	font_size: 18
				        	bold: True
				        	on_press:app.the_text+='rad('
				        MDFillRoundFlatButton:
				        	text: 'pow'
				        	height: 120
				        	font_size: 12
				        	bold: True
				        	on_press:app.the_text+="^"
        MDNavigationDrawer:
		    id:nav_drawer
		    BoxLayout:
		    	orientation:'vertical'
		    	spacing: 5
		    	AnchorLayout:
		    		anchor_x: 'left'
		    		
			    	AsyncImage:
			            source: "https://docs.google.com/drawings/d/e/2PACX-1vRkvtzEjtx2co6erguiMrBIIdiEToMXLdIqOslHXNUXix89AJpyWGP-HwrI2XAy0Spd6uvxfyVCx6uI/pub?w=480&h=360"
			    BoxLayout:
			        orientation :'vertical'
			        MDLabel:
			        	text: 'Created By Kundan Bhardwaj'
			        	font_style: 'Overline'
			        	font_size: 40
			        	bold: True
			        	pos_hint:{'center_x':0.6,'center_y':0.5}
			        	font_colour: "blue"
				    MDLabel:
			        	font_size: 40
			        	bold: True
			        	pos_hint:{'center_x':0.6,'center_y':0.5}				    	
				    	text: 'Just Because of    guidelines     and support from "Amit Sir"'
"""
class txt(TextInput):
	pass
class MenuScreen(Screen):
	the_text=StringProperty()
	def calc(self):
		b=self.ids.tex.text
		if "×" in b :
			def aud():
				sound=SoundLoader.load("click.wav")
				sound.play()			
			b=b.replace("×","*")
		if "÷" in b :
			b=b.replace("÷","/")
		if "!" not in b:
			if "√" not in b:
				if "sin(" not in b:
					if "cos(" not in b:
						if "tan(" not in b:
							if "log(" not in b:
								if "rad(" not in b:
									MDApp.get_running_app().the_text=str(eval(b))	
		while "!" in b:
			a=list(b)
			s=a.index("!")
			print(a)
			m=s-1
			r=m
			e=0
			k=e
			while a[r].isdigit == True:
				e=r-t
				t=t+1
			print(k)
			l=""
			for i in range(k,s):
				l=l+(a[i])
			print(l)
			op=""
			for i in ("+","-","/","*"):
				while i in l:
					op=i
					g=len(l)-1
					while l[g].isdigit==True:
						g=g-1
					y=l[g]
					h=l[g:len(l)]
					f=str(math.factorial(int(h)))
					print(h)
					del a[r]
					print(a)
					fa=a.index("!")
					a[fa]=f
					print(a)
					w = ''.join(map(str, a))
					b=w	
					if "!" not in b:
						if "√" not in b:
							MDApp.get_running_app().the_text=str(eval(b))
							break
			if "!" in b:
				f=str(math.factorial(int(l)))
				print(f)
				a[s]=f
				while a[k]!=f:
					print(a[k])
					del a[k]
				print(a)
				w = ''.join(map(str, a))
				b=w
			if "!" not in b:
				if "√" not in b:
					MDApp.get_running_app().the_text=str(eval(b))
		while "√" in b:
			s=b.find("√")
			print(b)
			print(s)
			m=s+1
			t=m
			while  t<=len(b)-1 and b[t].isdigit()==True :
				t=t+1
			print(t)
			k=""
			k=b[m:t]
			f=str(math.sqrt(int(k)))
			print(f)
			b=b.replace("√",f)
			b=b.replace(k,"")
			if "!" not in b:
				if "√" not in b:
					MDApp.get_running_app().the_text=str(eval(b))
		while "si" in b:
			l=list(b)
			s=b.find("si")
			print(b)
			print(s)
			m=s+4
			t=m
			while  t<len(b) and b[t].isdigit()==True :
				t=t+1
			print(t)
			k=""
			k=b[m:t]
			f=str(math.sin(math.radians(int(k))))
			print(f)
			b=b.replace("si",f)
			b=b.replace(k,"")
			b=b.replace("n","")
			b=b.replace("(","")				
			if "!" not in b:
				if "√" not in b:
					MDApp.get_running_app().the_text=str(eval(b))
		while "c" in b:
			l=list(b)
			s=b.find("c")
			print(b)
			print(s)
			m=s+4
			t=m
			while  t<len(b) and b[t].isdigit()==True :
				t=t+1
			print(t)
			k=""
			k=b[m:t]
			f=str(math.cos(math.radians(int(k))))
			print(f)
			b=b.replace("c",f)
			b=b.replace(k,"")
			b=b.replace("o","")
			b=b.replace("s","")
			b=b.replace("(","")				
			if "!" not in b:
				if "√" not in b:
					MDApp.get_running_app().the_text=str(eval(b))
		while "t" in b:
			l=list(b)
			s=b.find("t")
			print(b)
			print(s)
			m=s+4
			t=m
			while  t<len(b) and b[t].isdigit()==True :
				t=t+1
			print(t)
			k=""
			k=b[m:t]
			f=str(math.tan(math.radians(int(k))))
			print(f)
			b=b.replace("t",f)
			b=b.replace(k,"")
			b=b.replace("a","")
			b=b.replace("n","")
			b=b.replace("(","")				
			if "!" not in b:
				if "√" not in b:
					MDApp.get_running_app().the_text=str(eval(b))
		while "lo" in b:
			l=list(b)
			s=b.find("lo")
			print(b)
			print(s)
			m=s+4
			t=m
			while  t<len(b) and b[t].isdigit()==True :
				t=t+1
			print(t)
			k=""
			k=b[m:t]
			f=str(math.log(int(k)))
			print(f)
			b=b.replace("lo",f)
			b=b.replace(k,"")
			b=b.replace("g","")
			b=b.replace("(","")				
			if "!" not in b:
				if "√" not in b:
					MDApp.get_running_app().the_text=str(eval(b))
		while "r" in b:
			l=list(b)
			s=b.find("r")
			print(b)
			print(s)
			m=s+4
			t=m
			while  t<len(b) and b[t].isdigit()==True :
				t=t+1
			print(t)
			k=""
			k=b[m:t]
			f=str(math.radians(int(k)))
			print(f)
			b=b.replace("r",f)
			b=b.replace(k,"")
			b=b.replace("a","")
			b=b.replace("d","")			
			b=b.replace("(","")				
			if "!" not in b:
				if "√" not in b:
					MDApp.get_running_app().the_text=str(eval(b))
	def ch_sc(self):
		MDApp.get_running_app().root.current = "menu"				
class DemoApp(MDApp):
    the_text=StringProperty()
    def build(self):
    	l=['Indigo','Teal','Purple', 'DeepPurple', 'Blue',]
    	self.theme_cls.primary_palette = random.choice(l)
    	screen=Builder.load_string(screen_helper)
    	return screen
    def value(self):
    	b = root.ids.txt.text    	
    	if "×" in b :
    		b=b.replace("×","*")
DemoApp().run()