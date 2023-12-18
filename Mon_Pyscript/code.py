from pyscript import document


def translate(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")