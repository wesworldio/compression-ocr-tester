# Compression OCR Tester
**By**: Wes @ https://wesworld.io

**Version**: 0.1.0

**Description:**
Test if OCR can read any text in compressed image

## How to use:
- Clone this repo
- `make setup` (installs poetry + brew packages + pip packages in a python venv)
- `make run` (runs 1 fail + 1 success test case)


## Test Result:
```
################################################################################################
[TEST 1 - START] 2023-01-28 01:17:23.061945
[TEST 1 - INFO] Downloading :  https://pbs.twimg.com/media/FniFkELWIAATWoI?format=jpg&name=large
[TEST 1 - INFO] Image sucessfully Downloaded :  test.jpg
[TEST 1 - INFO] Running OCR on :  test.jpg
[TEST 1 - INFO] recognized.txt updated with full OCR text found

[TEST 1 - INFO] Text Recognized : 


[TEST 1 - FAIL]

No Text Found. Did you compress too small and not think to see if the text is readable thus making an eng sad enough to make this quick test? I get cost to run on all images, but there are ways around that.

[TEST 1 - END] 2023-01-28 01:17:23.402317


################################################################################################
[TEST 2 - START] 2023-01-28 01:17:23.402712
[TEST 2 - INFO] Downloading :  https://wesworld.io/assets/social/shapr3d-love-evidence.png
[TEST 2 - INFO] Image sucessfully Downloaded :  test.jpg
[TEST 2 - INFO] Running OCR on :  test.jpg
[TEST 2 - INFO] recognized.txt updated with full OCR text found

[TEST 2 - INFO] Text Recognized : 
( > Wes Lorenzini

[TEST 2 - PASS] Text Found
[TEST 2 - END] 2023-01-28 01:17:30.288091


################################################################################################
[TEST RESULTS]

Passed: 1 / 2
Failed: 1 / 2
```
**Test results above in**: `README_test_results.txt`