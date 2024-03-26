import requests, cv2, time
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq
import numpy as np

model = AutoModelForVision2Seq.from_pretrained("microsoft/kosmos-2-patch14-224")
processor = AutoProcessor.from_pretrained("microsoft/kosmos-2-patch14-224")

cap = cv2.VideoCapture(0)
prompt = "<grounding>An image of"

while True:
    ret, frame = cap.read()
    cv2.imshow('camera' , frame)
    key =cv2.waitKey(10)
    pil = Image.fromarray(frame)
    im = np.array(pil)
    pil_img = Image.fromarray(im)
    pil_img.save('image.jpg')

#   image = Image.open("guitar2.jpg")
    image = Image.open("image.jpg")
    inputs = processor(text=prompt, images=image, return_tensors="pt")
    generated_ids = model.generate(
            pixel_values=inputs["pixel_values"],
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            image_embeds=None,
            image_embeds_position_mask=inputs["image_embeds_position_mask"],
            use_cache=True,
            max_new_tokens=128,
            )
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    processed_text = processor.post_process_generation(generated_text, cleanup_and_extract=False)
    processed_text, entities = processor.post_process_generation(generated_text)
    print(processed_text,entities)
    time.sleep(5)




cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('camera' , frame)
    key =cv2.waitKey(10)
    time.sleep(2)
    pil = Image.fromarray(frame)
    im = np.array(pil)
    pil_img = Image.fromarray(im)
    pil_img.save('image.jpg')

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

