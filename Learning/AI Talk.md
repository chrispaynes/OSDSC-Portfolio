https://milvus.io/
- https://github.com/the-ai-alliance

![[Pasted image 20250213110745.png]]![[Pasted image 20250213110834.png]]
- https://www.perplexity.ai/
- lexical search vs semantic search
![[Pasted image 20250213111020.png]]
![[Pasted image 20250213111052.png]]
![[Pasted image 20250213111205.png]]
![[Pasted image 20250213111303.png]]
![[Pasted image 20250213111315.png]]
![[Pasted image 20250213111330.png]]
![[Pasted image 20250213111425.png]]
![[Pasted image 20250213111442.png]]
![[Pasted image 20250213112635.png]]
![[Pasted image 20250213112711.png]]
![[Pasted image 20250213112800.png]]
![[Pasted image 20250213112932.png]]
![[Pasted image 20250213113044.png]]
![[Pasted image 20250213113131.png]]
	- how do we only send relevant docs

![[Pasted image 20250213113244.png]]
![[Pasted image 20250213113311.png]]
![[Pasted image 20250213113346.png]]
![[Pasted image 20250213113406.png]]
	the vector db milvus will know which docs from the db are relevant and will send those to the LLM to solve the question
		- query milvus, provide context to llm, llm answers
		- milvus helps narrow down how many docs are searched

![[Pasted image 20250213113832.png]]

![[Pasted image 20250213114010.png]]
![[Pasted image 20250213114059.png]]
![[Pasted image 20250213114127.png]]
	- https://github.com/sujee/data-prep-kit-examples/blob/main/events/2025-02-13__AI-alliance-office-hour-RAG-workshop.md
![[Pasted image 20250213114325.png]]
	- need to reindex as part of your pipeline if add or remove the pipeline
	- the index needs to represent the current state of the docs for it to give you accurate embeddings
	- will need to frequently need to do this to keep data fresh
	- this can be expensive
![[Pasted image 20250213114420.png]]
![[Pasted image 20250213115458.png]]
![[Pasted image 20250213115513.png]]
	- each chunk becomes a row in the database
	- there's no "right" chunking size/boundary, experiment
![[Pasted image 20250213115820.png]]
![[Pasted image 20250213120848.png]]
- results sorted by score (-1 to 1)
- shows where the data came from
- gives you the docs that may have the answer
![[Pasted image 20250213121148.png]]
- use replicate api service to call the external LLM
- the llama 8B gave him good results
- https://replicate.com/

![[Pasted image 20250213121355.png]]
![[Pasted image 20250213121552.png]]
- want to confine answers to context you're supplied

![[Pasted image 20250213121737.png]]
	- always good to text that the LLM is confining it's answer in the provided context