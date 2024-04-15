
# gradio_variableslider
This Gradio component is dedicated to show only float values for a slider completely excluding whole numbers and integers.

For example, a step value of 0.2 will iterate as:
`0.2 0.4 0.6 0.8 1.2 1.4 1.6 1.8 2.2 2.4 2.6 2.8 3.2 3.4`
...skipping over integers 1 and 3.

<br>
A step of 0.05 would iterate as:

`1.90 1.95 2.05 2.1`
...skipping over integer 2.


## Example usage

```python

import gradio as gr
from gradio_variableslider import VariableSlider

example = VariableSlider().example_value()

with gr.Blocks() as demo:
    sub_slider = gr.Slider(label="Sub-Divisions", minimum=5, maximum=1000, step=5, value=1000, info="This is the amount of values that will occur between each integer.", interactive=True)
    def slider_function(slider_val):
        step = round(1/slider_val, 3)
        slider_final = VariableSlider(minimum=0, maximum=3, value=0, step=step, interactive=True)
        return slider_final
    float_values = VariableSlider(label="Alpha", minimum=0, maximum=2.99, step=0.01, interactive=True)
    sub_slider.release(fn=slider_function, inputs=sub_slider, outputs=alpha_slider)


if __name__ == "__main__":
    demo.queue().launch()

```
The example code above will allow users to iterate through a slider called `sub_slider`, labeled as `Sub-Divisions` which controls the amount of values between each integer. Changing this value will return another slider, `float_slider` which will be the `VariableSlider` custom component. Sliding the slider knob will skip over each integer set by the `minimum` and `maximum` parameters. Here, the returned slider will have the parameters, `minimum=0` and `maximum=3`. Therefore, the `VariableSlider` custom component will skip over integers 0, 1, 2, and 3.

## Changes made to the original `gradio.Slider()` component
- The `randomize` parameter was removed as it was not needed for the intended functionality. This is reflected in `variableslider.py`
- The HTML arrow buttons or "spinners" have been disabled. Additionally, the number form has been set to `readonly` to prevent users from manually typing out-of-range values or integers into the HTML input component. The user should only be able to use the slider knob to set the slider value. These changes are reflected in `Index.svelte`.