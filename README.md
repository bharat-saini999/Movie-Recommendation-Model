# Movie-Recommendation-Model
This project is a content-based movie recommendation system built using Python and machine learning. It uses the TMDB 5000 dataset to suggest similar movies based on a given input movie title.
This file consist of data of 5000 movies all around the world.
It performs operation on this data and give recommendation similar to the selected movie.


------------------How It Works:-----------------------------------------------------------------------

1.  Data Preprocessing

Merged movies and credits datasets on the title column.

Selected relevant features: movie_id, title, overview, genres, keywords, cast, crew.

Converted JSON-like columns (genres, keywords, cast, crew) into list of strings.

Extracted:

Top 3 cast members

Director from crew

Cleaned and combined all textual features into a single tags column.

2.  Text Vectorization

Applied CountVectorizer from sklearn to convert text into numerical feature vectors.

Limited vocabulary to 5000 most frequent words and removed English stopwords.

3.  Text Normalization

Used PorterStemmer from NLTK to stem words to their root form (e.g., "running" → "run").

4.  Similarity Calculation

Calculated cosine similarity between movies based on their vectorized tags.

5.  Recommendation Function

For a given movie, it finds the top 5 most similar movies using cosine similarity.


--------------------Sample Output:---------------------------------------------------------

For input 'Superman', recommendations include:

Superman II

Superman IV: The Quest for Peace

Central Intelligence

Superman Returns

The League of Extraordinary Gentlemen
