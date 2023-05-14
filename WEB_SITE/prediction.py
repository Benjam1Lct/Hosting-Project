import pipeline, tools

keras_pipeline = pipeline.Pipeline()

def ocr(image_url):
    image = tools.read(image_url)
    predictions = keras_pipeline.recognize([image])
    ocr_text = ""
    for text, box in predictions[0]:
        ocr_text += text + " "
    return ocr_text

print(ocr('./eng.jpg'))