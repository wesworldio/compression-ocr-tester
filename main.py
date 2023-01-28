# Source for this main.py 
# https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/

# Import required packages
import datetime
import requests
import shutil
import cv2
import pytesseract

###################################################################################################################

# Compression Settings without checking OCR after compression
TEST_IMAGE_URL_FAIL = 'https://pbs.twimg.com/media/FniFkELWIAATWoI?format=jpg&name=large'

# Pass for OCR
TEST_IMAGE_URL_SUCCESS = 'https://wesworld.io/assets/social/shapr3d-love-evidence.png'

# Saving image locally for test to
TEST_IMAGE_SAVE_FILENAME = 'test.jpg'

SASSY_COMPRESSION_FAIL_MESSAGE = "No Text Found. Did you compress too small and not think to see if the text is readable thus making an eng sad enough to make this quick test? I get cost to run on all images, but there are ways around that."

###################################################################################################################
# Vars
test_num = 1
test_num_fail = 0
test_num_pass = 0

###################################################################################################################

def run_test_with_image_url(image_url=None):
    global test_num, test_num_fail, test_num_pass

    print()
    if image_url is None:
        print('Please enter a URL to run the test')
        return

    print("################################################################################################")
    print(f"[TEST {test_num} - START]", datetime.datetime.now())
    print(f"[TEST {test_num} - INFO] Downloading : ",image_url)
    res = requests.get(image_url, stream = True)

    if res.status_code == 200:
        with open(TEST_IMAGE_SAVE_FILENAME,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print(f"[TEST {test_num} - INFO] Image sucessfully Downloaded : ",TEST_IMAGE_SAVE_FILENAME)
    else:
        print(f"[TEST {test_num} - INFO] Image Couldn\'t be retrieved")

    # Mention the installed location of Tesseract-OCR in your system
    # pytesseract.pytesseract.tesseract_cmd = 'System_path_to_tesseract.exe'

    # Read image from which text needs to be extracted
    img = cv2.imread(TEST_IMAGE_SAVE_FILENAME)

    # Preprocessing the image starts

    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = img.copy()

    # A text file is created and flushed
    file = open("recognized.txt", "w+")
    file.write("")
    file.close()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    full_text = ""
    print(f"[TEST {test_num} - INFO] Running OCR on : ",TEST_IMAGE_SAVE_FILENAME)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]

        # Open the file in append mode
        file = open("recognized.txt", "a")

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
        full_text += text

        # Appending the text into file
        file.write(text)
        file.write("\n")

        # Close the file
        file.close
        print(f"[TEST {test_num} - INFO] recognized.txt updated with full OCR text found")
        print()

    print(f"[TEST {test_num} - INFO] Text Recognized : ")
    print(full_text)
    print()
    if full_text != '':
        test_num_pass = test_num_pass + 1
        print(f"[TEST {test_num} - PASS] Text Found")
    else: 
        test_num_fail = test_num_fail + 1
        print(f"[TEST {test_num} - FAIL]")
        print()
        print(SASSY_COMPRESSION_FAIL_MESSAGE)
        print()
    print(f"[TEST {test_num} - END]", datetime.datetime.now())
    print()
    test_num = test_num + 1

###################################################################################################################
# Run Tests

#  Test Twitter Compression with quick OCR Test
run_test_with_image_url(TEST_IMAGE_URL_FAIL)

#  Test Image with quick OCR Test
run_test_with_image_url(TEST_IMAGE_URL_SUCCESS)

###################################################################################################################
# Test Results
test_total = test_num - 1

print()
print("################################################################################################")
print("[TEST RESULTS]")
print()
print(f"Passed: {test_num_pass} / {test_total}")
print(f"Failed: {test_num_fail} / {test_total}")
print()
