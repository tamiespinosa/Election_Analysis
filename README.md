# Election Analysis

## Table of Contents
- [Overview of Project](#OverviewProject)
  * [Purpose](#purpose)
- [Results](#Results)
  * [Results by County](#countyresults)
  * [Results by Candidate](#candidateresults)
- [Election Audit Summary](#Summary)
- [Resources](#Resources)

 
## <a name="OverviewProject"></a>Overview of Project

An employee for the Colorado Board of Directors is looking to audit and certify a recent congrassional election for the state. We were given a file with the voter ID, County were the vote was casted, and the candidate selected for 369.711 votes. A report with the Election Analysis was generated.   

### <a name="purpose"></a>Purpose

This audit needs to produce:
- The total number of votes
- The counties where the votes are collected from and 
  * Number of votes per county
  * Percentage of votes per county
  * County with the most votes
- The candidates in the election 
  * Number of votes per candidate
  * Percentage of votes per candidate
  * The winner of the election and the winner's vote count and percentage of votes. 
  
## <a name="Results"></a>Results

The results of this election are as follow. To verify the information provided, access the Election Analysis. 

* In this election a total of 369,711 votes were counted.  

* The votes counted came from three counties in Colorado, as seen in the table below. 

**County**|**Total Votes**|**Percentage**|
 --- |---|---|
 Denver    | 306,055       | 82.5%        |
 Jefferson | 38,855        | 10.5%        |
 Arapahoe  | 24,801        | 6.7%         |
 
* Of the counties were the votes were counted,the one with the largest turnout was Denver.  

* The candidates that received votes from those three counties are shown in the table below. 

**Candidate**|**Total Votes**|**Percentage**|
 --- |---|---|
 Diana DeGette            | 272,892       | 73.8%        |
 Charles Spencer Stockham | 85,213        | 23.0%        |
 Raymon Anthony Doanne    | 11,606        | 3.1%         |

* Diana DeGette received 73.8% (272,892) of the votes, making her the winner of the popular vote. 

## <a name="Summary"></a>Election Audit Summary

The code used to evaluate the votes gathered a list of candidates and counties when iterating through each vote. Afterwards the code counted the votes per candidate and county name. In other words, the candidates and counties names were not hard coded, making this code usable for other elections. 

In our data, the county and the candidate were the second and third column in our data respectively. As the computer passes through each row, it is evaluating the second item on the row as the county_name and the third item on the row as the candidate_name, as seen in the code below.  If this code was to be used for a similar election the order of the columns, in a new data set, would have to be inspected. The indexes used to evaluate candidate_name and county_name would have tp be updated accordingly. 

...
 candidate_name = row[2]
 county_name =row[1]
...

Additionally, the file paths for the input and output files would need to be updated. In out case our input is the file_to_load, and the output is the file_to_save. The file names and folders where those are located would need to be updated for a new data set.  

...
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
...

## <a name="Resources"></a>Resources
