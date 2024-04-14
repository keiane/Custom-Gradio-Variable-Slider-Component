
import gradio as gr
from gradio_variableslider import VariableSlider

example = VariableSlider().example_value()

with gr.Blocks() as demo:
    sub_slider = gr.Slider(label="Sub-Divisions", minimum=5, maximum=100, step=5, value=100, info="Select the amount of maps you will generate between each integer.", interactive=True)
    def slider_function(slider_val):
        step = round(1/slider_val, 3)
        slider_final = VariableSlider(minimum=0, maximum=3, value=0, step=step, interactive=True)
        return slider_final
    alpha_slider = VariableSlider(label="Alpha", minimum=0, maximum=3.99, step=0.01, interactive=True)
    sub_slider.release(fn=slider_function, inputs=sub_slider, outputs=alpha_slider)


if __name__ == "__main__":
    demo.queue().launch()
