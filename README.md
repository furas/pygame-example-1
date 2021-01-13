# pygame-example-1

Example for answer on Stackoverflow: [how do i scroll the elements with the background in this situation?](https://stackoverflow.com/questions/65652632/how-do-i-scroll-the-elements-with-the-background-in-this-situation)

## Code

Original code from question in `main-original.py` (it not run). 

Code after modifications in `main-mod.py` (it works).

## Images

Images created as `SVG` in free [Inkscape](https://inkscape.org/) and exported to `PNG`. 

You can find all `SVG` file in `images/svg - inkscape`.

## Video

![1](https://github.com/furas/pygame-example-1/blob/main/output.gif)

Video recorded with free [OBS Studio](https://obsproject.com/). 

Croped and converted to `animated GIF` with free [ffmpeg](https://ffmpeg.org/),

```bash
ffmpeg -i input.mkv -ss 00:00:04 -to 00:00:15.5 -vf scale=562:300 output.gif
```    
