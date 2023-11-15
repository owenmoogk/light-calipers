import serial
import pygame, math

def main():
	# configure arduino
	global arduino
	arduino = serial.Serial('COM9', 9600)
	arduino.reset_input_buffer()
	data_list = []
	moving_average = 0
			

	pygame.init()
	screen = pygame.display.set_mode((400, 300))
	font = pygame.font.Font(None, 36)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		data = arduino.readline().decode("utf-8")
		data_value = float(data)

		# Append the data to the list
		data_list.append(data_value)

		# Keep the last 20 elements
		if len(data_list) > 20:
				data_list = data_list[-20:]

		# Calculate the moving average
		moving_average = sum(data_list) / len(data_list)

		# Print the moving average
		print(f"Current moving average: {moving_average}")
		print("Incoming Data: " + data, end='')
							
		screen.fill((255, 255, 255))
		data_value = data_value/1024.0*5*(-4.5844)+22.226
		data_value = math.floor(data_value * 1000) / 1000.0
		# Render the moving average number to the screen
		text = font.render(f"{data_value} +/- 1.05 [cm]", True, (0, 0, 0))
		screen.blit(text, (50, 50))

		# Update the display
		pygame.display.flip()

if __name__ == '__main__':
	main()