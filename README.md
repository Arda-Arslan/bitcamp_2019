# FINRA Insights

A solution leveraging FINRA's big data

<p align="center">
  <img src="https://github.com/arda-arslan/bitcamp2019/blob/master/assets/bitcamp_img.png" width="75%" />
</p>

## Problem
The Financial Industry Regulatory Authority has a lot of data on its hands but isn't sure how to make sense of it to protect the public.

## Inspiration

There are bad actors in business everywhere, but it can be difficult to make sense of data to pinpoint them. FINRA's mission statement is to “Provide investor protection and promote market integrity” and within the constraints of this hackathon, we thought that the best way to help FINRA accomplish it's mission is to leverage their data to generate insights on who the bad actors in their business (e.g. harmful advisors and their respective companies) are so that they can be tracked and monitored to protect the public.

## What we built

1. A network graph tool that shows associations of people via firm, color-coded by a modifiable reputation score
2. A dashboard that visually shows the characteristics of advisors and location
3. A visualization of disclosure files grouped by topical similarity

## Why we built these

1. The culture of firms are created by their employees. By visualizing harmful advisors and the companies/people they have worked with, FINRA analysts can get a sense of which advisors they may have to pay especially close attention to, given that they have a history of working with other nefarious brokers and brokerages.
2. There was a lot of value in the data provided by FINRA, but not a lot of the value could be extracted by us without knowledge of the industry. By creating a dashboard that accepts the dataset, we could let FINRA analysts decide which attributes are important instead of imposing what we think is important.
3. Although the given dataset was extensive, it wasn't expansive. We wanted to dig deeper into why brokers and brokerages had complaints filed against them, so we downloaded the complaint documents and grouped them by topical similarity so that FINRA analysts can have a quick overview of the type and severity of complaints against brokers.

## Why we built these and not something else

A common theme at this hackathon was to:
1. Take FINRA's data
2. Plug it into a machine learning model

Machine learning models can work great in certain situations, but we didn't think this was one of them because the data we were provided in this hackathon wasn't always clear or meaningful. For example, one column of data represented whether a broker has had a customer complaint made against them, expressed by a 'Y' or 'N'. The data provided makes no indication about the severity of the complaint - one broker could have had a complaint because they embezzeled money from clients and another broker could have had a complaint because it was too chilly in their office (not really but you get the idea).

We built a series of tools that would be actively operated by FINRA analysts such that we wouldn't have a black box on our hands.

## How we built it

We used python for data cleaning, webscraping complaint forms, and building our graph visualizations. `pandas` was especially helpful for working with the data.

## Challenges we ran into

- The data is messy and XML is hard to parse
 - We had to create custom solutions to transform the data into a workable csv
- Conclusions are hard to draw
 - e.g. hasCustComp = ‘Y’ – Why?
 - Parsed Individual BrokerCheck PDFs of Advisors to gather more detail
- Data gets big very fast
 - Created proof-of-concept with first 1,000 advisors

## What's next for FINRA Insights

- Track year-over-year changes with Form ADV Data
- Create database from XML
- Visualize clusters by company
- Run simulation with all data
