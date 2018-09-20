### Forked from https://www.kaggle.com/soaxelbrooke/first-inbound-and-response-tweets
import pandas as pd 
import numpy as np
import re

# Extract the zip file
import zipfile
zip_ref = zipfile.ZipFile('customer-support-on-twitter.zip', 'r')
zip_ref.extractall('./customer_support_dataset')
zip_ref = zipfile.ZipFile('./customer_support_dataset/twcs.zip', 'r')
zip_ref.extractall('./customer_support_dataset')
zip_ref.close()

# Read dataset
tweets = pd.read_csv('./customer_support_dataset/twcs.csv')

# Pick only inbound tweets that aren't in reply to anything...
first_inbound = tweets[pd.isnull(tweets.in_response_to_tweet_id) & tweets.inbound]
print('Found {} first inbound messages.'.format(len(first_inbound)))

# Merge in all tweets in response
inbounds_and_outbounds = pd.merge(first_inbound, tweets, left_on='tweet_id', 
                                  right_on='in_response_to_tweet_id')
print("Found {} responses.".format(len(inbounds_and_outbounds)))

# Filter out cases where reply tweet isn't from company
inbounds_and_outbounds = inbounds_and_outbounds[inbounds_and_outbounds.inbound_y ^ True]

print("Found {} responses from companies.".format(len(inbounds_and_outbounds)))
print("Tweets Preview:")
print(inbounds_and_outbounds)

# Clean the dataset (remove user names and urls) and extract question (x) and answer (y) texts.
def sn_replace(match):
    _sn = match.group(2).lower()
    if not _sn.isnumeric():
        # This is a company screen name
        return match.group(1) + match.group(2)
    return ''


sn_re = re.compile('(\W@|^@)([a-zA-Z0-9_]+)')
print("Replacing anonymized screen names in X...")
x_text = inbounds_and_outbounds.text_x.apply(lambda txt: sn_re.sub(sn_replace, txt)).apply(lambda txt: re.sub(r'http\S+', '__url__', txt)).apply(lambda txt: txt.replace('\n', '')).apply(lambda txt: " ".join(txt.split()))
print("Replacing anonymized screen names in Y...")
y_text = inbounds_and_outbounds.text_y.apply(lambda txt: sn_re.sub(sn_replace, txt)).apply(lambda txt: re.sub(r'http\S+', '__url__', txt)).apply(lambda txt: txt.replace('\n', '')).apply(lambda txt: " ".join(txt.split()))

# Split the dataset into training, validation and testing (60/20/20)
x_text_train, x_text_validate, x_text_test = np.split(x_text.sample(frac=1), [int(.6*len(x_text)), int(.8*len(x_text))])
y_text_train, y_text_validate, y_text_test = np.split(y_text.sample(frac=1), [int(.6*len(y_text)), int(.8*len(y_text))])

# Save the data
with open('./customer_support_dataset/x_text_train.txt', 'w') as oufi:
	for line in x_text_train:
		oufi.write(line+"\n")

with open('./customer_support_dataset/y_text_train.txt', 'w') as oufi:
	for line in y_text_train:
		oufi.write(line+"\n")	
		
with open('./customer_support_dataset/x_text_validate.txt', 'w') as oufi:
	for line in x_text_validate:
		oufi.write(line+"\n")	

with open('./customer_support_dataset/y_text_validate.txt', 'w') as oufi:
	for line in y_text_validate:
		oufi.write(line+"\n")	

with open('./customer_support_dataset/x_text_test.txt', 'w') as oufi:
	for line in x_text_test:
		oufi.write(line+"\n")
		
with open('./customer_support_dataset/y_text_test.txt', 'w') as oufi:
	for line in y_text_test:
		oufi.write(line+"\n")
