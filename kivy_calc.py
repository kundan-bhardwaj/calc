import kivymd
import math
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
import PIL
import random
from kivy.uix.videoplayer import VideoPlayer
import webbrowser
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition

screen_helper = """
#: import NoTransition kivy.uix.screenmanager.NoTransition
ScreenManager:
	id: screen_manager
	MenuScreen:
	otherscreen:
<txt>:
<MenuScreen>:
	name: 'menu'
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
        		        title: 'Calculator0'
        		        type: 'top'
			            left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
			            elevation:10
			        txt:
			        	text: app.the_text
			        	id: tex
			        	height: 40
			        	multiline: True
			        	font_size: 80	
			        GridLayout:
				    	cols: 4
				        padding: 40
				        spacing: 20
				        size_hint:1,3
				        MDFillRoundFlatButton:
				        	text: ' 1 '
				            bg_color : 'green'
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='1'
				        MDFillRoundFlatButton:
				        	text: ' 2 '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+= '2'		        	
				        MDFillRoundFlatButton:
				        	text: ' 3 '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='3'				        	
				        MDFillRoundFlatButton:
				        	text: ' + '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='+'				        	
				        MDFillRoundFlatButton:
				        	text: ' 4 '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='4'				        	
				        MDFillRoundFlatButton:
				        	text: ' 5 '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='5'				        	
				        MDFillRoundFlatButton:
				        	text: ' 6 '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='6'			        	
				        MDFillRoundFlatButton:
				        	text: ' × '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='*'				        	
				        MDFillRoundFlatButton:
				        	text: ' 7 '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='7'				        	
				        MDFillRoundFlatButton:
				        	text: ' 8 '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='8'				        	
				        MDFillRoundFlatButton:
				        	text: ' 9 '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='9'
				        MDFillRoundFlatButton:
				        	text: '  -  '
				        	height: 160
				        	font_size: 32
				        	bold: True
				        	on_press:app.the_text+='-'
				        MDFillRoundFlatButton:
				        	text: 'AC'
				        	height: 160
				        	font_size: 35
				        	bold: True
				        	on_press:app.the_text =''
				        MDFillRoundFlatButton:
				        	text: ' 0 '
				        	height: 160
				        	font_size: 35
				        	bold: True
				        	on_press:app.the_text +='0'
				        MDFillRoundFlatButton:
				        	text: ' C '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:
				        		app.the_text=app.the_text[0:len(app.the_text)-1]
				        MDFillRoundFlatButton:
				        	text: ' = '
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press: app.the_text=str(eval(str(app.the_text)))
				    MDFillRoundFlatButton:
				        text: '       more items      '
				        height: 120
				        font_size: 30
				        bold: True
				        pos_y : 600
				        pos_hint: {'center_x':0.5,'center_y':0.5}
				        on_press:
				        	root.manager.current='other'
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
			        	size_hint_y: None
			        	bold: True
			        	pos_hint:{'center_x':0.6,'center_y':10}
			        	font_colour: "blue"
				    MDLabel:
			        	font_size: 40
			        	size_hint_y: None
			        	bold: True
			        	pos_hint:{'center_x':0.6,'center_y':10}				    	
				    	text: 'Just Because of good    guidelines from "Amit Sir"'
<otherscreen>:
	name: 'other'
	tex: tex
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'   
                    MDToolbar:
        		        title: 'Calculator'
        		        type: 'top'
			            left_action_items: [['arrow-left',lambda x: root.ch_sc()]]
			            elevation:10
			        txt:
			        	text: app.the_text
			        	id: tex
			        	height: 400
			        	multiline: True
			        	font_size: 80	
			        GridLayout:
				    	cols: 5
				        padding: 40
				        spacing: 20
				        size_hint : 1,3
				        MDFillRoundFlatButton:
				        	text: '+'
				            bg_color : 'green'
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='+'
				        MDFillRoundFlatButton:
				        	text: '-'
				        	height: 160
				        	font_size: 80
				        	bold: True
				        	on_press:app.the_text+= '-'		        	
				        MDFillRoundFlatButton:
				        	text: '×'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='*'
				        MDFillRoundFlatButton:
				        	text: '/'
				        	height: 160
				        	font_size: 50
				        	bold: True
				        	on_press:app.the_text+='/'
				        MDFillRoundFlatButton:
				        	text: 'C'
				        	height: 160
				        	font_size: 35
				        	bold: True
				        	on_press:
				        		app.the_text=app.the_text[0:len(app.the_text)-1]
				        MDFillRoundFlatButton:
				        	text: '1'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='1'
				        MDFillRoundFlatButton:
				        	text: '2'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='2'
				        MDFillRoundFlatButton:
				        	text: '3'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='3'
				        MDFillRoundFlatButton:
				        	text: '4'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='4'   		
				        MDFillRoundFlatButton:
				        	id: 'factorial'
				        	text: ' ! '
				        	height: 160
				        	font_size: 30
				        	bold: True
				        	on_press:app.the_text+='!'				        	
				        MDFillRoundFlatButton:
				        	text: '5'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='5'				        	
				        MDFillRoundFlatButton:
				        	text: '6'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='6'
				        MDFillRoundFlatButton:
				        	text: '7'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='7'
				        MDFillRoundFlatButton:
				        	text: '.'
				        	height: 160
				        	font_size: 80
				        	bold: True
				        	on_press:app.the_text+='.'				        	
				        MDFillRoundFlatButton:
				        	text: '8'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='8'			        	
				        MDFillRoundFlatButton:
				        	text: '√'
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='√'				        	
				        MDFillRoundFlatButton:
				        	text: '9'
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='9'
				        MDFillRoundFlatButton:
				        	text: '0'
				        	height: 160
				        	font_size: 45
				        	bold: True
				        	on_press:app.the_text+='0'
				        MDFillRoundFlatButton:
				        	text: '7'
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='7'				        	
				        MDFillRoundFlatButton:
				        	text: '√'
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:app.the_text+='√'
				        MDFillRoundFlatButton:
				        	text: 'sin'
				        	height: 160
				        	font_size: 20
				        	bold: True
				        	on_press:app.the_text+='sin('
				        MDFillRoundFlatButton:
				        	text: 'cos'
				        	height: 160
				        	font_size: 18
				        	bold: True
				        	on_press:app.the_text+='cos('
				        MDFillRoundFlatButton:
				        	text: 'tan'
				        	height: 160
				        	font_size: 20
				        	bold: True
				        	on_press:app.the_text+='tan('
				        MDFillRoundFlatButton:
				        	text: 'AC'
				        	height: 160
				        	font_size: 24
				        	bold: True
				        	on_press:app.the_text =''
				        MDFillRoundFlatButton:
				        	text: '='
				        	height: 160
				        	font_size: 40
				        	bold: True
				        	on_press:root.calc()		    	
"""
class MenuScreen(Screen):
	pass
class otherscreen(Screen):
	the_text=StringProperty()
	def calc(self):
		b=self.ids.tex.text
		for i in ("+","-","/","*"):
			if i in b:
				for j in ('!','√'):
					if j in b:
						break
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
			u=m
			print(m)
			for i in ("+","-","*","/"):
				while b[u]!=i:
					u=u+1
			print(u)
			k=""
			k=b[m:u+1]
			f=str(math.sqrt(int(k)))
			print(f)
			b[s]=f
			b=b.remove(l)
			if "!" not in b:
				if "√" not in b:
					MDApp.get_running_app().the_text=str(eval(b))
	def ch_sc(self):
		MDApp.get_running_app().root.current = "menu"				
class txt(TextInput):
	pass
class DemoApp(MDApp):
    the_text=StringProperty()
    def build(self):
    	l=[ 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'Green']
    	self.theme_cls.primary_palette = random.choice(l)
    	screen=Builder.load_string(screen_helper)
    	return screen
    def value(self):
    	b = root.ids.txt.text
if __name__ == "__main__":
	DemoApp().run()