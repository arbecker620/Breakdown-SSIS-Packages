# Breakdown SSIS Packages


## Business Problem
Enterprises and Companies have built their data infrastrutruce and processing around Microsoft's SSIS. Data Engineers and BI Developers have moved onto other technologies to support data efforts and has left legacy data flows as an ongoing tech debt. 


## Solution
The following CLI app breakdowns the XML file for  SSIS  into sections inside the documentation. From this point the end user can decided how they intend to move their data flow into another tool. 
From the CLI, a use must provide a directory where files are located to be processed. Th eoutput of this file creates a readme file where metadata about the package can be analyzed. 
This is not an end all solutions for engineers in gathering the info and should not be treated as such. Its merely a starting point for trying to beging an implmentation on moving data infrascture from SSIS into something else. 


## How to Run
The app utilized the python package typer as apart of the CLI. The 

```console
root@b16946c7e7ab:/app# python3 app.py main '/app/'

```
The following commands outputs a markdown file named "SSIS Packages Reviewed".

## Components

### Paths
The Path section details the flow of data taskes for each relate to that flow. 

### SQL Statement
This task includes SQL code which is used to grab perform SQL statements


### Input Columns 
This section details areas which have an inflow of data columns 

### Output Columns
This section details areas where the ending columns are used

## Baseline Files 
The following example packages were used for creating this project. 

- LoadXMLData.dtsx
- DataTransfer.dtsx

I have tried to find more examples of SSIS files but am limited into what I can see and use to build this out. 
  
