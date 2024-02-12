![[Pasted image 20230816211014.png]]
![[Pasted image 20230816211142.png]]
![[Pasted image 20230816211222.png]]
![[Pasted image 20230816211245.png]]
![[Pasted image 20230816211257.png]]
![[Pasted image 20230816211318.png]]
![[Pasted image 20230816211405.png]]
![[Pasted image 20230816211633.png]]
![[Pasted image 20230816211739.png]]
![[Pasted image 20230816211812.png]]
![[Pasted image 20230816211904.png]]
![[Pasted image 20230816211935.png]]
![[Pasted image 20230816212148.png]]
![[Pasted image 20230816212223.png]]
![[Pasted image 20230816212250.png]]
![[Pasted image 20230816212312.png]]
![[Pasted image 20230816212342.png]]
![[Pasted image 20230816212402.png]]
![[Pasted image 20230816212645.png]]
![[Pasted image 20230816212803.png]]
![[Pasted image 20230816212837.png]]
![[Pasted image 20230816212927.png]]
# https://en.wikipedia.org/wiki/Cosine_similarity
The resulting similarity ranges from -1 meaning exactly opposite, to 1 meaning exactly the same, with 0 indicating [orthogonality](https://en.wikipedia.org/wiki/Orthogonality "Orthogonality") or [decorrelation](https://en.wikipedia.org/wiki/Decorrelation "Decorrelation"), while in-between values indicate intermediate similarity or dissimilarity.

For [text matching](https://en.wikipedia.org/wiki/Approximate_string_matching "Approximate string matching"), the attribute vectors _A_ and _B_ are usually the [term frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf "Tf–idf") vectors of the documents. Cosine similarity can be seen as a method of [normalizing](https://en.wikipedia.org/wiki/Normalization_(statistics) "Normalization (statistics)") document length during comparison. In the case of [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval "Information retrieval"), the cosine similarity of two documents will range from 0→1![{\displaystyle 0\to 1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/385148d2752cc8c677f4c0b31f4ff0f5cad05303), since the term frequencies cannot be negative. This remains true when using [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf "Tf–idf") weights. The angle between two term frequency vectors cannot be greater than 90°.

---

Cosine similarity is a metric used to measure the similarity between two vectors in a vector space. It is widely used in natural language processing, information retrieval, and machine learning to quantify the similarity of documents, text, or any data represented as vectors.

The cosine similarity between two vectors, $A$ and $B$, is calculated using the cosine of the angle θθ between the vectors. The formula for cosine similarity is as follows:
$$
Cosine Similarity(A,B)=∥A∥⋅∥B∥A⋅B​
$$
where:

- $A⋅B$ is the dot product of vectors AA and BB.
- $∥A∥$ and $∥B∥$ are the magnitudes (Euclidean norms) of vectors $A$ and $B$, respectively.

The cosine similarity ranges from -1 to 1, with 1 indicating perfect similarity, 0 indicating no similarity, and -1 indicating perfect dissimilarity. The angle between vectors is crucial in this calculation; smaller angles result in higher cosine similarity.

Key points about cosine similarity:

1. **Directional Measure**: Cosine similarity is a directional measure, meaning it considers the orientation of vectors but not their magnitude.
    
2. **Scale Invariant**: Cosine similarity is scale-invariant, meaning it is not affected by the magnitude of the vectors. It only depends on the direction.
    
3. **Use Cases**: Cosine similarity is commonly used in information retrieval, document clustering, recommendation systems, and natural language processing. In text analysis, it is frequently employed to measure the similarity between documents represented as vectors of term frequencies (TF-IDF) or word embeddings.
    
4. **Normalization**: It's common to normalize vectors before calculating cosine similarity to ensure that the similarity is not affected by the length of the vectors.
    
5. **Efficiency**: Calculating cosine similarity can be computationally efficient, especially when dealing with high-dimensional sparse vectors, as often encountered in text data.
    

To calculate cosine similarity in practice, you can use various programming libraries, and it is a built-in metric in many machine learning frameworks. The cosine similarity is a valuable tool for comparing the similarity between vectors in a way that is robust to differences in vector magnitudes.