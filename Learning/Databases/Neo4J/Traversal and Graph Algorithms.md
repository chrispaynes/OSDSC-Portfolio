1. **Simple Node Retrieval:**
   ```cypher
   MATCH (n:Label)
   RETURN n;
   ```

2. **Node and Outgoing Relationship Retrieval:**
   ```cypher
   MATCH (n:Label)-[r:REL_TYPE]->(m)
   RETURN n, r, m;
   ```

3. **Node and Incoming Relationship Retrieval:**
   ```cypher
   MATCH (n:Label)<-[r:REL_TYPE]-(m)
   RETURN n, r, m;
   ```

4. **Node with Specific Property:**
   ```cypher
   MATCH (n:Label {property: value})
   RETURN n;
   ```

5. **Node and Outgoing Relationship with Specific Property:**
   ```cypher
   MATCH (n:Label)-[r:REL_TYPE {property: value}]->(m)
   RETURN n, r, m;
   ```

6. **Node and Incoming Relationship with Specific Property:**
   ```cypher
   MATCH (n:Label)<-[r:REL_TYPE {property: value}]-(m)
   RETURN n, r, m;
   ```

7. **Multiple Hop Traversal:**
   ```cypher
   MATCH (a:Label)-[:REL_TYPE]->(b)-[:REL_TYPE]->(c)
   RETURN a, b, c;
   ```

8. **Variable-Length Relationship Traversal:**
   ```cypher
   MATCH (a:Label)-[:REL_TYPE*1..3]->(b)
   RETURN a, b;
   ```

9. **Union of Results:**
   ```cypher
   MATCH (a:Label)-[:REL_TYPE]->(b)
   RETURN a, b
   UNION
   MATCH (c:Label)-[:ANOTHER_REL]->(d)
   RETURN c, d;
   ```

10. **Conditional Traversal:**
    ```cypher
    MATCH (a:Label)-[:REL_TYPE]->(b)
    WHERE a.property = value
    RETURN a, b;
    ```

---

Here are some more advanced graph traversal patterns and queries in Cypher:

1. **Path Finding with `shortestPath`:**
   Find the shortest path between two nodes.
   ```cypher
   MATCH p = shortestPath((a:Label {property: 'start'})-[*]-(b:Label {property: 'end'}))
   RETURN p;
   ```

2. **Path Finding with `allShortestPaths`:**
   Find all shortest paths between two nodes.
   ```cypher
   MATCH p = allShortestPaths((a:Label {property: 'start'})-[*]-(b:Label {property: 'end'}))
   RETURN p;
   ```

3. **Common Neighbors of Nodes:**
   Find nodes that are common neighbors of two given nodes.
   ```cypher
   MATCH (a)-[:REL_TYPE]->(common)-[:REL_TYPE]->(b)
   WHERE id(a) <> id(b)
   RETURN common;
   ```

4. **Clustering Coefficient:**
   Calculate the clustering coefficient for a node.
   ```cypher
   MATCH (a:Label)-[:REL_TYPE]-(b)-[:REL_TYPE]-(c)
   WHERE id(a) = id(c)
   RETURN count(distinct b) / (count(distinct b) + 2.0) as clusteringCoefficient;
   ```

5. **PageRank Algorithm:**
   Implement the PageRank algorithm to find influential nodes.
   ```cypher
   CALL algo.pageRank.stream('Label', 'REL_TYPE', {iterations: 20, dampingFactor: 0.85})
   YIELD nodeId, score
   RETURN algo.asNode(nodeId).property as node, score
   ORDER BY score DESC
   LIMIT 10;
   ```

6. **Community Detection with Louvain:**
   Use the Louvain algorithm for community detection.
   ```cypher
   CALL algo.louvain('Label', 'REL_TYPE', {writeProperty: 'community'})
   YIELD nodes, communityCount
   RETURN nodes, communityCount;
   ```

7. **Graph Embedding with Node2Vec:**
   Use Node2Vec for graph embedding.
   ```cypher
   CALL gds.alpha.node2vec.write({
     nodeProjection: 'Label',
     relationshipProjection: {
       REL_TYPE: {type: 'REL_TYPE', orientation: 'UNDIRECTED'}
     },
     embeddingDimension: 16,
     iterations: 10,
     walkLength: 80,
     inOutFactor: 1.0,
     returnFactor: 1.0
   })
   YIELD nodeCount, createMillis;
   ```

8. **Graph Similarity with Jaccard Similarity:**
   Calculate Jaccard similarity between nodes based on neighbors.
   ```cypher
   MATCH (a:Label)-[:REL_TYPE]->(n1)
   WITH a, collect(id(n1)) as set1
   MATCH (a)-[:REL_TYPE]->(n2)
   WITH a, set1, collect(id(n2)) as set2
   RETURN a, algo.similarity.jaccard(set1, set2) as jaccardSimilarity
   ORDER BY jaccardSimilarity DESC
   LIMIT 5;
   ```

