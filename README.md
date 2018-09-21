# WMdata

## Introduction
WeChat is the most popular messaging application in China and WM serves as its mobile social network, which has attracted 963 million monthly active users, covering almost all ages of people. 

In WeChat, the connection between users are bi-directional, and users only have access to the WM of their friends. It indicates that we can infer the friendships among the acquaintances community from the information diffusion.


This dataset is a collection of the server log on users' actions, which reveals the friendships, information diffusion, sharing or browsing web pages and the interests of the users. The sensitive information is removed or anonymized.

**WeChat Moments application**
 
A WM application is a set of webpages, the link to which can be posted/shared on users' walls. The WM applications are typically developed using HTML5 (H5) templates, and users can slide up or down to browse each page.  Meanwhile, the link of a WM application can be sent by users to their friends or reposted on their own walls by clicking the share button.

**Data collection**

The data is collected through the APIs provided by Rabbit-Pre, Fibonacci Data Consulting Services Inc., which focuses on analyzing the spreading data of mobile H5 applications in order to assist enterprise marketing. The dataset records 5792 WM users' actions from Aug. 1st, 2017 to Aug. 30th, 2017, involving 4137 web papges. The dataset is split by ten-days length. For the first ten days, 18217 friendships are exposed. For the second ten days, 18714 friendships are exposed.
For the last ten days, 15383 friendships are exposed.
Overall, 40097 friendships are exposed.

## Data format
The data we select contains thousands of applications created by businesses or individual users. Regarding these applications, there are a large number of application views contributed by WeChat users.

**Each application view record is represented as follows:**

+ (**WEBID**) The id of the WM application
	+ From 0 to 4136
	+ If the TYPE field indicates "userinfo", then this field makes no sense whatever it is.
+ (**PUBLERID**) The unique ID of the publisher, the user who posts/reposts the application link
	+ From 0 to 5792
	+ If this field indicates a zero, it means that the viewer browsed this web pages from the OfficialAccount, rather than one of his/her friend.
	+ If the TYPE field indicates "share", then this field makes no sense whatever it is.
+ (**VIEWERID**) The unique ID of the viewer
	+ From 1 to 5792
+ (**TYPE**) The type of actions of this record
	+ If this field indicates "_view_", then this record describes that the user with VIEWERID browsed a web page posted/reposted by the user with PUBLERID.
	+ If this field indicates "_switchpage_", then this record describes that the user with VIEWERID browsed a web page posted/reposted by the user with PUBLERID and and switched the H5 pages.
	+ If this field indicates "_unload_", then this record describes that the user with VIEWERID tried to browse a web page posted/reposted by the user with PUBLERID but the web page failed to load.
	+ If this field indicates "_exit_", then this record describes that the user with VIEWERID closed a web page posted/reposted by the user with PUBLERID.
	+ If this field indicates "_userinfo_", then this record describes the information of the user with VIEWERID.
	+ If this field indicates "_share_", then this record describes that the user with VIEWERID reposted the web page to his/her WM.
+ (**TIME**) The timestamp when this action happened
+ (**JSON**) The supplementary information to this record in JSON format
	+ If the TYPE field indicates "_view_":
		+ "_shareType_": the channel through which this view action happened, including "singlemessage", "groupmessage", "timeline", "gzh" (official account), "" (unknown), "qq".
		+ "_screen_": the size of the screen of the device.
		+ "_url_": the url of the web page.
		+ "_netType_": the type of network through which this view action happened.
		+ "_useragent_": the system of the device.
		+ "_model_": the manufacturer of the device.
	+ If the TYPE field indicates "_switchpage_":
		+ "_staytm_": how long the user spent on the web page in milliseconds.
		+ "_ttp_": the amount of pages of the web page
		+ "_ctp_": the current page which the user stayed at.
	+ If the TYPE field indicates "_unload_":
		+ "_staym_": the duration until the user gave up loading the pages in milliseconds.
	+ If the TYPE field indicates "_exit_":
		+ "_currentPage_": the page number when the user closed the web page.
	+ If the TYPE field indicates "_userinfo_":
		+ "_province_", "_city_", "_country_": the location in which the user claims he/she lives.
		+ "_sex_": 1 for male, 2 for female, 0 for secret
	+ If the TYPE field indicates "_share_":
		+ "_shareType_": the channel to which the user shared the web page, including "friend" (could be either single message or group message), "timeline", "qq", "qzone".
		+ "_useragent_": the system of the device.
		+ "_staytm_": the duration until the user shared the web page in milliseconds.

Note that some records might be missing due to the package loss.

There is also a file named "WebURL.txt" recording the URLs of the web pages involved in the dataset (might be unavailable now).

## Citing WMData

If you find the data useful in your research, please consider citing:

    @article{zhang2018mobile,
	  title={Mobile Social Big Data: WeChat Moments Dataset, Network Applications, and Opportunities},
	  author={Zhang, Yuanxing and Li, Zhuqi and Gao, Chengliang and Bian, Kaigui and Song, Lingyang and Dong, Shaoling and Li, Xiaoming},
	  journal={IEEE Network},
	  volume={32},
	  number={3},
	  pages={146--153},
	  year={2018},
	  publisher={IEEE}
	}
