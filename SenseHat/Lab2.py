from sense_emu import SenseHat
import time
from fastapi import FastAPI
from pydantic import BaseModel

OFFSET_LEFT = 1
OFFSET_TOP = 2

settings = {
"temperature" : "up",
"humidity" : "right",
"pressure" : "left"
}
class Settings(BaseModel):
    temperature : str
    humidity : str
    pressure : str

NUMS =[[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1],  # 0
       [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],  # 1
       [1,1,1,0,0,1,0,1,0,1,0,0,1,1,1],  # 2
       [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1],  # 3
       [1,0,0,1,0,1,1,1,1,0,0,1,0,0,1],  # 4
       [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1],  # 5
       [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1],  # 6
       [1,1,1,0,0,1,0,1,0,1,0,0,1,0,0],  # 7
       [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1],  # 8
       [1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]]  # 9

red = (255,0,0)
green = (24,252,0)
blue = (0,0,255)
yellow = (255,255,0)

def show_digit(val, offset_left, offset_top, r, g, b):
    table_used = NUMS[val]
    y = -1
    for i in range(0,15):
        x = i % 3
        if x == 0:
            y = y + 1
        sense.set_pixel(offset_left+x,offset_top+y,r*table_used[i], g*table_used[i], b*table_used[i])

def show_number(val, r, g, b):
    abs_val = abs(val)
    tens = abs_val // 10
    units = abs_val % 10
    print("tens",tens)
    print("units",units)
    print("val",val)
    if abs_val > 9:
        show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
    show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)

def show_number_of_cells(val, r, g, b):
    counter = 0
    for i in range(0,8):
        for j in range(0,8):
            if counter < val:
                sense.set_pixel(i,j,r,g,b)
                counter = counter + 1
            else:
                break

def reset_screen():
    for i in range(0,8):
        for j in range(0,8):
            sense.set_pixel(i,j,0, 0, 0)
sense = SenseHat()
sense.clear()

def do_thing(event):
    if event.action == 'pressed':
        if event.direction == settings['temperature'] :
                reset_screen()
                temperature = 0
            #while True:
                #if sense.temp != temperature:
                #    reset_screen()
                temperature = sense.temp
                show_number(int(temperature),240,255,240)
                if temperature < 0:
                    for i in range (0,8):
                        sense.set_pixel(i,7,blue)
                else:
                    for i in range (0,8):
                        sense.set_pixel(i,0,red)
                time.sleep(1)
        elif event.direction == settings['humidity']:
            reset_screen()
            humidity = sense.get_humidity()
            # 1.56 to jeden kafelek
            number_of_cells = 0.0 + humidity / 1.56
            #print("number_of_cells:",number_of_cells)
            show_number_of_cells(number_of_cells,255,255,0)
        elif event.direction == settings['pressure']:
            reset_screen()
            pressure = sense.get_pressure()
            # 1.56 to jeden kafelek
            number_of_cells = 0.0 + pressure / 15.6
            #print("number_of_cells:",number_of_cells)
            show_number_of_cells(number_of_cells,24,252,0)
        print(event.direction)

app = FastAPI()

@app.get("/device")
def device_definition():
    return {"message":"enviornment app"}

@app.get("/settings")
def show_settings():
    return settings

@app.post("/settings")
def set_settings(record : Settings):
    if (record.temperature != record.humidity) and (record.temperature != record.pressure) and (record.humidity != record.pressure) :
        settings["temperature"] = record.temperature
        settings["humidity"] = record.humidity
        settings["pressure"] = record.pressure
        return settings

sense.stick.direction_any = do_thing
#while True:
#    pass

sense.clear()


