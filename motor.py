import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin1 = 14
pin2 = 15
pin3 = 17
pin4 = 18
pin5 = 23

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)
GPIO.setup(pin5,GPIO.IN)

forward_seq = ['1010', '0110', '0101', '1001']
reverse_seq = ['1001', '0101', '0110', '1010']

def forward(delay,steps):
	for i in range(steps):
		for step in forward_seq:
			set_step(step)
			print(step)
			time.sleep(delay)
def reverse(delay,steps):
	for i in range(steps):
		for step in reverse_seq:
			set_step(step)
			print(step)
			time.sleep(delay)
def set_step(step):
		GPIO.output(pin1, step[0] == '1');
		GPIO.output(pin2, step[1] == '1');
		GPIO.output(pin3, step[2] == '1');
		GPIO.output(pin4, step[3] == '1');
while True:
#	select = raw_input("Select:")
#	if select == 'A' or select == 'a':
	input = GPIO.input(pin5)
	if input:
		set_step('0000')
		print("2 steps forward, delay 10 milliseceonds")
		forward(int(10) / 1000.0 , int(2))
		prev_input = input;
	elif prev_input == 1 and input == 0:
		set_step('0000')
		print("2 steps reverse, delay 10 milliseceonds")
		reverse(int(10) / 1000.0, int (2))
		prev_input = 0;

