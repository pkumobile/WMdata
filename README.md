# WMdata

## Introduction
WeChat is the most popular messaging application in China and WM serves as its mobile social network, which has attracted 963 million monthly active users, covering almost all ages of people.

**WeChat Moments application**
 
A WM application is a set of webpages, the link to which can be posted/shared on users' walls. The WM applications are typically developed using HTML5 (H5) templates, and users can slide up or down to browse each page.  Meanwhile, the link of a WM application can be sent by users to their friends or reposted on their own walls by clicking the share button.

**Data collection**

The data is collected through the APIs provided by Rabbit-Pre, Fibonacci Data Consulting Services Inc., which focuses on analyzing the spreading data of mobile H5 applications in order to assist enterprise marketing.

## Data format
The data we select contains 2866 applications created by businesses or individual users. Regarding these applications, there are 30241752 application views contributed by 2286662 users.

**Each application view record is represented as follows:**

+ The id of the WM application
+ The unique ID of the publisher, the user who posts/reposts the application link
+ The unique ID of the viewer
+ The province where the viewer locates
+ The date when the viewer viewed the application, which is the number of days from 2016-01-01
+ The time when the viewer viewed the application, which is the number of seconds from 00 : 00 that day
+ The duration when the viewer viewed the application
+ The total pages the viewer viewed
+ The total number of pages in the application

**The code for reading the data is shown in read_data.py**