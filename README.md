# Breakdown SSIS Packages


## Business Problem
Enterprises and Companies have built their data infrastrutruce and processing around Microsoft's SSIS. Data Engineers and BI Developers have moved onto other technologies to support data efforts and has left legacy data flows as an ongoing tech debt. 


## Solution
The following CLI app seeks to breakdown the XML file SSIS  into sections inside the documentation. From this point the end user can decided how they intend to move their data flow into another tool. 

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
  
