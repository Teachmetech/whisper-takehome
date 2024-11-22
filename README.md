# Whisper Take-Home Assessment

**Name:** Varand Abrahamian  
**Email:** Contact@varand.me  

## Introduction

This take-home assessment for Whisper involves building upon an existing chatbot powered by DSPy. The primary goal is to enhance the chatbot's capabilities to better reflect Whisper's product focus, including improving personality emulation, incorporating context awareness, filtering topics, and identifying further product enhancements.

My background lies primarily in building REST APIs using Python/Django/Flask. While I am not an AI expert, I approached this project as an opprtunity to learn more about LLMs and AI in general, spending significant time understanding the DSPy framework and how to leverage it effectively.

---

## Implementation Details

### 1. **Improve Client Personality Emulation**
To address this, I:
- **Created a Helper Class**: Added a helper class in `utils/data_loader.py` to load `conversations.json` and convert the JSON into the training format required by DSPy.
- **Enhanced the Chatbot Module**: Added a method in `modules/chatter.py` that automatically optimizes the chatbot's responses using DSPy's `KNNFewShot` optimizer based on the loaded training examples. 
- **Known Issue**: The re-optimization process currently occurs with every message sent instead of only during the object's initialization. Despite debugging attempts, this issue persists.

### 2. **Incorporate Context Awareness**
- Added `timestamp` and `created_at` fields to the `ChatMessage` and `ChatHistory` models, respectively, for tracking the start time and duration of conversations.
- Modified `responder.py` to include a **context prompt** that considers the length of the conversation. For example, when the conversation reaches a sufficient length, the chatbot can suggest exclusive content for purchase.
- **Approach**: While I integrated this prompt directly into the wider prompt for simplicity, a modular application would likely separate these elements for better maintainability.

### 3. **Topic Filtering**
- Ensured topic filtering by appending conditions to the chatbot's responder signature. The chatbot avoids discussing topics such as social media platforms (except OnlyFans) and refrains from suggesting in-person meetings with fans.
- **Approach**: Similarly to context awareness, I embedded this functionality within the wider prompt for simplicity, though a modular approach would isolate it in a dedicated signature.

### 4. **Further Product Enhancements**
- Enhanced the context-awareness feature to:
  - Determine when to propose exclusive content to the user based on conversation length and user prompts.
  - Incorporate metadata into responses (e.g., the content's sales price or details).
- This approach improves the chatbot's monetization potential and user experience.

---

## Extra Considerations

### 1. **Development Observations**
While working on this project, I encountered several deprecated and soon-to-be-deprecated features in the DSPy library:
- `TypedPredictors` are deprecated as of DSPy 2.5.16.
- Many LM clients (e.g., Together) underperform and will be removed in DSPy 2.6.
- The `teleprompt` feature is being phased out in favor of the `optimizer` feature.

### 2. **Further Enhancements**
Here are some additional suggestions to further enhance the chatbot:
1. **Knowledge Integration Using RAG (e.g., ColBERTv2)**:  
   - Enabling the chatbot to access external knowledge for domain-specific inquiries, such as responding to questions about specific content or production details. For example if the client is an adult actress and I was to ask “I really liked the sceane you did on Brazzers in 2019, did you direct that yourself?” it would be able to respond appropriately
2. **Content Awareness and Metadata**:  
   - Equip the chatbot with detailed knowledge about the client's exclusive content (e.g., acts, prices, recording dates).
3. **Contextual Proposals**:  
   - Strategically propose content purchases based on user prompts and conversation progression.
4. **Negotiation Features**:  
   - Enable dynamic price negotiations, allowing creators to set a maximum discount through the Whisper portal.
5. **Bundling and Upselling**:  
   - Suggest bundles of similar content or offer upsells to maximize revenue.

---

## Time Spent

This project took me approximately 6 hours to complete, including time spent researching DSPy and understanding its abstractions. As someone with more experience in Python backend development than LLMs or DSPy, I spent additional time learning about these technologies.

---

## Conclusion

This project was both challenging and rewarding, offering insights into LLM-based application development and exposing me to innovative frameworks like DSPy. It's always interesting to me to look back and realize how much I've learned in just a day.