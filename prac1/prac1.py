from manim import*
from math import*
from random import*
import numpy as np

config.background_color = YELLOW_A

class Scene1(Scene):
    def construct(self):
        v0 = 2.5
        g = 1.5*DOWN
        dt = 1/60
        class Particle():
            def __init__(self, cir):
                self.cpos = cir.get_center()
                theta = random()*2*PI
                self.ppos = self.cpos - v0*cos(theta)*dt*RIGHT - v0*sin(theta)*dt*UP
            def iterate(self, cir):
                res = VGroup()
                cir.shift(self.cpos-self.ppos)
                temp = self.cpos
                self.cpos = 2*self.cpos - self.ppos + g*dt*dt
                self.ppos = temp
                dist = sqrt(np.dot(self.cpos, self.cpos))
                if(dist>3):
                    nor = self.cpos[0]/dist*RIGHT + self.cpos[1]/dist*UP
                    self.cpos -= 2*(np.dot((self.cpos-self.ppos), nor))*nor
                res.add(cir)
                return res
                
        circ1 = Circle(radius=0.2, color=DARK_GRAY, fill_color=DARK_GRAY, fill_opacity=1)
        room = Circle(radius = 3 + circ1.width/2, color = DARK_GRAY)
        text1 = Text("A cricket in a circular cage :))", color=BLACK, font_size=40)
        part1 = Particle(circ1)
        self.play(Write(text1))
        self.wait(0.5)
        self.play(Unwrite(text1))
        self.play(Write(room), run_time = 0.5)
        self.play(FadeIn(circ1), run_time = 0.5)
        self.play(UpdateFromFunc(circ1, part1.iterate), run_time=45)
        

                
                


