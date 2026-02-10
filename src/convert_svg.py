import cairosvg

def svg_to_png(input_svg, output_png):
    cairosvg.svg2png(
    url=input_svg,
    write_to=output_png,
    output_width=256,
    output_height=256
)