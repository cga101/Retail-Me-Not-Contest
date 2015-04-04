Submission for : http://www.mindsumo.com/contests/analyze-clicks-and-bounce-rates-from-online-couponers

Extra Credit Offered for Accomplishing the Following:

|Condition | Fulfillment|
|----------|------------|
|No 3rd Party Libraries | All Imports From Native Libraries|

I decided to deliver using Python as the code is easy for others to read and I have little issues using the regex library.

When determining Min-Max Click Times, I decided to use a greedy approach in the event of ties (that is, the first one with the appropriate number of clicks get reported). As I am not sure how this CSV would be parsed, I wanted to ensure that each row is consistent with the next (thus attempting to minimize problems). This does, however, present the issue of having a number of rows that report the same min/max time. In my opinion, this seems logically sound- rows that have clicks at one time are both a minimum and a maximum. However, I am not sure how this would have been handled in a production environment and welcome insight on this!

For both programs, I start by using Regex to extract the necessary information from each line of the file. For each line I receive, I then check if the line is an out request, a get request or not relevant for the problem and handle each case. Should it be an out, I map coupons to times & retailers to ips. Should it be a get, I map retailers to ips. Once that is handled, I perform the necessary arithmetic to fulfill both of the problem constraints and write to a CSV.

As I am always looking to improve as a software engineer, I appreciate any and all criticism! Feel free to reach out to me if you have advice on how I can improve.
