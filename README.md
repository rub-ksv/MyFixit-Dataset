# MyFixit Dataset

This repository contains the MyFixit dataset. It also includes the processed data and column corpus required for the [MyFixit Annotator](https://github.com/rub-ksv/MyFixit-Annotator). 

MyFixit is a collection of repair manuals, collected from [iFixit](https://www.ifixit.com) website. There are in total **31,601** repair manuals in 15 device categories. Each step in the manuals of the 'Mac Laptop' category is annotated with the required tool, disassembled parts, and the removal verbs (in total **1,497** manuals with **36,659** steps). The rest of the categories do not have human annotations yet.

For the details of dataset and the annotation guideline, please refer to the [paper](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.260.pdf) published in LREC 2020.

Here is an example of an annotated step in the dataset:

    {"Title": "MacBook Unibody Model A1278 Hard Drive Replacement", 
    "Ancestors": ["MacBook", "Mac Laptop", "Mac", "Root"], 
    "Guidid": 816, 
    "Category": "MacBook Unibody Model A1278", 
    "Subject": "Hard Drive",
    "Toolbox": 
        [{"Name": ["phillips 00 screwdriver"], "Url": "https://www.ifixit.com/Store/Parts/Phillips-00-Screwdriver/IF145-006", "Thumbnail": "https://da2lh5cs8ikqj.cloudfront.net/cart-products/rLfPqcRxAVqNxfwc.mini"},
        {"Name": ["spudger"], "Url": "http://www.ifixit.com/Tools/Spudger/IF145-002", "Thumbnail": "https://da2lh5cs8ikqj.cloudfront.net/cart-products/fIQ3oZSjd1yLgqpX.mini"},
        {"Name": ["t6 torx screwdriver"], "Url": "https://www.ifixit.com/Store/Tools/TR6-Torx-Security-Screwdriver/IF145-225", "Thumbnail": ""}],
    "Url": "https://www.ifixit.com/Guide/MacBook+Unibody+Model+A1278+Hard+Drive+Replacement/816",
    "Steps": [{
        "Order": 1,
        "Tools_annotated": ["NA"],
		"Tools_extracted": ["NA"],
        "Word_level_parts_raw": [{"name": "battery", "span": [19, 19]}],
		"Word_level_parts_clean": ["battery"],
        "Removal_verbs": [{"name": "pull out", "span": [17, 17], "part_index": [0]}], 
        "Lines":
            [{"Text": "be sure the access door release latch is vertical before proceeding."},
            {"Text": "grab the white plastic tab and pull the battery up and out of the unibody."}],
        "Text_raw": "Be sure the access door release latch is vertical before proceeding. Grab the white plastic tab and pull the battery up and out of the Unibody.",
        "Images": ["https://d3nevzfk7ii3be.cloudfront.net/igi/WkwQip2DfR1iJLMX.standard"], 
        "StepId": 4122},
         ...]}

**The data and models are available in the following formats:**

## 1- Complete dataset
There are 15 category of manuals. Here are the statistics of each category:

| Category          | Number of manuals | Number of steps with unique text |
|-------------------|-------------------|----------------------------------|
| Mac               | 2868              | 8893                             |
| Car and Truck     | 761               | 3320                             |
| Household         | 1710              | 7859                             |
| Computer Hardware | 927               | 4502                             |
| Appliance         | 1333              | 5744                             |
| Camera            | 2761              | 12000                            |
| PC                | 6677              | 26181                            |
| Electronics       | 2343              | 9765                             |
| Phone             | 6005              | 20573                            |
| Game Console      | 1008              | 4517                             |
| Skills            | 140               | 885                              |
| Vehicle           | 374               | 1815                             |
| Media Player      | 649               | 2697                             |
| Apparel           | 382               | 2051                             |
| Tablet            | 2756              | 10679                            |

For each category, there is a JSON file that contains all the collected manuals with more than one step and one tool. The teardown manuals are excluded from the data. 

The JSON files are collections of JSON-like objects with one object in each line.

### Finding the relevant manuals:
There is a simple script [search.py](search.py) that helps you to find the proper manuals and save them in XML or JSON format. The script receives the following arguments:

    -device: Name of the device. (Optional)
    -input: Name of one of the files in 'jsons/' directory (Required)
    -part: Part of the device to repair. (Optional)
    -format: The format of output data, XML or JSON. (Optional, default is JSON)
    -output: Name of the output file. (Required)
    -mintools: Minimum number of tools in the manual. (Optional)
    -minsteps: Minimum number of steps in the manual. (Optional)
    -verbose: Prints the titles of selected manuals. (Optional)
    -annotatedtool: Only selecting the manuals with the annotation of required tools (Optional)
    -annotatedpart: Only selecting the manuals with the annotation of disassembled parts (Optional)

Required libraries:
> dicttoxml (only if xml is selected as the output format)    

Example:

    python search.py -input Mac.json -output tmp -device macbook pro -part battery -mintools 2 -minsteps 15 -format xml -verbose -annotatedtool -annotatedpart
    
Output:

    Total number of matched manuals :29  
    Title of manuals:  
    MacBook Pro 17" Models A1151 A1212 A1229 and A1261 Battery Connector Replacement  
    MacBook Pro 17" Models A1151 A1212 A1229 and A1261 PRAM Battery Replacement  
    MacBook Pro 15" Core 2 Duo Model A1211 PRAM Battery Replacement  
    MacBook Pro 15" Core 2 Duo Model A1211 Battery Connector Replacement  
    MacBook Pro 15" Core Duo Model A1150 PRAM Battery Replacement  
    MacBook Pro 15" Core Duo Model A1150 Battery Connector Replacement  
    MacBook Pro 15" Core 2 Duo Models A1226 and A1260 Battery Connector Replacement  
    MacBook Pro 15" Unibody Late 2008 and Early 2009 Battery Connector Replacement  
    MacBook Pro 13" Retina Display Late 2012 Battery Replacement  
    MacBook Pro 13" Retina Display Early 2013 Battery Replacement  
    MacBook Pro 13" Retina Display Late 2013 Battery Replacement  
    MacBook Pro 13" Retina Display Mid 2014 Battery Replacement  
    MacBook Pro 13" Retina Display Early 2015 Battery Replacement  
    MacBook Pro 13" Function Keys Late 2016 Battery Replacement  
    MacBook Pro 15" Retina Display Mid 2012 Battery Replacement  
    MacBook Pro 15" Retina Display Late 2013 Battery Replacement  
    MacBook Pro 15" Retina Display Mid 2015 Battery Replacement  
    MacBook Pro 15" Retina Display Early 2013 Battery Replacement  
    MacBook Pro 15" Retina Display Mid 2014 Battery Replacement  
    MacBook Pro 13" Retina Display Late 2012 Battery Replacement (Legacy)  
    MacBook Pro 13" Retina Display Early 2013 Battery Replacement (Legacy)  
    MacBook Pro 13" Retina Display Late 2013 Battery Replacement (Legacy)  
    MacBook Pro 13" Retina Display Mid 2014 Battery Replacement (Legacy)  
    MacBook Pro 13" Retina Display Early 2015 Battery Replacement (Legacy)  
    MacBook Pro 15" Retina Display Mid 2012 Battery Replacement (Legacy)  
    MacBook Pro 15" Retina Display Late 2013 Battery Replacement (Legacy)  
    MacBook Pro 15" Retina Display Mid 2014 Battery Replacement (Legacy)  
    MacBook Pro 15" Retina Display Early 2013 Battery Replacement (Legacy)  
    MacBook Pro 15" Retina Display Mid 2015 Battery Replacement (Legacy)  
    Selected manuals are saved in tmp.xml

### Running a Mongodb sever and importing data:

To work with the annotator tool, you need to load the database into a running MongoDB server.  

For learning about mongodb installation please refer to its [documentations](https://docs.mongodb.com/manual/installation/).

#### After running the sever you can import the dataset  with following command:

    mongoimport --db myfixit --collection posts --file <fileName>.json

  

## 2- Processed data for the [MyFixit annotator](https://github.com/rub-ksv/MyFixit-Annotator)

The web-based MyFixit annotator produces a table of processed data for the selected device category and fills the annotation pages with it. The tables include the extracted tools, cleaned text, the annotated and unannotated sentences separated in each step, the part and verb candidates extracted either with the unsupervised (basic) model or the supervised (deep) model. The tables also have the list of parts' names that were filtered by Wordnet at each step.

In order to work with the annotator without running the parser/tagger, copy the tables to `/src/web_app/static/tables/`. Otherwise, the tables will be generated automatically from the database. Generating the tables might take some time, depending on the size of the selected category and the chosen model. 

## 3- Column corpus of annotated data

If the table of processed data does not exist for the selected category, and if the supervised method is selected for part extraction, the app trains a bilstm-CRF based model from the annotated data. For doing that, it looks for a column corpus in `/src/part_extraction/data/`, in which the labels are represented in the BIEO form. If the file does not exist, it will be automatically produced from the annotated steps in the database. There is a column corpus for the category Mac laptop.

# Cite
If you found this dataset or our work useful, please cite:

    @InProceedings{nabizadeh-kolossa-heckmann:2020:LREC,
      author    = {Nabizadeh, Nima  and  Kolossa, Dorothea  and  Heckmann, Martin},
      title     = {MyFixit: An Annotated Dataset, Annotation Tool, and Baseline Methods for Information Extraction from Repair Manuals},
      booktitle      = {Proceedings of The 12th Language Resources and Evaluation Conference},
      month          = {May},
      year           = {2020},
      address        = {Marseille, France},
      publisher      = {European Language Resources Association},
      pages     = {2120--2128}}
