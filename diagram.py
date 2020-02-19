import argparse
import re
from turtle import *


parser = argparse.ArgumentParser()
parser.add_argument('--type', help='Тип диаграммы')
parser.add_argument('--text', nargs='*', help='Текст для построения')
parser.add_argument('--colors', nargs='*', help='Цвета диаграммы')

type = parser.parse_args().type
text = parser.parse_args().text
colors = parser.parse_args().colors

font_size = 24
style = ('Arial', font_size, 'normal')
text = [re.sub(r'[^\w\s]', '', i) for i in text]
text = [i.casefold() for i in text]
text = [i for i in text if i != '']
result = {i: text.count(i) for i in text}
speed('fastest')
up()
goto(-200, 0)
down()

def round(angle, clr):
	begin_fill()    
	color(clr)
	circle(150, 360 / len(text) * angle)
	lt(90)
	fd(150)
	end_fill()
	lt(180)
	fd(150)
	lt(90)
	ht()

def linear(height, clr):
	begin_fill()
	color(clr)
	setheading(90)
	fd(800 / len(text) * height)
	right(90)
	fd(50)
	right(90)
	fd(800 / len(text) * height)
	end_fill()
	ht()

ind = 0
for x, y in result.items():
	if type == 'round':
		round(result[x], colors[ind])
		ind += 1
	elif type == 'linear':
		linear(result[x], colors[ind])
		ind += 1

up()
goto(100, 200)

index_of_colors = 0
for x, y in result.items():
	output = str(x) + ': ' + str(y)
	begin_fill()
	color(colors[index_of_colors])
	index_of_colors += 1
	write(output, font = style)
	goto(100, ycor() - (font_size + 10))
	end_fill()

mainloop()