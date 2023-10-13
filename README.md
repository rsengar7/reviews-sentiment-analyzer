# Introduction 
Sentiment analysis is a natural language processing (NLP) technique that is used to identify and extract opinions and emotions from text. It is a powerful tool that can be used for a variety of purposes, such as understanding customer sentiment, tracking social media trends, and analyzing product reviews. 
The sentiment analysis code that is provided in the prompt is a well-written and comprehensive implementation of this technique. It uses a variety of NLP techniques, such as tokenization, stemming, stop word removal, part-of-speech tagging, and negation detection, to pre-process the text data. It then uses a Random Forest classifier to predict the sentiment of the text (positive, negative, or neutral). 
 
# About Data 
This dataset contains about 7906 records with binary independent variables taking values ‘pos’ and ‘neg’. Below figure demonstrates the distribution of positive vs negative. 

![Distribution of Ratings](https://github.com/rsengar7/reviews-sentiment-analyzer/blob/main/Images/bar-chart.png)

![Word Cloud](https://github.com/rsengar7/reviews-sentiment-analyzer/blob/main/Images/word-cloud.png)

# Evaluation 
We evaluated the sentiment analysis code by using it to predict the sentiment of a set of product reviews. The code performed well, with an accuracy of over 75% of the test data. This suggests that the code can reliably identify the sentiment of text data. 

![Confusion Matrix](https://github.com/rsengar7/reviews-sentiment-analyzer/blob/main/Images/confusion-matrix.png)

From the confusion matrix, 717 records were classified as True negative which means negative sentiment and 1222 as positive sentiments. 

# Category Tagging 
Category tagging in sentiment analysis is the process of assigning one or more categories to a piece of text based on its sentiment. This can be done manually or automatically. Automatic category tagging uses machine learning to assign categories to text based on its features, such as its words, phrases, and sentiment score. This can be a faster and more efficient way to tag text, but it is important to note that the results may not be as accurate as manual tagging. Category tagging is used to make sentiment analysis more informative. 

This text can be tagged with the following categories: 
1. Product: This category represents the product that is being discussed in the text, which is in this case "product". 
2. Communication: This category represents the communication between the customer and the company, which is in this case bad. 
3. Sentiment: This category represents the overall sentiment of the text, which is in this case mixed. 
 
### Here are some additional benefits of using category tagging in sentiment analysis for this example: 
More informative results: Category tagging can make sentiment analysis more informative by providing insights into the reasons for a particular sentiment. For example, in the case of the image you sent, the category tagging would help to identify that the customer is satisfied with the quality of the products, but dissatisfied with the communication from the company. This information could then be used by the company to improve its communication with customers. 
Better insights: Category tagging can help to provide better insights into customer behavior and public opinion. For example, if a company uses category tagging to understand the sentiment of customer feedback, it can identify the specific aspects of its products and services that are most important to customers. This information can be used to improve products and services, as well as to develop better marketing and sales strategies. 
Overall, category tagging is a valuable tool that can be used to improve the accuracy, informativeness, and insights gained from sentiment analysis. 
