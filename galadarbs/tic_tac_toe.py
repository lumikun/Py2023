import pyray as pr


pr.init_window(800, 450, "Hello, Pyray")
pr.set_target_fps(60)

while not pr.window_should_close():
    pr.clear_background(pr.RAYWHITE)
    pr.draw_text("Hello, World!", 190, 200, 20, pr.VIOLET)
    pr.end_drawing()
pr.close_window()
