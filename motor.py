import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin = [29,31,33,35]

for i in range(4):
	gpio.setup(pin[i],GPIO.OUT)

#GPIO.setup(pin5,GPIO.IN)

forward_seq = ['0011', '1001', '1100', '0110']
reverse_seq = ['0110', '1100', '1001', '0011']

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
	for i in range(4):
		GPIO.output(pin[i], step[i] == '1');
while True:
	select = raw_input("Select:")
	if select == 'A' or select == 'a':
#	input = GPIO.input(pin5)
#	if prev_input == 0 and input == 1:
		set_step('0000')
		print("2 steps forward, delay 10 milliseceonds")
		forward(0.01, int(720))
		prev_input = input;
	elif select == 'B' or select == 'b':
#	elif prev_input == 1 and input == 0:
		set_step('0000')
		print("2 steps reverse, delay 10 milliseceonds")
		reverse(0.01, int (720))
		prev_input = 0;
	else:
		GPIO.cleanup()
		exit();

