from PIL import Image, ImageDraw
from PIL import ImageFont
import imageio
import math

def draw_hot_chocolate_frame(draw, frame_number, width, height):
    # cup
    cup_bottom = height - 50
    cup_top = cup_bottom - 500
    cup_width = 500
    draw.polygon([(width // 2 - cup_width // 2, cup_top), (width // 2 + cup_width // 2, cup_top),
                  (width // 2 + cup_width // 4, cup_bottom), (width // 2 - cup_width // 4, cup_bottom)],
                  fill=(0, 0, 128))  # orange (210, 105, 30))

    # steam 
    steam_length = 100
    swirl_intensity = 40
    swirl_frequency = 0.05

    steam_x = width // 2
    steam_y = cup_top - frame_number % (cup_top + steam_length)

#Dec 13 is National Hot Chocolate Day
    text = "Happy National \nHot Chocolate Day!"
    font_size = 75
    font_path = "C:\Windows\Fonts\BRADHITC.ttf"
    font = ImageFont.truetype(font_path, font_size)

    text_position = ((width - len(text) * 25) // 2, 10)
    draw.text(text_position, text, font=font, fill=(255, 255, 255))

    # Draw steam a little at a time
    line_thickness = 5
    for i in range(min(frame_number, steam_length)):
        angle = i * swirl_frequency
        offset = int(swirl_intensity * math.sin(angle))
        start_point = (steam_x + offset, steam_y - i)
        end_point = (steam_x + offset, steam_y - i - line_thickness)
        draw.line([start_point, end_point], fill=(255, 255, 255), width=line_thickness)

def create_hot_chocolate_gif(output_path, width, height, num_frames):
    images = []

    for frame_number in range(num_frames):
        # black background
        image = Image.new("RGB", (width, height), color=(0, 0, 0))
        draw = ImageDraw.Draw(image)

        draw_hot_chocolate_frame(draw, frame_number, width, height)

        images.append(image)

    imageio.mimsave(output_path, images, duration=0.1, palettesize=256, optimize=True, compress='LZW')

if __name__ == "__main__":
    gif_output_path = "hot_chocolate.gif"
    image_width = 900
    image_height = 1200
    num_frames = 150

    create_hot_chocolate_gif(gif_output_path, image_width, image_height, num_frames)
    print(f"GIF saved at: {gif_output_path}")
