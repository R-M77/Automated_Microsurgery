# Automated_Microsurgery
Supplementary materials for Automation of Real-Time Three-Dimensional Image-Based Visual Servo Control for Single Cell Surgery

Watch the tool align with its target in a six-second microscope recording, then see how the tracker and feedback controller work together. [Read the illustrated research note](https://r-m77.github.io/R-M77/notes/microscope-feedback/).

Armin Eshaghi and James K. Mills, *Automation of single cell surgery in real-time using a vision-based control system*, 2021. [Read the journal article](https://www.inderscience.com/info/inarticle.php?artid=118413).

## Try template matching

The [Python example](examples/track_target.py) generates two small grayscale frames, locates the same target in each and reports its displacement in pixels. This standalone example illustrates the image-tracking step. The published experiments and controller are documented in the paper above.

```sh
python -m pip install numpy opencv-python-headless
python examples/track_target.py
```

The expected displacement is eight pixels right and three pixels up. The [MIT license](examples/LICENSE) applies to the example code. The accompanying research media retain their existing rights.
