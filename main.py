def my_function():
    radio.send_number(10)
Kitronik_Game_Controller.on_button_press(Kitronik_Game_Controller.ControllerButtonPins.RIGHT,
    Kitronik_Game_Controller.ControllerButtonEvents.UP,
    my_function)

def my_function2():
    radio.send_number(6)
Kitronik_Game_Controller.on_button_press(Kitronik_Game_Controller.ControllerButtonPins.DOWN,
    Kitronik_Game_Controller.ControllerButtonEvents.UP,
    my_function2)

def my_function3():
    radio.send_number(5)
Kitronik_Game_Controller.on_button_press(Kitronik_Game_Controller.ControllerButtonPins.DOWN,
    Kitronik_Game_Controller.ControllerButtonEvents.DOWN,
    my_function3)

def my_function4():
    radio.send_number(8)
Kitronik_Game_Controller.on_button_press(Kitronik_Game_Controller.ControllerButtonPins.LEFT,
    Kitronik_Game_Controller.ControllerButtonEvents.UP,
    my_function4)

def my_function5():
    radio.send_number(3)
Kitronik_Game_Controller.on_button_press(Kitronik_Game_Controller.ControllerButtonPins.UP,
    Kitronik_Game_Controller.ControllerButtonEvents.DOWN,
    my_function5)

def my_function6():
    radio.send_number(4)
Kitronik_Game_Controller.on_button_press(Kitronik_Game_Controller.ControllerButtonPins.UP,
    Kitronik_Game_Controller.ControllerButtonEvents.UP,
    my_function6)

def my_function7():
    radio.send_number(9)
Kitronik_Game_Controller.on_button_press(Kitronik_Game_Controller.ControllerButtonPins.RIGHT,
    Kitronik_Game_Controller.ControllerButtonEvents.DOWN,
    my_function7)

def my_function8():
    radio.send_number(7)
Kitronik_Game_Controller.on_button_press(Kitronik_Game_Controller.ControllerButtonPins.LEFT,
    Kitronik_Game_Controller.ControllerButtonEvents.DOWN,
    my_function8)

def on_forever():
    radio.set_group(1)
    if Kitronik_Game_Controller.button_is_pressed(Kitronik_Game_Controller.ControllerButtonPins.FIRE1):
        radio.send_number(1)
    if Kitronik_Game_Controller.button_is_pressed(Kitronik_Game_Controller.ControllerButtonPins.FIRE2):
        radio.send_number(2)
basic.forever(on_forever)
