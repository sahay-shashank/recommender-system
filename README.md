# Recommender System

A recommender system which extracts features with count vectorizer and find similarities with cosine similarity.

## What is count vectorizer

Count vectorizer extracts words without repeative words (like articles) and makes a matrix with the rows being the word and the column as the sentence. The data stored in the matrix is the number of times the word appears in that sentence. While fitting the data, it creates vectors for each sentence which are used for finding similarities.

## What is cosine similarity

With cosine similarity we find the angles between two vectors which denotes how similar is the two vectors.

## What comes next

With the similarities found between the vectors, we can compare and rank items to return top 5 or top 10 similar items which the user may like or may find useful.
