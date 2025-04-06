import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

def generate_visualizations(data):
    # Sentiment distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(data["VADER_Polarity"], palette="viridis")
    plt.title("Sentiment Distribution (VADER)")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()

    # WordCloud
    text = " ".join(data["Review"])
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width=800, height=400, background_color="black", stopwords=stopwords).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("WordCloud of Reviews")
    plt.show()