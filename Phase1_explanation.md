# OCR Pipeline (Phase 1)

Here we will explain everything line by line in a systematic manner.

#Start with Pipeline.py

It imports a bunch of stuff, lets take a look.

1. dataclass : it is basically a class only , they automatically generate boiler plate for functions like __inti__, __repr__ .....
2. Path: Path represents a filesystem path , also offers
methods to do system calls on path objects. 
3. Optional, Dict, List: Dict and List we know
Optional :- Optional[X] is equivalent to Union[X, None]. We can specify a type or multiple type or no type at all.
4. hashlib: we use to make a 256 bit hash value for our files names.

Then we start by importing our files, the files will we explained in the process.


Then we initialise a data class named page.
## Page
it has 
1. page number
2. image path: the path where its image is stored, it is of the form
    data-> temp -> doc_name_hash->pages.
3. preprocessed path: the path where the pre-processed images are stored.
4. Layout: 
5. ocr_blocks:
6. text : extracted text will be stored here and can be referenced.
7. text_layer : 
8. Confidence :
9. failed : 
10. error : 

Now we make a class named document
##  Document
it has 
1. id : the hashed id
2. input_path : the path of the doc, generally in raw
3. work_dir : the temporary directory to store the info about the docs
4. self.pages: it is a dictionary, 
5. meta : 
6. status : 

Now the actual work start, this is the main OCRPipeline.

### __init__
1. use_layout:
2. use_postprocess:
3. has_gpu:

### run 
This function turn the raw doc into an object of document class.

1. path : the path of the raw doc
2. _setup_document : this is a function which return the doc as an object of document class with attributes path, work_dir(the temp one) and the doc id.
3. _extract_pages : we pass the doc and it extract pages and store it inside the temp directory.
4. _preprocess :
5. _find_layout :
6. _ocr :
7. _rebuild_text :
8. _cleanup :

### check GPU
This function return true or false to the __inti__ section of the main pipeline,based on if gpu is available

### _doc_hash
Converts the doc in an 256 bit id and return the last 16 bit.

## Stages 
### _setup_document