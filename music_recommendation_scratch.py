data = {
    'pop': ['Hande Yener', 'Serdar Ortaç', 'Demet Akalın', 'Tarkan'],
    'rock': ["Guns N' Roses", 'Led Zeppelin', 'Måneskin', 'Queen'],
    'rap': ['Sefo', 'Uzi', 'Güneş', 'Lvbel C5'],
    'blues': ['B.B. King', 'Eric Clapton', 'Gary Moore', 'Stevie Ray Vaughan']
}


def cosine_similarity(vec1:list, vec2:list) -> float:
    dot_product = sum([vec1[i] * vec2[i] for i in range(len(vec1))])
    norm1 = sum([x ** 2 for x in vec1]) ** 0.5
    norm2 = sum([x ** 2 for x in vec2]) ** 0.5
    if norm1 == 0 or norm2 == 0:
        return 0
    else:
        return dot_product / (norm1 * norm2)


def recommend_songs(genre:str, artist:str, k:int=3) -> list:
    # Get all artists in the same genre
    artists = data[genre]
    
    # Get the vector representation of the user's preferred artist
    preferred_artist = [0] * len(artists)
    preferred_artist[artists.index(artist)] = 1
    
    # Calculate the similarity between the preferred artist and all other artists
    similarities = []
    for i, a in enumerate(artists):
        if a != artist:
            vector = [0] * len(artists)
            vector[i] = 1
            sim = cosine_similarity(preferred_artist, vector)
            similarities.append((a, sim))
    
    # Sort the artists by similarity and get the top k
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_artists = [a for a, sim in similarities[:k]]
    
    # Get a list of recommended songs from the top artists
    recommendations = []
    for a in top_artists:
        recommendations.append(a)
    
    return recommendations


genre = 'blues'
artist = 'B.B. King'
recommendations = recommend_songs(genre, artist, k=3)
print(f"Recommended songs in the {genre} genre based on your liking of {artist}:")
for i,recommendation in enumerate(recommendations):
    print(f'{i+1}: {recommendation}')

