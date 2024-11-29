from animation_classes_test import *

def main():
    def run_animations():
        if animations:
            current_animation = animations.pop(0)
            current_animation.start(run_animations)  # Start current animation

    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # Initialize animations
    animations = [
        AnimationA(canvas),
        AnimationB(canvas),
        WinAnimation(canvas, 10),
        # LoadingScreen(canvas, 10)
    ]

    # Start animation sequence
    run_animations()

    root.mainloop()

if __name__ == "__main__":
    main()
