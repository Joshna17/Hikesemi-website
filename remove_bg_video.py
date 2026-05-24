import cv2
import numpy as np
from PIL import Image
from rembg import remove, new_session
import imageio
import os

INPUT  = r"D:\Gen-4 Turbo - Medium shot of  sleek PCIe 5_0 SSD and DDR5 RAM module suspended  zero gravity against.mp4"
OUTPUT = r"C:\Users\HP\hiksemi\assets\videos\hero-product.webm"

cap = cv2.VideoCapture(INPUT)
fps     = cap.get(cv2.CAP_PROP_FPS)
total   = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width   = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Video: {width}x{height} @ {fps:.2f}fps  |  {total} frames")

session = new_session("u2net")

writer = imageio.get_writer(
    OUTPUT,
    fps=fps,
    codec="vp9",
    pixelformat="yuva420p",
    output_params=["-b:v", "0", "-crf", "30"],
    macro_block_size=None,
)

for i in range(total):
    ret, frame = cap.read()
    if not ret:
        break
    rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil   = Image.fromarray(rgb)
    out   = remove(pil, session=session)          # RGBA PIL image
    rgba  = np.array(out)                          # H x W x 4
    writer.append_data(rgba)
    if (i + 1) % 10 == 0:
        print(f"  {i+1}/{total} frames done")

cap.release()
writer.close()
print(f"\nDone! Saved to: {OUTPUT}")
print(f"File size: {os.path.getsize(OUTPUT)/1024:.1f} KB")
