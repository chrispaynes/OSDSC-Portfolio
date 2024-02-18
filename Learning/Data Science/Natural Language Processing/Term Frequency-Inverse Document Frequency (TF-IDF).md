TF-IDF, which stands for Term Frequency-Inverse Document Frequency, is a ==numerical statistic used in natural language processing and information retrieval to evaluate the importance of a word in a document relative to a collection of documents (corpus). It is commonly employed for text mining, document classification, and information retrieval tasks. TF-IDF combines two components: Term Frequency (TF) and Inverse Document Frequency (IDF).==

1. **Term Frequency (TF):**
   - ==TF measures the frequency of a term (word) within a specific document.==
   - ==It is calculated as the ratio of the number of times a term occurs in a document to the total number of terms in that document.==
   - High TF values indicate that a term is frequently used within a document.

   $TF(t, d) = \frac{\text{Number of times term } t \text{ appears in document } d}{\text{Total number of terms in document } d}$

2. **Inverse Document Frequency (IDF):**
   - ==IDF measures the importance of a term across the entire document collection (corpus).==
   - ==It is calculated as the logarithm of the ratio of the total number of documents to the number of documents containing the term.==
   - ==Terms that are rare across the entire corpus receive higher IDF values.==

   $IDF(t, D) = \log\left(\frac{\text{Total number of documents in corpus } D}{\text{Number of documents containing term } t}\right)$

3. **TF-IDF Score:**
   - ==The TF-IDF score for a term in a document is obtained by multiplying its TF and IDF values.==

   $TF\text{-}IDF(t, d, D) = TF(t, d) \times IDF(t, D)$

   - ==The resulting score reflects the significance of the term within the specific document and the overall collection of documents.==

==In practice, TF-IDF is used to identify words that are both frequently used within a document (high TF) and relatively rare across the entire corpus (high IDF). Such terms are considered important for distinguishing and characterizing the content of a document within a larger context.==