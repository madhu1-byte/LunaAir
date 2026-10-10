from machine import ADC, Pin, I2C
from lcd_i2c import LCD
import time

# Initialize temperature sensor
adc = ADC(4)

# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)

# Initialize LCD
lcd = LCD(addr=0x27, cols=16, rows=2, i2c=i2c)
lcd.begin()

while True:

    # Read temperature sensor
    ADC_voltage = adc.read_u16() * (3.3 / 65535)

    # Convert voltage to Celsius
    temperature_celsius = 27 - (ADC_voltage - 0.706) / 0.001721

    # Convert Celsius to Fahrenheit
    temperature_fahrenheit = 32 + (1.8 * temperature_celsius)

    # Display temperature on LCD
    lcd.clear()
    lcd.print("Temperature")

    lcd.set_cursor(0, 1)
    lcd.print("Temp: {:.1f} F".format(temperature_fahrenheit))

    # Print to Thonny
    print("Temperature: {:.2f} C | {:.2f} F".format(
        temperature_celsius,
        temperature_fahrenheit
    ))

    time.sleep(1) 
