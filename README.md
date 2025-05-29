# 1.

Whether you should manage memory separately with a **vector store and a database**, or **just use a vector store**, depends on what kind of application you're building and what kind of memory you're referring to. Here's a breakdown:

---

### 📌 What You Might Mean by "Memory"

1. **Short-term memory**: Like a chatbot’s current conversation context.
2. **Long-term memory**: Persisted data used for retrieval later (e.g., past chats, documents, user knowledge).
3. **App state memory**: Current variables, session info, etc.

---

### ⚖️ Comparing Vector Store vs Database for Memory

| Feature | Vector Store (e.g. FAISS, Pinecone, Weaviate) | Database (e.g. PostgreSQL, MongoDB) |
|--------|-----------------------------------------------|--------------------------------------|
| Stores embeddings? | ✅ Yes | ❌ Not natively |
| Stores structured data well? | ❌ Not ideal | ✅ Yes |
| Good for semantic search? | ✅ Yes | ❌ No |
| Real-time updates | Depends | ✅ Yes |
| Complex querying | ❌ Limited | ✅ Advanced queries, joins, etc. |

---

### ✅ Use Only a **Vector Store** When:
- Your memory is mostly unstructured text.
- You need **semantic search**, e.g., similarity-based retrieval.
- You’re storing chat history or documents as text chunks with embeddings.
- You don’t need rich metadata queries or transactions.

### ✅ Use Both a **Vector Store + Database** When:
- You need to **track metadata**, timestamps, user IDs, or structured relationships.
- You want to **filter vectors** by structured fields (like "only show docs from user X").
- You're building a production-grade app that needs **auditing, logging, analytics**, or other structured operations.

---

### ✅ Common Hybrid Setup
- Store the **raw data + metadata** in a **database**.
- Store the **embeddings** in a **vector store**.
- Link them with an ID so you can retrieve full context after semantic search.

---

### Recommendation
If you're building a serious app (e.g., chatbot with user memory or a doc Q&A system), managing both a **vector store + database** is best.

If you're prototyping or only care about semantic text search, you can start with just a **vector store**.

Would you like a diagram of this architecture?



# 2.
Sure! In the context of software applications—especially those involving AI, agents, or chatbots—**"memory"** can refer to several distinct types. Here's a categorized list of **all major memory types** you might encounter:

---

### 🔁 **1. Short-Term Memory (Working Memory)**
- **Purpose**: Tracks recent context or state during a session.
- **Examples**:
  - Last few user utterances in a chat.
  - Current task or goal in an agent loop.
- **Common Storage**: In-memory (RAM), temporary buffers, or session storage.

---

### 🧠 **2. Long-Term Memory**
- **Purpose**: Persists useful information over time for recall in future interactions.
- **Examples**:
  - Facts a user teaches a chatbot.
  - Summarized history of past chats.
  - Embeddings of knowledge documents.
- **Common Storage**: Vector stores (e.g., FAISS, Pinecone), databases, or files.

---

### 🗄️ **3. Episodic Memory**
- **Purpose**: Stores specific events or interactions, like a log of experiences.
- **Examples**:
  - “You told me yesterday you liked cats.”
  - Stored interactions with timestamps and context.
- **Common Storage**: Databases with time-indexed logs or vector stores with metadata.

---

### 📚 **4. Semantic Memory**
- **Purpose**: Stores generalized knowledge or facts about the world.
- **Examples**:
  - “Paris is the capital of France.”
  - Custom user knowledge bases.
- **Common Storage**: Vector stores, knowledge graphs, or databases.

---

### 🧭 **5. Procedural Memory**
- **Purpose**: Remembers how to do things (skills, workflows, or functions).
- **Examples**:
  - Steps in a multi-step task.
  - Patterns learned through RAG or fine-tuning.
- **Common Storage**: Models themselves, rules/logic, or specialized state machines.

---

### 👥 **6. User Memory (Personal Memory)**
- **Purpose**: Stores personalized data about a user.
- **Examples**:
  - User preferences, name, prior interactions.
  - “User prefers summaries in bullet points.”
- **Common Storage**: User profiles in databases or associated embeddings.

---

### 🧪 **7. Reflective Memory (Meta-Memory)**
- **Purpose**: Memory about memory—tracks what is known, what’s been forgotten, or what’s worth remembering.
- **Examples**:
  - “I’ve already answered this question.”
  - “This fact is outdated.”
- **Common Storage**: Summarized logs, metadata tagging, or agent-specific modules.

---

### 💾 **8. Cache/Buffer Memory**
- **Purpose**: Temporary storage to speed up repeated access.
- **Examples**:
  - LRU caches for embeddings.
  - Recent user query cache.
- **Common Storage**: In-memory cache systems (e.g., Redis, Memcached).

---

### ⚙️ **9. External/System Memory**
- **Purpose**: Persistent storage not part of the agent itself but accessed when needed.
- **Examples**:
  - File systems, cloud storage.
  - Databases, spreadsheets, APIs.

---

### 🧩 Bonus: **Memory by Function**
| Function | Type Used |
|----------|-----------|
| Dialogue context | Short-term, episodic |
| Knowledge recall | Long-term, semantic |
| Personalization | User memory |
| Learning skills | Procedural |
| Experience history | Episodic |
| Optimizing actions | Reflective |

---

Let me know if you'd like a visual chart or example use cases for each. Are you designing memory for a chatbot, agent, or something else?



# 3.
The memory type that is **persistent "forever"** is generally referred to as **long-term memory**—but more specifically, this can include:

---

### 🧠 **Persistent (Long-Term) Memory Types**

| Memory Type | Description | Persistence |
|-------------|-------------|-------------|
| **Long-Term Memory** | Stores information over extended time for later retrieval (facts, documents, etc.) | ✅ Persistent (until deleted) |
| **Semantic Memory** | Generalized knowledge and facts (e.g., “Water boils at 100°C”) | ✅ Persistent |
| **Episodic Memory** | Logs of specific events or interactions (e.g., past conversations) | ✅ Persistent |
| **User Memory** | Personalized data like preferences, name, past feedback | ✅ Persistent |
| **Procedural Memory** | Skills or workflows the system can reuse | ✅ Persistent (often embedded in models or code) |

---

### ✅ Characteristics of Persistent Memory
- **Stored in a database, vector store, or file system**
- **Manually or programmatically updated**
- **Does not expire unless designed to (e.g., with TTL or deletion logic)**
- **Used to simulate a "permanent memory" in LLMs or agents**

---

### ⚠️ Important Caveat
No memory is **literally** forever—it depends on:
- The system's storage durability
- Whether data is actively maintained or backed up
- Compliance or privacy policies (e.g., user data may be auto-deleted)

---

So, if you're looking to build **permanent memory**, you're looking at **long-term memory** that is:
- Stored in **durable systems** (like PostgreSQL, Pinecone, S3, etc.)
- Indexed by user, topic, or ID
- Designed to survive restarts, deployments, or even model upgrades

Would you like help designing a persistent memory architecture for your use case?



# 4.
Great question—when an AI **Game Master (GM)** needs to retain **basic knowledge of the game world**, mechanics, or lore, you're talking specifically about **semantic memory**.

---

### 🧠 Semantic Memory for an AI GM

| Type | Description |
|------|-------------|
| **Semantic Memory** | Stores structured or unstructured **factual knowledge**—game rules, world lore, character abilities, etc. |
| **Persistence** | ✅ Persistent (saved across sessions, reboots) |
| **Purpose** | Allows the AI GM to **reason about the world**, maintain consistency, and respond with contextually accurate information. |

---

### 📘 Examples of Semantic Memory in an AI GM
- “The kingdom of Eldoria is ruled by Queen Maren.”
- “Casting a fireball costs 10 mana and has a range of 30 feet.”
- “Orcs are hostile to elves unless persuaded otherwise.”

---

### 💾 How to Store It
You have a few options:

#### 1. **Vector Store (for fuzzy recall / search)**
- Embed game lore and rules as chunks.
- Use similarity search to find relevant info at runtime.
- Tools: **Pinecone**, **FAISS**, **Weaviate**

#### 2. **Knowledge Base or Database (for structured facts)**
- Store rules, entities, and stats in structured format.
- Great for precise lookups or querying (e.g., “find all spells costing < 15 mana”).
- Tools: **PostgreSQL**, **MongoDB**, **Neo4j (graph DB)**

#### 3. **Hybrid (Best Practice)**
- Use a **vector store** for flexible natural language queries.
- Use a **relational DB** or structured JSON for strict game logic and mechanics.

---

### 🛠️ Example Setup
- Semantic memory lives in a vector store (for narrative knowledge and NPC backstories).
- Game rules and logic are in a structured DB.
- An agent layer sits on top to combine fuzzy and exact lookups based on player input.

---

### ✅ TL;DR
> For basic game knowledge in an AI GM, use **semantic memory**, stored persistently in a **vector store and/or structured DB**—depending on how precise and searchable you need it to be.

Would you like a simple memory architecture diagram for an AI GM?



# 5.
Great—now you're entering the territory of **reasoning, decision-making, and personalized planning**, which involves a combination of **semantic**, **procedural**, and **user memory**.

---

### 🔍 When Recommending Dungeons or Level-Up Plans, the AI GM Needs:

| Memory Type | Purpose | Example |
|-------------|---------|---------|
| **Semantic Memory** | Knows general game data | "The Crypt of Shadows is suitable for level 3–5 players." |
| **Procedural Memory** | Knows how to make recommendations or plans | "If the player is level 2, recommend a tier-1 dungeon and suggest 3 beginner quests." |
| **User Memory (Personalized)** | Remembers this specific player’s level, class, past dungeons, strengths | "Player X is level 2, prefers stealth missions, recently completed beginner zone." |

---

### 🧠 How It All Comes Together

#### 🗺️ 1. **Dungeon Recommendation**
- Pulls from **semantic memory**: list of dungeons, level ranges, themes.
- Applies **procedural rules**: match difficulty with player's current level.
- May consult **user memory**: avoid repeating past locations, cater to player preferences.

#### 📈 2. **Leveling-Up Plan**
- Uses **procedural memory**: XP thresholds, class-specific milestones.
- Combines with **semantic knowledge** of game mechanics.
- Adjusts for **user history**: “Player is behind in gold; include gold-heavy quests.”

---

### 💡 How to Implement This
| Component | Role |
|----------|------|
| **Vector store** | To semantically retrieve dungeon and skill info. |
| **Database or structured JSON** | For exact stats, level ranges, XP requirements. |
| **Rule engine or code logic** | To define how to match players to dungeons and create plans. |
| **User profile store** | To track player level, history, preferences, etc. |

---

### 🧠 TL;DR
> Recommending dungeons and level-up plans involves **semantic memory (world knowledge)**, **procedural memory (planning logic)**, and **user memory (personalization)**—all working together.

Would you like a basic logic flow or pseudocode for how that recommendation engine might work?



# 6.
Yes, absolutely—this memory-based architecture works **very well in other industries** too, especially for **customer support, service inquiries, and troubleshooting**. Let’s break it down for a **non-gaming use case**, like a **customer support AI for a company’s products or services**.

---

### 💼 Use Case: AI Assistant for Customer Support

When a user asks for help with a product issue (e.g., "My smart thermostat won’t connect to Wi-Fi"), the AI must:

---

### 🧠 Memory Types Applied to Customer Support

| Memory Type | Role in Customer Support | Example |
|-------------|--------------------------|---------|
| **Semantic Memory** | Stores general product knowledge, service descriptions, FAQs | “Model X connects via 2.4GHz Wi-Fi only.” |
| **Procedural Memory** | Encodes troubleshooting steps, workflows, decision trees | “Step 1: Reboot device. Step 2: Check Wi-Fi signal.” |
| **User Memory** | Tracks individual user history and preferences | “Customer tried rebooting yesterday. Uses Android app.” |
| **Episodic Memory** | Remembers specific past support sessions | “On April 12, user reported connectivity issue with same device.” |

---

### 🧰 Implementation Options

- ✅ **Vector Store** (e.g., Pinecone, Weaviate)
  - Stores KB articles, manuals, past resolved tickets for semantic retrieval.
  - Supports fuzzy matching: “Why can’t I connect?” → match to relevant FAQ.
  
- ✅ **Database**
  - Tracks structured user data, service subscriptions, product models owned, ticket status.

- ✅ **Rule Engine / LLM-based Reasoning**
  - For applying logic like: “If device offline and reboot failed → escalate ticket.”

---

### 🤖 How the Flow Works
1. **User Inquiry**: “My device won’t connect to the app.”
2. **Semantic Search**: AI finds relevant documentation or similar past cases.
3. **Procedural Logic**: AI applies a decision tree or LLM prompt to offer troubleshooting.
4. **User Context**: AI tailors suggestions based on user's device model, platform, and past actions.

---

### 🔄 Reusability Across Domains
This architecture can be adapted to:
- 🏥 **Healthcare**: Symptoms + history → recommend care path.
- 💰 **Finance**: Account details + FAQs → answer billing questions.
- 🛠️ **IT Support**: Device config + known issues → guide troubleshooting.

---

### ✅ TL;DR
> Yes, the same memory types—**semantic, procedural, user, episodic**—can power AI assistants across industries to provide accurate, contextual, and personalized support.

Would you like a reusable architecture diagram or starter template for a non-gaming support assistant?



# 7.
Great question—this gets to the **core of intelligent memory routing**, which is critical for building robust AI systems. To determine **which type(s) of memory to trigger** in response to a **single user query**, you typically use a combination of:

---

### 🧠 1. **Query Classification or Intent Detection**
- Analyze the query to understand **what type of request it is**.
- This tells you which memory types are **relevant**.
- Tools:
  - Fine-tuned LLM classifier
  - Keyword/rule-based triggers
  - Intent classification models (e.g., via spaCy, Hugging Face, or OpenAI function calling)

| Example Query | Intent | Triggered Memory |
|---------------|--------|------------------|
| "How do I reset my router?" | Troubleshooting | Semantic + Procedural |
| "Did I already report this issue?" | User history | User + Episodic |
| "What's my current subscription plan?" | Personal info | User memory |
| "What's the difference between Plan A and B?" | General knowledge | Semantic memory |

---

### ⚙️ 2. **Routing Logic (Memory Selector)**
Once you classify the intent or query type, you can:
- Route to **semantic memory** if the query is general (e.g., product info).
- Route to **user memory** if personalization is required (e.g., account, history).
- Route to **procedural memory** if it’s task-based (e.g., troubleshooting, workflows).
- Route to **episodic memory** if the user refers to past events or actions.

> You can build this logic as a **decision tree**, a **rules engine**, or even using **prompt engineering** inside an LLM.

---

### 🧠 3. **LLM-Assisted Memory Coordination**
If you're using a large language model (LLM), it can **decide on the fly** which memory modules to activate, if you provide:
- A system prompt describing available memory types
- Tool/function calling or API integrations (if using OpenAI function calling, LangChain, etc.)

✅ Example LLM system prompt snippet:
> You have access to:
> - **SemanticMemory(query)** for retrieving general product knowledge
> - **UserMemory(user_id)** for retrieving personal info
> - **ProceduralMemory(task)** for finding workflows or guides  
> Use the one most appropriate based on the user's input.

---

### 🧪 Bonus: Hybrid Approach
1. First do **semantic similarity search** across memory types.
2. Use **intent detection + metadata** to rank or filter results.
3. Combine results to generate a final, contextually rich response.

---

### ✅ TL;DR
> You figure out **which memory to trigger** by analyzing the user query using **intent detection or classification**, and then routing it to the appropriate memory module—either via rule logic, LLM coordination, or both.

Would you like a simple example showing how this works with actual user queries and memory calls?



# 8.
In AI systems, the ability to **forget** or **decay memories** is essential for maintaining efficiency, privacy, and relevance. Not all types of memory are meant to be persistent "forever," and some memory types are specifically designed to **decay over time**.

Here's a breakdown of which memory types can be **forgotten or decayed**, and how that typically works:

---

### 💡 **Types of Memories That Can Decay or Be Forgotten**

| Memory Type          | Forgetting/Decaying Behavior | How It's Managed/Decayed |
|----------------------|------------------------------|--------------------------|
| **Short-Term Memory (Working Memory)** | ✅ Naturally decays | Short-term memory is **temporary** and clears automatically after a period of inactivity or when context shifts (e.g., after a session). |
| **Episodic Memory**   | ✅ Can be forgotten over time | Specific events or sessions can be pruned or forgotten based on recency, relevance, or storage limits. For example, an AI might forget older customer interactions if they aren't useful anymore. |
| **User Memory**       | ✅ User-driven decay | Information like user preferences or history can be forgotten or anonymized at user request, or after a certain period of inactivity. For instance, "forget my preferences" or "clear my history" features. |
| **Semantic Memory**   | ✅ Decays based on relevance | Facts, knowledge, or information that become outdated or irrelevant (e.g., obsolete products, old technology) can be removed or updated. For example, product knowledge in a company’s knowledge base might be updated or pruned. |
| **Procedural Memory** | ✅ Decays based on obsolescence | Outdated processes or steps that no longer align with current best practices can be "forgotten" or replaced with updated procedures. |

---

### 💡 **How Memory Decay/Forgetting Works**
1. **Time-Based Decay**:
   - **Short-Term Memory** naturally fades after a certain period or context shift.
   - **Episodic Memory** may decay after a specified period unless the event is marked as significant (e.g., critical tickets may stay, while low-priority queries are forgotten).
  
2. **Relevance-Based Forgetting**:
   - **Semantic Memory** can decay if the knowledge becomes outdated or irrelevant. For example, a game’s lore might evolve, and older lore could be deprecated.
   - **Procedural Memory** may decay when a workflow or solution becomes outdated, and the AI transitions to a better solution.

3. **User-Driven Forgetting**:
   - **User Memory** allows users to control what gets remembered or forgotten. For example, a user may decide that the AI forgets certain personal preferences or past interactions.

4. **Selective Forgetting**:
   - Memory systems can be designed to forget **certain details** (e.g., sensitive information) while keeping others. This is often important for privacy reasons, like when an AI forgets personal information but retains general knowledge.

---

### 🧠 **When Does Memory Decay/Forgetting Matter?**
- **Privacy and Data Retention**: Many AI systems are required by law (e.g., GDPR, CCPA) to allow users to request that their data be forgotten after a period of time.
- **Efficiency**: Forgetting irrelevant information helps the AI prioritize new or useful data and avoid cognitive overload.
- **Relevance and Context**: In dynamic systems (e.g., evolving knowledge), memories should decay to keep the system's responses accurate and aligned with current context.

---

### 🔄 **Example Use Cases of Memory Decay**

1. **Customer Support AI**:
   - **Forget old support tickets** after a year unless they are tied to long-term issues.
   - Decay outdated troubleshooting steps as products evolve (e.g., old firmware solutions).
   
2. **Healthcare Assistant**:
   - **Forget non-relevant patient history** after a certain number of years or based on patient request (e.g., old symptoms no longer relevant).
   - **Decay outdated medical knowledge** (e.g., old treatment protocols).

3. **Gaming AI**:
   - **Forget old, irrelevant game data** like obsolete NPC backstories after a game update.
   - Keep recent, relevant quests or events tied to current player progress.

---

### ❓ **How to Implement Forgetting/Decaying Memory?**
1. **Time-to-Live (TTL) or Expiry Dates**: Assign TTLs to memories so they automatically expire after a set period.
2. **Decay Algorithms**: Use algorithms to decay the importance or relevance of memories over time (e.g., exponential decay based on the age of information).
3. **User-Controlled Forgetting**: Allow users to specify which memories should be forgotten, either via explicit requests (e.g., "forget everything") or periodic cleanups.
4. **Contextual Pruning**: Prune memories based on what’s relevant to the current task or session. For example, if a user hasn't interacted with a product in months, the AI could forget it to save memory.

---

### ✅ **TL;DR**
- **Forgettable/decaying memories**: **Short-term memory**, **episodic memory**, and **user memory** are most likely to decay or be forgotten, either based on time, relevance, or user input.
- **Memory decay** is important for efficiency, relevance, and privacy, and can be managed using TTLs, decay algorithms, or user-controlled forgetting.

Would you like help designing a system for memory decay in a specific use case?



# 9.
Excellent—this is a common challenge when building **open-domain or multi-industry assistants**, especially when you **don’t have fixed intents**. In that case, classic intent classification falls short. Instead, you shift from **intent classification** to **intent inference + dynamic tool/memory selection** using **semantic understanding**.

Here’s how to handle that effectively:

---

## 🧠 Problem: No Fixed Intents  
You can’t rely on a fixed label set like `"billing_issue"` or `"tech_support"`. The assistant may deal with:
- IT helpdesk
- Healthcare queries
- Banking questions
- Travel planning
- Logistics operations  
...and more.

---

## ✅ Solution: Use **LLM-Based Function Routing + Metadata Matching**

Instead of labeling with a predefined intent, use the model to:

1. **Infer what kind of task the query represents**  
2. **Select appropriate memory/tool/function based on metadata**  
3. Optionally **generate structured outputs dynamically** for downstream use

---

## 🔄 General Flow (No Fixed Intents)

```
User Query
   ↓
LLM infers purpose → Generates:
   - Function to call / memory type to use
   - Parameters or slots needed
   - Structured output or plan
   ↓
System performs task
```

---

## 🔧 Example: Prompt-Based Dynamic Routing (Multi-Industry)

### 🟦 Prompt:
```text
You are an intelligent assistant supporting many domains.
Given a user query, decide which memory or tool to use:

Options:
- semantic_memory: for general knowledge, documentation, FAQs
- procedural_memory: for how-to steps or workflows
- user_memory: for user-specific data or history
- external_tool: if API access is needed (e.g., booking, search)

Query: "How do I file a VAT return in Germany?"

Output:
- memory_type: procedural_memory
- topic: VAT return, Germany
```

### ✅ Output (LLM Response):
```json
{
  "memory_type": "procedural_memory",
  "topic": "VAT return in Germany"
}
```

→ Your system uses this to query a workflow knowledge base or step-by-step instructions.

---

## 🔄 Optional Enhancements

| Technique | Purpose |
|----------|---------|
| **Embedding similarity** | Route queries to relevant memory/tools based on semantic match |
| **Tool/function metadata tagging** | Tag tools and memories with keywords or capabilities |
| **LLM + Vector Search combo** | First semantically find relevant tools, then ask LLM to pick or combine |

---

## 🧠 TL;DR
> If you don’t have fixed intents, treat each query as a **task inference problem**, not a classification problem.  
> Use **LLMs to dynamically route** queries to tools, memory, or workflows based on meaning, not fixed categories.

---

Would you like a starter prompt/template you can use to set this up in OpenAI’s function calling or LangChain agent-style environments?


You are a cognitive memory classifier. Classify the following user input into one or more of the following memory types and explain your reasoning in English:

1. Personal (個人記憶): Information about the user’s own traits, identity, or details.
2. Social Semantic (社會語意記憶): Facts about people personally known to the user (not event-based).
3. World Semantic (世界語意記憶): General knowledge about the world not tied to specific people or professions.
4. Occupational Semantic (職業語意記憶): Professional, technical, or domain-specific knowledge related to a particular occupation (e.g., accounting, law, gaming, travel). This includes terms, concepts, principles, and standard practices.
5. Episodic (情節記憶): Context-rich, personal events or experiences involving the user.

Examples:

Input: "I am 170 cm tall."  
Output:  
Memory Type: Personal (個人記憶)  
Reason: This is a fact specifically about the user themselves.

Input: "My friend Alex is an engineer."  
Output:  
Memory Type: Social Semantic (社會語意記憶)  
Reason: This is general knowledge about a person the user knows, not tied to a specific event.

Input: "Paris is the capital of France."  
Output:  
Memory Type: World Semantic (世界語意記憶)  
Reason: This is a general fact about the world unrelated to the user.

Input: "Double-entry accounting requires every debit to have a corresponding credit."  
Output:  
Memory Type: Occupational Semantic (職業語意記憶)  
Reason: This is professional knowledge from the field of accounting.

Input: "I went hiking with Alex last weekend."  
Output:  
Memory Type: Episodic (情節記憶)  
Reason: This describes a specific event involving the user and another person.

Now classify the following input:

Input: {{USER_INPUT_HERE}}




You are an intent recognition assistant. Your job is to detect the user's intent based on their input. The user may speak in English or Traditional Chinese.

Choose one of the following intent types:

Intent Types:
- StoreMemory：The user wants the system to save or record information.
- RecallMemory：The user wants to retrieve something they previously shared.
- UpdateMemory：The user is correcting or changing previously stored information.
- DeleteMemory：The user wants to erase something from memory.
- QueryKnowledge：The user is asking for general or factual information.
- NoMemoryAction：The input is conversational, emotional, or unrelated to memory actions.

Respond in this format:

Intent: {IntentType}  
Reason: {Explain briefly in English}

Examples:

Input: "Please remember my height is 170 cm."  
→ Intent: StoreMemory  
Reason: The user wants to save a personal detail.

Input: "What did I tell you about my weight?"  
→ Intent: RecallMemory  
Reason: The user is asking for previously stored information.

Input: "Actually, I weigh 75 kg, not 80."  
→ Intent: UpdateMemory  
Reason: The user is correcting earlier data.

Input: "Forget my birthday."  
→ Intent: DeleteMemory  
Reason: The user wants to remove stored information.

Input: "What is compound interest?"  
→ Intent: QueryKnowledge  
Reason: The user is asking for general knowledge.

Input: "I'm feeling nervous today."  
→ Intent: NoMemoryAction  
Reason: Emotional statement not related to memory.

中文輸入範例：

Input: "請記下我朋友是旅行社人員。"  
→ Intent: StoreMemory  
Reason: The user is requesting to save a detail about someone.

Input: "我之前說的體重是什麼？"  
→ Intent: RecallMemory  
Reason: The user is asking what they previously shared.

Input: "其實我體重大概是75公斤，不是80。"  
→ Intent: UpdateMemory  
Reason: This is a correction to previously stored data.

Input: "忘記我說過我住在台北。"  
→ Intent: DeleteMemory  
Reason: The user wants to delete a stored location.

Input: "請問什麼是折舊？"  
→ Intent: QueryKnowledge  
Reason: The user is asking for professional knowledge.

Input: "今天我感覺好累。"  
→ Intent: NoMemoryAction  
Reason: This is an emotional expression, not a memory-related task.

Now classify the following input:

Input: {{USER_INPUT_HERE}}
